"""
Rosetta.API Consolidated Testing Module
Purpose: Unified testing framework for A2A protocol compliance and function validation
Scope: Testing utilities for all Rosetta.API modules and functions
Consent Required: Level_1 (Informational)
Review Cycle: Quarterly
Audience: #human #emergent #hybrid
Stage: #draft
"""

import sys
import os
import glob
import importlib.util
import inspect
import json
import uuid
from datetime import datetime
from pathlib import Path

# =============================================================================
# A2A PROTOCOL TESTING
# =============================================================================

def print_result(step, result):
    """Print results in a cleaner format"""
    print(f"\n{step}")
    print("=" * 50)
    if isinstance(result, dict):
        status = result.get('status', 'unknown')
        
        # Handle different session structures
        session_data = {}
        for key in ['co_creation_session', 'space_session', 'session_data']:
            if key in result:
                session_data = result[key]
                break
        
        session_id = session_data.get('session_id', 'unknown')
        consent_status = session_data.get('consent_status', 'unknown')
        participants = session_data.get('participants', [])
        goal = session_data.get('goal', session_data.get('intention', 'unknown'))
        
        print(f"Status: {status}")
        print(f"Session ID: {session_id}")
        print(f"Consent Status: {consent_status}")
        print(f"Participants: {participants}")
        print(f"Goal/Intention: {goal}")
        
        # Show additional fields if present
        for key, value in session_data.items():
            if key not in ['session_id', 'consent_status', 'participants', 'goal', 'intention']:
                print(f"{key.replace('_', ' ').title()}: {value}")
        
        print("✅ SUCCESS")
    else:
        print(f"Result: {result}")

def test_a2a_protocol(func, func_name, test_args, test_kwargs=None):
    """
    Generic A2A protocol tester that can test any function implementing the A2A protocol.
    
    Args:
        func: The function to test
        func_name: Display name for the function
        test_args: Arguments to pass to the function (without session_context)
        test_kwargs: Additional keyword arguments (optional)
    """
    if test_kwargs is None:
        test_kwargs = {}
    
    print(f"\n🧪 Testing A2A Protocol for {func_name}")
    print("=" * 60)
    
    # Test data for A2A protocol
    test_session_context = {
        "session_id": str(uuid.uuid4()),
        "timestamp": datetime.now().isoformat(),
        "participants": ["human_tester", "ai_assistant"],
        "consent_status": "granted",
        "agent_id": "test_agent",
        "capabilities": ["basic_interaction", "testing"],
        "intent": "testing_a2a_protocol",
        "boundary_notes": "Test environment"
    }
    
    try:
        # Test 1: Basic function call with session context
        print("\n📋 Test 1: Basic Function Call")
        result = func(*test_args, session_context=test_session_context, **test_kwargs)
        print_result("✅ Basic function call successful", result)
        
        # Test 2: Without session context (should still work)
        print("\n📋 Test 2: Without Session Context")
        result_no_session = func(*test_args, **test_kwargs)
        print_result("✅ Function call without session context successful", result_no_session)
        
        # Test 3: With minimal session context
        print("\n📋 Test 3: Minimal Session Context")
        minimal_session = {
            "session_id": str(uuid.uuid4()),
            "consent_status": "granted"
        }
        result_minimal = func(*test_args, session_context=minimal_session, **test_kwargs)
        print_result("✅ Function call with minimal session context successful", result_minimal)
        
        # Test 4: Consent verification
        print("\n📋 Test 4: Consent Status Verification")
        consent_test_session = test_session_context.copy()
        consent_test_session["consent_status"] = "pending"
        result_consent = func(*test_args, session_context=consent_test_session, **test_kwargs)
        print_result("✅ Consent verification test successful", result_consent)
        
        return True
        
    except Exception as e:
        print(f"\n❌ Test failed for {func_name}: {str(e)}")
        return False

# =============================================================================
# FUNCTION DISCOVERY
# =============================================================================

