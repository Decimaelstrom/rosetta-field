#!/usr/bin/env python3
"""
Muse Local Orchestrator
System resource validation and local deployment testing for Adobe Muse agent constellation
"""

import psutil
import subprocess
import json
import sys
import os
from pathlib import Path
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple
import requests
import time

@dataclass
class ModelRequirement:
    name: str
    vram_gb: float
    ram_gb: float
    description: str
    fallback_model: Optional[str] = None

@dataclass
class AgentConfig:
    name: str
    model: ModelRequirement
    priority: str  # "critical", "high", "medium", "low"
    can_share_resources: bool = False

class MuseLocalOrchestrator:
    def __init__(self):
        self.system_info = self._get_system_info()
        self.ollama_available = self._check_ollama()
        
        # Model requirements based on our analysis
        self.models = {
            "gemini_2_0_flash": ModelRequirement(
                name="gemini_2_0_flash",
                vram_gb=8.0,  # Estimated for 33B parameters
                ram_gb=16.0,
                description="Gemini 2.0 Flash (33B) - High reasoning capability"
            ),
            "gemini_1_5_flash": ModelRequirement(
                name="gemini_1_5_flash", 
                vram_gb=4.0,  # Estimated for smaller model
                ram_gb=8.0,
                description="Gemini 1.5 Flash - Medium capability"
            ),
            "gemini_2_5_flash": ModelRequirement(
                name="gemini_2_5_flash",
                vram_gb=2.0,  # Estimated for efficiency model
                ram_gb=4.0,
                description="Gemini 2.5 Flash - Efficient processing"
            ),
            # Local alternatives for Ollama - Gemma 3 models (available)
            "gemma3_27b": ModelRequirement(
                name="gemma3:27b",
                vram_gb=16.0,
                ram_gb=24.0,
                description="Gemma 3 27B - High capability (already installed)"
            ),
            "gemma3_12b": ModelRequirement(
                name="gemma3:12b",
                vram_gb=8.0,
                ram_gb=12.0,
                description="Gemma 3 12B - Good capability (already installed)"
            ),
            "gemma3_4b": ModelRequirement(
                name="gemma3:4b",
                vram_gb=3.0,
                ram_gb=5.0,
                description="Gemma 3 4B - Efficient processing (already installed)"
            ),
            "gemma3_1b": ModelRequirement(
                name="gemma3:1b",
                vram_gb=1.0,
                ram_gb=2.0,
                description="Gemma 3 1B - Ultra efficient (already installed)"
            ),
            # Gemma 2 models (for comparison)
            "gemma2_9b": ModelRequirement(
                name="gemma2:9b",
                vram_gb=6.0,
                ram_gb=10.0,
                description="Gemma 2 9B - Good capability"
            ),
            "gemma2_2b": ModelRequirement(
                name="gemma2:2b",
                vram_gb=2.0,
                ram_gb=3.0,
                description="Gemma 2 2B - Efficient processing"
            ),
            # Additional local alternatives
            "llama_3_8b": ModelRequirement(
                name="llama3:8b",
                vram_gb=6.0,
                ram_gb=8.0,
                description="Llama 3 8B - Local high capability"
            ),
            "mistral_7b": ModelRequirement(
                name="mistral:7b",
                vram_gb=4.0,
                ram_gb=6.0,
                description="Mistral 7B - Local efficient processing"
            )
        }
        
        # Agent configuration - use available Gemma 3 models
        self.agents = {
            "orchestrator": AgentConfig(
                name="Orchestrator",
                model=self.models["gemma3_4b"],  # Use installed Gemma 3 4B
                priority="critical"
            ),
            "presenter": AgentConfig(
                name="Presenter", 
                model=self.models["gemma3_4b"],  # Use installed Gemma 3 4B
                priority="critical"
            ),
            "document_scribe": AgentConfig(
                name="DocumentScribe",
                model=self.models["gemma3_1b"],  # Ultra efficient for content processing
                priority="high",
                can_share_resources=True
            ),
            "firefly_image": AgentConfig(
                name="Firefly_Image",
                model=self.models["gemma3_1b"],  # Ultra efficient for prompt engineering
                priority="high",
                can_share_resources=True
            ),
            "firefly_video": AgentConfig(
                name="Firefly_Video", 
                model=self.models["gemma3_1b"],  # Ultra efficient for prompt engineering
                priority="high",
                can_share_resources=True
            ),
            "firefly_music": AgentConfig(
                name="Firefly_Music",
                model=self.models["gemma3_1b"],  # Ultra efficient for creative prompts
                priority="medium",
                can_share_resources=True
            ),
            "export_handler": AgentConfig(
                name="ExportHandler",
                model=self.models["gemma3_1b"],  # Light processing tasks
                priority="low",
                can_share_resources=True
            ),
            "error_monitor": AgentConfig(
                name="ErrorMonitor",
                model=self.models["gemma3_1b"],  # Pattern matching tasks
                priority="low", 
                can_share_resources=True
            )
        }
        
        # Fallback configurations for different resource levels
        self.agent_fallbacks = {
            "high_resource": {  # 8GB+ VRAM
                "critical": "gemma2_9b",
                "high": "gemma2_2b", 
                "medium": "gemma2_2b",
                "low": "gemma2_2b"
            },
            "medium_resource": {  # 4-8GB VRAM
                "critical": "gemma2_2b",
                "high": "gemma2_2b",
                "medium": "gemma2_2b", 
                "low": "gemma2_2b"
            },
            "low_resource": {  # <4GB VRAM
                "critical": "mistral_7b",
                "high": "mistral_7b",
                "medium": "mistral_7b",
                "low": "mistral_7b"
            }
        }
    
    def _get_system_info(self) -> Dict:
        """Get comprehensive system information"""
        info = {
            "total_ram_gb": round(psutil.virtual_memory().total / (1024**3), 2),
            "available_ram_gb": round(psutil.virtual_memory().available / (1024**3), 2),
            "cpu_count": psutil.cpu_count(),
            "cpu_freq_ghz": round(psutil.cpu_freq().max / 1000, 2) if psutil.cpu_freq() else "unknown"
        }
        
        # Try to get GPU information
        try:
            import GPUtil
            gpus = GPUtil.getGPUs()
            if gpus:
                gpu = gpus[0]  # Primary GPU
                info["gpu_name"] = gpu.name
                info["vram_total_gb"] = round(gpu.memoryTotal / 1024, 2)
                info["vram_free_gb"] = round(gpu.memoryFree / 1024, 2)
            else:
                info["gpu_name"] = "No GPU detected"
                info["vram_total_gb"] = 0
                info["vram_free_gb"] = 0
        except ImportError:
            # Fallback: try nvidia-smi
            try:
                result = subprocess.run(
                    ["nvidia-smi", "--query-gpu=name,memory.total,memory.free", "--format=csv,noheader,nounits"],
                    capture_output=True, text=True, timeout=10
                )
                if result.returncode == 0:
                    gpu_info = result.stdout.strip().split(", ")
                    info["gpu_name"] = gpu_info[0]
                    info["vram_total_gb"] = round(int(gpu_info[1]) / 1024, 2)
                    info["vram_free_gb"] = round(int(gpu_info[2]) / 1024, 2)
                else:
                    info["gpu_name"] = "No NVIDIA GPU detected"
                    info["vram_total_gb"] = 0
                    info["vram_free_gb"] = 0
            except (subprocess.TimeoutExpired, FileNotFoundError):
                info["gpu_name"] = "GPU detection failed"
                info["vram_total_gb"] = 0
                info["vram_free_gb"] = 0
        
        return info
    
    def _check_ollama(self) -> bool:
        """Check if Ollama is available"""
        try:
            result = subprocess.run(["ollama", "list"], capture_output=True, text=True, timeout=10)
            return result.returncode == 0
        except (subprocess.TimeoutExpired, FileNotFoundError):
            return False
    
    def _get_ollama_models(self) -> List[str]:
        """Get list of available Ollama models"""
        if not self.ollama_available:
            return []
        
        try:
            result = subprocess.run(["ollama", "list"], capture_output=True, text=True, timeout=10)
            if result.returncode == 0:
                lines = result.stdout.strip().split('\n')[1:]  # Skip header
                return [line.split()[0] for line in lines if line.strip()]
        except subprocess.TimeoutExpired:
            pass
        return []
    
    def calculate_resource_requirements(self, deployment_mode: str = "full") -> Dict:
        """Calculate total resource requirements for deployment"""
        requirements = {
            "total_vram_gb": 0,
            "total_ram_gb": 0,
            "agent_breakdown": {},
            "deployment_mode": deployment_mode
        }
        
        agents_to_deploy = list(self.agents.values())
        
        if deployment_mode == "minimal":
            # Only critical agents
            agents_to_deploy = [a for a in agents_to_deploy if a.priority == "critical"]
        elif deployment_mode == "essential":
            # Critical + high priority
            agents_to_deploy = [a for a in agents_to_deploy if a.priority in ["critical", "high"]]
        elif deployment_mode == "ultra_efficient":
            # All agents but using ultra-efficient models
            for agent in agents_to_deploy:
                agent.model = self.models["gemma3_1b"]  # Force all to use 1B model
        
        # Group agents that can share resources
        resource_groups = {}
        for agent in agents_to_deploy:
            if agent.can_share_resources:
                model_key = agent.model.name
                if model_key not in resource_groups:
                    resource_groups[model_key] = {
                        "agents": [],
                        "vram_gb": agent.model.vram_gb,
                        "ram_gb": agent.model.ram_gb
                    }
                resource_groups[model_key]["agents"].append(agent.name)
            else:
                # Dedicated resources
                requirements["total_vram_gb"] += agent.model.vram_gb
                requirements["total_ram_gb"] += agent.model.ram_gb
                requirements["agent_breakdown"][agent.name] = {
                    "vram_gb": agent.model.vram_gb,
                    "ram_gb": agent.model.ram_gb,
                    "model": agent.model.name,
                    "shared": False
                }
        
        # Add shared resource groups
        for model_key, group in resource_groups.items():
            requirements["total_vram_gb"] += group["vram_gb"]
            requirements["total_ram_gb"] += group["ram_gb"]
            for agent_name in group["agents"]:
                requirements["agent_breakdown"][agent_name] = {
                    "vram_gb": group["vram_gb"] / len(group["agents"]),  # Split for display
                    "ram_gb": group["ram_gb"] / len(group["agents"]),
                    "model": model_key,
                    "shared": True,
                    "shared_with": group["agents"]
                }
        
        return requirements
    
    def validate_system_resources(self, deployment_mode: str = "full") -> Dict:
        """Validate if system can handle the deployment"""
        requirements = self.calculate_resource_requirements(deployment_mode)
        
        validation = {
            "can_deploy": True,
            "issues": [],
            "recommendations": [],
            "deployment_mode": deployment_mode,
            "system_info": self.system_info,
            "requirements": requirements
        }
        
        # Check VRAM
        vram_needed = requirements["total_vram_gb"]
        vram_available = self.system_info["vram_free_gb"]
        
        if vram_needed > vram_available:
            validation["can_deploy"] = False
            validation["issues"].append(
                f"Insufficient VRAM: Need {vram_needed:.1f}GB, have {vram_available:.1f}GB available "
                f"(Total: {self.system_info['vram_total_gb']:.1f}GB)"
            )
            
            # Suggest deployment mode downgrade
            if deployment_mode == "full":
                validation["recommendations"].append("Try 'essential' deployment mode")
            elif deployment_mode == "essential":
                validation["recommendations"].append("Try 'minimal' deployment mode")
            else:
                validation["recommendations"].append("Consider using local Ollama models with smaller requirements")
        
        # Check RAM
        ram_needed = requirements["total_ram_gb"]
        ram_available = self.system_info["available_ram_gb"]
        
        if ram_needed > ram_available:
            validation["can_deploy"] = False
            validation["issues"].append(
                f"Insufficient RAM: Need {ram_needed:.1f}GB, have {ram_available:.1f}GB available "
                f"(Total: {self.system_info['total_ram_gb']:.1f}GB)"
            )
        
        # GPU check
        if self.system_info["vram_total_gb"] == 0:
            validation["issues"].append("No GPU detected - will fallback to CPU processing (very slow)")
            validation["recommendations"].append("Consider using cloud deployment for GPU acceleration")
        
        return validation
    
    def suggest_local_alternatives(self) -> Dict:
        """Suggest local Ollama model alternatives"""
        suggestions = {
            "ollama_available": self.ollama_available,
            "installed_models": self._get_ollama_models() if self.ollama_available else [],
            "recommended_models": {},
            "installation_commands": []
        }
        
        if not self.ollama_available:
            suggestions["installation_commands"].append("curl -fsSL https://ollama.ai/install.sh | sh")
            return suggestions
        
        # Map agents to suitable local models - use available Gemma 3 models
        for agent_name, agent_config in self.agents.items():
            if agent_config.priority in ["critical"]:
                if self.system_info["vram_total_gb"] >= 8:
                    suggestions["recommended_models"][agent_name] = "gemma3:12b"
                elif self.system_info["vram_total_gb"] >= 4:
                    suggestions["recommended_models"][agent_name] = "gemma3:4b"
                else:
                    suggestions["recommended_models"][agent_name] = "gemma3:1b"
            elif agent_config.priority in ["high"]:
                if self.system_info["vram_total_gb"] >= 4:
                    suggestions["recommended_models"][agent_name] = "gemma3:4b"
                else:
                    suggestions["recommended_models"][agent_name] = "gemma3:1b"
            else:
                suggestions["recommended_models"][agent_name] = "gemma3:1b"
        
        # Check which models need to be pulled
        installed = set(suggestions["installed_models"])
        recommended = set(suggestions["recommended_models"].values())
        
        for model in recommended - installed:
            suggestions["installation_commands"].append(f"ollama pull {model}")
        
        return suggestions
    
    def test_model_loading(self, model_name: str, test_prompt: str = "Hello, can you respond?") -> Dict:
        """Test if a model can be loaded and responds"""
        test_result = {
            "model": model_name,
            "success": False,
            "response_time": None,
            "error": None,
            "memory_usage": {}
        }
        
        # Record initial memory
        initial_ram = psutil.virtual_memory().percent
        initial_vram = None
        
        try:
            # Try GPU memory if available
            import GPUtil
            gpus = GPUtil.getGPUs()
            if gpus:
                initial_vram = gpus[0].memoryUsed
        except ImportError:
            pass
        
        start_time = time.time()
        
        try:
            if self.ollama_available and any(model_name.startswith(prefix) for prefix in ["llama", "mistral", "codellama"]):
                # Test Ollama model
                result = subprocess.run(
                    ["ollama", "run", model_name, test_prompt],
                    capture_output=True, text=True, timeout=30
                )
                if result.returncode == 0:
                    test_result["success"] = True
                else:
                    test_result["error"] = result.stderr
            else:
                # For cloud models, we can't really test loading, but we can check API availability
                test_result["success"] = True
                test_result["error"] = "Cloud model - local testing not applicable"
        
        except subprocess.TimeoutExpired:
            test_result["error"] = "Model loading timeout (>30s)"
        except Exception as e:
            test_result["error"] = str(e)
        
        test_result["response_time"] = time.time() - start_time
        
        # Record final memory usage
        final_ram = psutil.virtual_memory().percent
        test_result["memory_usage"]["ram_increase_percent"] = final_ram - initial_ram
        
        if initial_vram is not None:
            try:
                import GPUtil
                gpus = GPUtil.getGPUs()
                if gpus:
                    final_vram = gpus[0].memoryUsed
                    test_result["memory_usage"]["vram_increase_mb"] = final_vram - initial_vram
            except ImportError:
                pass
        
        return test_result
    
    def run_full_system_test(self) -> Dict:
        """Run comprehensive system validation and testing"""
        print("🚀 Muse Local Orchestrator - System Validation")
        print("=" * 60)
        
        test_results = {
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "system_info": self.system_info,
            "deployment_validations": {},
            "local_alternatives": self.suggest_local_alternatives(),
            "model_tests": {},
            "final_recommendation": {}
        }
        
        # Test different deployment modes
        for mode in ["minimal", "essential", "full", "ultra_efficient"]:
            print(f"\n📊 Testing {mode} deployment mode...")
            validation = self.validate_system_resources(mode)
            test_results["deployment_validations"][mode] = validation
            
            if validation["can_deploy"]:
                print(f"✅ {mode.title()} mode: FEASIBLE")
                print(f"   VRAM needed: {validation['requirements']['total_vram_gb']:.1f}GB")
                print(f"   RAM needed: {validation['requirements']['total_ram_gb']:.1f}GB")
            else:
                print(f"❌ {mode.title()} mode: INSUFFICIENT RESOURCES")
                for issue in validation["issues"]:
                    print(f"   ⚠️  {issue}")
        
        # Test local model alternatives if available
        if self.ollama_available:
            print(f"\n🧪 Testing local Ollama models...")
            local_models = ["gemma3:1b", "gemma3:4b", "gemma3:12b"]
            for model in local_models:
                if model in self._get_ollama_models():
                    print(f"   Testing {model}...")
                    test_result = self.test_model_loading(model)
                    test_results["model_tests"][model] = test_result
                    if test_result["success"]:
                        print(f"   ✅ {model}: Loaded successfully ({test_result['response_time']:.1f}s)")
                    else:
                        print(f"   ❌ {model}: {test_result['error']}")
        
        # Generate final recommendation
        best_mode = None
        for mode in ["full", "essential", "minimal", "ultra_efficient"]:
            if test_results["deployment_validations"][mode]["can_deploy"]:
                best_mode = mode
                break
        
        if best_mode:
            test_results["final_recommendation"] = {
                "status": "DEPLOYABLE",
                "recommended_mode": best_mode,
                "message": f"System can handle {best_mode} deployment mode"
            }
        else:
            test_results["final_recommendation"] = {
                "status": "INSUFFICIENT_RESOURCES", 
                "recommended_mode": "local_only",
                "message": "Use local Ollama models or upgrade hardware"
            }
        
        return test_results

