# Muse Local Deployment Guide

## Overview
The Muse Local Orchestrator validates system resources and determines deployment feasibility for the Adobe Muse agent constellation.

## Quick Start

### Install Dependencies
```bash
pip install psutil requests
```

### Run System Validation
```bash
# Full system test with recommendations
python lib/muse_local_orchestrator.py test

# Validate specific deployment mode
python lib/muse_local_orchestrator.py validate [minimal|essential|full]

# Check local Ollama alternatives
python lib/muse_local_orchestrator.py local
```

## System Requirements Analysis

### Deployment Modes

**Minimal Mode** (Critical agents only):
- Orchestrator + Presenter
- **VRAM**: 16GB required
- **RAM**: 32GB required

**Essential Mode** (Critical + High priority):
- Adds DocumentScribe + Firefly agents
- **VRAM**: 20GB required  
- **RAM**: 40GB required

**Full Mode** (All agents):
- Complete agent constellation
- **VRAM**: 22GB required
- **RAM**: 42GB required

### Current System Example
```
System: NVIDIA RTX A1000 Laptop GPU
- Total VRAM: 4.0GB
- Available VRAM: 3.9GB
- Total RAM: 31.7GB
- Available RAM: 14.3GB

Result: ❌ INSUFFICIENT RESOURCES for all modes
Recommendation: Use local Ollama models
```

## Local Alternatives

### Ollama Installation
```bash
# Install Ollama
curl -fsSL https://ollama.ai/install.sh | sh

# Pull recommended models
ollama pull mistral:7b     # 4GB VRAM, efficient processing
ollama pull llama3:8b      # 6GB VRAM, higher capability
ollama pull codellama:7b   # 4GB VRAM, technical tasks
```

### Resource-Optimized Model Mapping
```
High-End Systems (8GB+ VRAM):
├── Critical Agents → llama3:8b
└── Other Agents → mistral:7b

Low-End Systems (4GB VRAM):
├── All Agents → mistral:7b
└── Fallback → CPU processing
```

## Error Messages

### Insufficient VRAM
```
❌ Insufficient VRAM: Need 16.0GB, have 3.9GB available (Total: 4.0GB)
```
**Solutions**:
1. Use local Ollama models (2-6GB VRAM)
2. Deploy to cloud with GPU instances
3. Use CPU-only processing (slow)

### Insufficient RAM
```
❌ Insufficient RAM: Need 32.0GB, have 14.3GB available (Total: 31.7GB)
```
**Solutions**:
1. Close other applications
2. Use smaller local models
3. Implement model swapping

### No GPU Detected
```
⚠️ No GPU detected - will fallback to CPU processing (very slow)
```
**Solutions**:
1. Install GPU drivers
2. Use cloud deployment
3. Accept slower CPU processing

## Output Files

The orchestrator generates:
- `muse_system_test_results.json` - Complete validation report
- Console output with recommendations
- Resource breakdown by agent

## Integration with Muse Architecture

This orchestrator validates the compute requirements from our [Muse Architecture Analysis](../lib/r-api-classes/muse-diagram.mermaid):

- **Orchestrator** (Critical) → High-compute model required
- **Presenter** (Critical) → High-compute model required  
- **DocumentScribe** (High) → Medium-compute model
- **Firefly Agents** (High) → Medium-compute model
- **Utilities** (Low) → Efficient models

The validation ensures each agent tier gets appropriate compute resources based on workload complexity and user impact.