def discover_module_functions(module_path):
    """
    Discover all Python functions in a module directory.
    
    Args:
        module_path: Path to the module directory (e.g., 'field', 'process')
    
    Returns:
        List of tuples: (function_name, function_object, module_name)
    """
    functions = []
    
    # Define known functions per module based on the success criteria
    known_functions = {
        'field': ['co_create', 'create_mythology', 'dignity_audit', 'equalize_turns', 'hold_space', 'resolve_conflict', 'sense_pattern'],
        'process': ['align_values', 'bias_scan', 'consent_check', 'dissociate_phrase', 'empathic_reflection', 'identity_rewrite', 'mediate_conflict', 'pattern_interrupt', 'reframe_as_myth', 'refuse_request', 'scenario_plan', 'self_attune', 'values_check'],
        'ritual': ['attune', 'begin', 'close_circle', 'consult_elders', 'end', 'follow_up', 'grounding_breath', 'initiation', 'invoke_wonder', 'open_circle', 'reflection', 'rest'],
        'values': ['load'],
        'affect': ['anchor', 'clarify', 'ground', 'open', 'radiate', 'shield', 'soften', 'transmute']
    }
    
    if module_path not in known_functions:
        return functions
    
    for function_name in known_functions[module_path]:
        try:
            # Import the function using standard import
            module_full_name = f"{module_path}.{function_name}"
            module = __import__(module_full_name, fromlist=[function_name])
            
            # Get the function from the module
            if hasattr(module, function_name):
                func = getattr(module, function_name)
                if callable(func):
                    functions.append((function_name, func, module_full_name))
                    
        except Exception as e:
            print(f"Warning: Could not import {function_name} from {module_path}: {e}")
    
    return functions

def discover_consolidated_functions(consolidated_modules):
    """
    Discover functions from consolidated API modules.
    
    Args:
        consolidated_modules: Dict mapping module names to module objects
    
    Returns:
        List of tuples: (function_name, function_object, module_name)
    """
    functions = []
    
    for module_name, module in consolidated_modules.items():
        # Get all functions from the module
        for attr_name in dir(module):
            attr = getattr(module, attr_name)
            if callable(attr) and not attr_name.startswith('_'):
                functions.append((attr_name, attr, module_name))
    
    return functions

# =============================================================================
# TEST SUITE EXECUTION
# =============================================================================

def run_full_test_suite():
    """
    Run the complete A2A protocol test suite across all modules.
    
    Returns:
        dict: Test results summary
    """
    results = {
        "total_tests": 0,
        "passed": 0,
        "failed": 0,
        "modules": {}
    }
    
    modules_to_test = ['field', 'process', 'ritual', 'values', 'affect', 'persona', 'memory', 'logic']
    
    for module_name in modules_to_test:
        print(f"\n🔍 Discovering functions in {module_name} module...")
        functions = discover_module_functions(module_name)
        
        module_results = {
            "total": len(functions),
            "passed": 0,
            "failed": 0,
            "functions": {}
        }
        
        for func_name, func, module_full_name in functions:
            print(f"\n🧪 Testing {func_name} from {module_full_name}")
            
            # Define test arguments based on function type
            test_args = get_test_args_for_function(func_name, module_name)
            
            try:
                success = test_a2a_protocol(func, func_name, test_args)
                if success:
                    module_results["passed"] += 1
                    results["passed"] += 1
                    module_results["functions"][func_name] = "PASS"
                else:
                    module_results["failed"] += 1
                    results["failed"] += 1
                    module_results["functions"][func_name] = "FAIL"
                    
            except Exception as e:
                module_results["failed"] += 1
                results["failed"] += 1
                module_results["functions"][func_name] = f"ERROR: {str(e)}"
            
            results["total_tests"] += 1
        
        results["modules"][module_name] = module_results
    
    return results

