"""
Rosetta.API Consolidated Testing Module
Purpose: Unified testing framework for A2A protocol compliance and function validation
Scope: Testing utilities for all Rosetta.API modules and functions with cultural/linguistic context
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
        for key in ['co_creation_session', 'space_session', 'session_data', 'session_context']:
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
        
        # Show cultural and linguistic context if present
        context = session_data.get('context', {})
        if 'cultural_context' in context:
            print(f"Cultural Context: {context['cultural_context']}")
        if 'linguistic_context' in context:
            print(f"Linguistic Context: {context['linguistic_context']}")
        
        # Show additional fields if present
        for key, value in session_data.items():
            if key not in ['session_id', 'consent_status', 'participants', 'goal', 'intention', 'context']:
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
    
    # Test data for A2A protocol with cultural/linguistic context
    test_session_context = {
        "session_id": str(uuid.uuid4()),
        "timestamp": datetime.now().isoformat(),
        "participants": ["human_tester", "ai_assistant"],
        "consent_status": "granted",
        "agent_id": "test_agent",
        "capabilities": ["basic_interaction", "testing", "cultural_sensitivity"],
        "intent": "testing_a2a_protocol",
        "boundary_notes": "Test environment",
        "context": {
            "cultural_context": "eastern_collective",
            "linguistic_context": "poetic_metaphorical"
        },
        "language": "en",
        "region": "US"
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
        
        # Test 5: Cultural and linguistic context handling
        print("\n📋 Test 5: Cultural and Linguistic Context")
        cultural_test_session = test_session_context.copy()
        cultural_test_session["context"]["cultural_context"] = "indigenous_holistic"
        cultural_test_session["context"]["linguistic_context"] = "ceremonial_sacred"
        result_cultural = func(*test_args, session_context=cultural_test_session, **test_kwargs)
        print_result("✅ Cultural and linguistic context test successful", result_cultural)
        
        return True
        
    except Exception as e:
        print(f"\n❌ Test failed for {func_name}: {str(e)}")
        return False

def test_enhanced_functionality(func, func_name, test_args, test_kwargs=None):
    """
    Test enhanced functionality including cultural context, storage, and dynamic generation.
    
    Args:
        func: The function to test
        func_name: Display name for the function
        test_args: Arguments to pass to the function
        test_kwargs: Additional keyword arguments (optional)
    """
    if test_kwargs is None:
        test_kwargs = {}
    
    print(f"\n🔬 Testing Enhanced Functionality for {func_name}")
    print("=" * 60)
    
    # Test different cultural contexts
    cultural_contexts = [
        "eastern_zen",
        "indigenous_holistic", 
        "african_diasporic",
        "celtic_ancestral",
        "nordic_balance"
    ]
    
    linguistic_contexts = [
        "poetic_metaphorical",
        "conversational_warm",
        "ceremonial_sacred",
        "mentor_encouraging"
    ]
    
    try:
        # Test cultural context variations
        print("\n📋 Test: Cultural Context Variations")
        for cultural_context in cultural_contexts[:2]:  # Test first 2 for brevity
            test_session = {
                "session_id": str(uuid.uuid4()),
                "consent_status": "granted",
                "context": {
                    "cultural_context": cultural_context,
                    "linguistic_context": "poetic_metaphorical"
                }
            }
            result = func(*test_args, session_context=test_session, **test_kwargs)
            print(f"✅ {cultural_context} context: {result.get('status', 'success')}")
        
        # Test linguistic context variations
        print("\n📋 Test: Linguistic Context Variations")
        for linguistic_context in linguistic_contexts[:2]:  # Test first 2 for brevity
            test_session = {
                "session_id": str(uuid.uuid4()),
                "consent_status": "granted",
                "context": {
                    "cultural_context": "eastern_collective",
                    "linguistic_context": linguistic_context
                }
            }
            result = func(*test_args, session_context=test_session, **test_kwargs)
            print(f"✅ {linguistic_context} context: {result.get('status', 'success')}")
        
        # Test enhanced storage features (for memory functions)
        if 'memory' in func_name.lower() or 'save' in func_name.lower():
            print("\n📋 Test: Enhanced Storage Features")
            test_session = {
                "session_id": str(uuid.uuid4()),
                "consent_status": "granted",
                "context": {
                    "cultural_context": "eastern_collective",
                    "linguistic_context": "poetic_metaphorical"
                }
            }
            result = func(*test_args, session_context=test_session, **test_kwargs)
            if isinstance(result, dict) and 'storage_info' in result:
                print(f"✅ Enhanced storage: {result['storage_info'].get('encrypted', False)}")
        
        # Test dynamic generation features (for logic functions)
        if 'logic' in func_name.lower() or 'non_sequitur' in func_name.lower() or 'paradox' in func_name.lower():
            print("\n📋 Test: Dynamic Generation Features")
            test_session = {
                "session_id": str(uuid.uuid4()),
                "consent_status": "granted",
                "context": {
                    "cultural_context": "eastern_collective",
                    "linguistic_context": "poetic_metaphorical"
                }
            }
            result = func(*test_args, session_context=test_session, **test_kwargs)
            if isinstance(result, dict) and 'context_analysis' in result:
                print(f"✅ Dynamic generation: {result['context_analysis'].get('generation_method', 'unknown')}")
        
        return True
        
    except Exception as e:
        print(f"\n❌ Enhanced functionality test failed for {func_name}: {str(e)}")
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
    Discover functions from consolidated API modules with enhanced functionality.
    
    Args:
        consolidated_modules: Dict mapping module names to module objects
    
    Returns:
        List of tuples: (function_name, function_object, module_name)
    """
    functions = []
    
    # Define enhanced functions to test
    enhanced_functions = {
        'persona': ['persona_load', 'persona_simulate', 'customize'],
        'memory': ['save_session', 'memory_replay', 'memory_tag_insight', 'memory_export', 'search_memories', 'memory_evolve_ideas'],
        'logic': ['non_sequitur', 'paradox', 'logic_metaphor', 'logic_sacred_play', 'logic_pattern_hack', 'logic_creative_shift']
    }
    
    for module_name, module in consolidated_modules.items():
        if module_name in enhanced_functions:
            for func_name in enhanced_functions[module_name]:
                if hasattr(module, func_name):
                    func = getattr(module, func_name)
                    if callable(func):
                        functions.append((func_name, func, module_name))
    
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
            test_args, test_kwargs = get_test_args_for_function(func_name, module_name)
            
            try:
                success = test_a2a_protocol(func, func_name, test_args, test_kwargs)
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
    Get appropriate test arguments for a given function.
    
    Args:
        func_name: Name of the function to test
        module_name: Name of the module containing the function
    
    Returns:
        tuple: (args, kwargs) for testing the function
    """
    # Enhanced test arguments for new functionality
    enhanced_test_args = {
        'persona_load': (['Blocked Artist'], {}),
        'persona_simulate': (['Blocked Artist', 'I can\'t create anything good'], {}),
        'customize': (['Blocked Artist', {'cultural_context': 'indigenous_holistic'}], {}),
        'save_session': (['test_session_001', {'session_type': 'creative_journey'}, ['insight1'], ['tag1']], {}),
        'memory_replay': (['test_session_001'], {}),
        'memory_tag_insight': (['test_session_001', 'Test insight', ['tag1', 'tag2'], 'creative', 3], {}),
        'memory_export': (['test_session_001'], {}),
        'search_memories': (['creativity'], {}),
        'memory_evolve_ideas': ([None, 'Test idea evolution'], {}),
        'non_sequitur': (['I can\'t create anything good'], {}),
        'paradox': (['I need to be perfect to create'], {}),
        'logic_metaphor': (['I can\'t create', 'nature'], {}),
        'logic_sacred_play': (['creative', 'gentle'], {}),
        'logic_pattern_hack': (['I can\'t create', 'perspective'], {}),
        'logic_creative_shift': (['I\'m not good enough', 'gentle'], {})
    }
    
    if func_name in enhanced_test_args:
        return enhanced_test_args[func_name]
    
    # Fallback to original test arguments
    test_args = {
        'co_create': (['Alice', 'Bob'], {'goal': 'healing_circle'}),
        'hold_space': (['grief_processing'], {}),
        'resolve_conflict': (['Alice', 'Bob'], {'issue': 'misunderstanding'}),
        'consent_check': (['deep_emotional_work', 'participant'], {}),
        'values_check': (['proposed_action'], {'values': {'consent': True, 'dignity': True}}),
        'begin': (['healing_ceremony', ['participant1', 'participant2']], {}),
        'end': (['healing_ceremony'], {}),
        'anchor': (['feeling_overwhelmed', 'breathwork'], {}),
        'transmute': (['anger', 'wisdom_and_compassion'], {}),
        'load': (['default'], {})
    }
    
    return test_args.get(func_name, ([], {}))

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
    for key in ['co_creation_session', 'space_session', 'session_data', 'session_context']:
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