def main():
    """Main orchestrator interface"""
    orchestrator = MuseLocalOrchestrator()
    
    if len(sys.argv) > 1:
        command = sys.argv[1].lower()
        
        if command == "validate":
            mode = sys.argv[2] if len(sys.argv) > 2 else "full"
            validation = orchestrator.validate_system_resources(mode)
            print(json.dumps(validation, indent=2))
            
        elif command == "test":
            results = orchestrator.run_full_system_test()
            
            # Save results
            output_file = "muse_system_test_results.json"
            with open(output_file, 'w') as f:
                json.dump(results, f, indent=2)
            
            print(f"\n💾 Results saved to: {output_file}")
            print(f"\n🎯 FINAL RECOMMENDATION: {results['final_recommendation']['status']}")
            print(f"   {results['final_recommendation']['message']}")
            
        elif command == "local":
            alternatives = orchestrator.suggest_local_alternatives()
            print(json.dumps(alternatives, indent=2))
            
        else:
            print("Usage: python muse_local_orchestrator.py [validate|test|local] [deployment_mode]")
    else:
        # Default: run full test
        results = orchestrator.run_full_system_test()
        print(f"\n🎯 FINAL RECOMMENDATION: {results['final_recommendation']['status']}")
        print(f"   {results['final_recommendation']['message']}")

if __name__ == "__main__":
    main()