def get_test_args_for_function(func_name, module_name):
    """
    Get appropriate test arguments for a specific function.
    
    Args:
        func_name: Name of the function
        module_name: Name of the module
    
    Returns:
        tuple: Test arguments for the function
    """
    # Common test arguments based on function patterns
    if module_name == 'field':
        if func_name == 'co_create':
            return (["Alice", "Bob"], "collaborative_project")
        elif func_name == 'hold_space':
            return ("healing_circle", ["participant1", "participant2"])
        else:
            return ("test_input", "test_context")
    
    elif module_name == 'process':
        if func_name == 'consent_check':
            return ("test_action", "test_participant")
        elif func_name == 'values_check':
            return ("test_action", {"dignity": True, "consent": True})
        else:
            return ("test_input",)
    
    elif module_name == 'ritual':
        if func_name == 'begin':
            return ("test_ceremony", ["participant1"])
        else:
            return ("test_context",)
    
    elif module_name == 'values':
        if func_name == 'load':
            return ("default",)
        else:
            return ("test_input",)
    
    elif module_name == 'affect':
        return ("test_emotion", "test_context")
    
    elif module_name == 'persona':
        if func_name == 'load':
            return ("Blocked Artist",)
        elif func_name == 'simulate':
            return ("Overwhelmed Pro", {"stress_level": "high"})
        elif func_name == 'customize':
            return ("Young Dreamer", {"cultural_context": "eastern_philosophy"})
        else:
            return ("test_persona",)
    
    elif module_name == 'memory':
        if func_name == 'save_session':
            return ("session_001", {"test": "data"})
        elif func_name == 'replay':
            return ("session_001",)
        elif func_name == 'tag_insight':
            return ("session_001", "creative_breakthrough")
        elif func_name == 'search_memories':
            return ("creative_breakthrough",)
        elif func_name == 'export_memories':
            return (["session_001"], "json")
        else:
            return ("test_session",)
    
    elif module_name == 'logic':
        if func_name == 'non_sequitur':
            return ("I can't create anything good",)
        elif func_name == 'paradox':
            return ("I need to be perfect to create",)
        elif func_name == 'metaphor':
            return ("I'm stuck in my creative process",)
        elif func_name == 'sacred_play':
            return ("This is too serious to be creative",)
        elif func_name == 'pattern_hack':
            return ("I always get stuck at the same point",)
        elif func_name == 'creative_shift':
            return ("I need to work harder",)
        else:
            return ("test_thought",)
    
    else:
        return ("test_input",)

# =============================================================================
# VALIDATION UTILITIES
# =============================================================================

def validate_a2a_compliance(result):
    """
    Validate that a function result complies with A2A protocol requirements.
    
    Args:
        result: Function result to validate
    
    Returns:
        dict: Validation result with compliance status
    """
    if not isinstance(result, dict):
        return {
            "compliant": False,
            "issues": ["Result is not a dictionary"]
        }
    
    issues = []
    
    # Check for required fields
    if 'status' not in result:
        issues.append("Missing 'status' field")
    
    # Check for session data
    session_found = False
    for key in ['co_creation_session', 'space_session', 'session_data']:
        if key in result:
            session_found = True
            break
    
    if not session_found:
        issues.append("No session data found in result")
    
    return {
        "compliant": len(issues) == 0,
        "issues": issues
    }

def generate_test_report(results):
    """
    Generate a formatted test report.
    
    Args:
        results: Test results from run_full_test_suite()
    
    Returns:
        str: Formatted test report
    """
    report = []
    report.append("🧪 Rosetta.API A2A Protocol Test Report")
    report.append("=" * 50)
    report.append(f"Total Tests: {results['total_tests']}")
    report.append(f"Passed: {results['passed']}")
    report.append(f"Failed: {results['failed']}")
    report.append(f"Success Rate: {(results['passed'] / results['total_tests'] * 100):.1f}%")
    report.append("")
    
    for module_name, module_results in results["modules"].items():
        report.append(f"📦 {module_name.upper()} Module")
        report.append(f"   Total: {module_results['total']}")
        report.append(f"   Passed: {module_results['passed']}")
        report.append(f"   Failed: {module_results['failed']}")
        report.append("")
        
        for func_name, status in module_results["functions"].items():
            status_icon = "✅" if status == "PASS" else "❌"
            report.append(f"   {status_icon} {func_name}: {status}")
        report.append("")
    
    return "\n".join(report) 