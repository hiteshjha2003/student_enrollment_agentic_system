"""
Tool implementations for the Student Enrollment Assistant Agent
Loads data from data.json file
"""

import json
import os
from pathlib import Path

# Get the path to data.json
DATA_FILE = Path(__file__).parent / "data.json"

def load_data():
    """Load data from data.json file"""
    try:
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading data.json: {e}")
        return {"programs": [], "applicants": []}

# Load data on startup
_DATA = load_data()
PROGRAMS_DB = {prog['program_name']: prog for prog in _DATA.get('programs', [])}
APPLICANTS_DB = {app['app_id']: app for app in _DATA.get('applicants', [])}

# For backwards compatibility
DEADLINES_DB = {
    prog['program_name']: {
        "application_deadline": prog.get('application_deadline', ''),
        "document_submission_deadline": prog.get('document_submission_deadline', ''),
        "decision_notification_date": prog.get('decision_notification_date', '')
    }
    for prog in _DATA.get('programs', [])
}


def get_program_info(program_name: str) -> dict:
    """
    Retrieves program information from the data
    
    Args:
        program_name: Name of the program
        
    Returns:
        Dictionary with program details or error message
    """
    # Try exact match first
    if program_name in PROGRAMS_DB:
        prog = PROGRAMS_DB[program_name]
        return {
            "success": True,
            "data": {
                "program_name": prog.get('program_name'),
                "duration": prog.get('duration'),
                "tuition": prog.get('tuition'),
                "prerequisites": prog.get('prerequisites', [])
            }
        }
    
    # Try case-insensitive match
    for key in PROGRAMS_DB:
        if key.lower() == program_name.lower():
            prog = PROGRAMS_DB[key]
            return {
                "success": True,
                "data": {
                    "program_name": prog.get('program_name'),
                    "duration": prog.get('duration'),
                    "tuition": prog.get('tuition'),
                    "prerequisites": prog.get('prerequisites', [])
                }
            }
    
    available_programs = ', '.join(PROGRAMS_DB.keys())
    return {
        "success": False,
        "error": f"Program '{program_name}' not found. Available programs: {available_programs}"
    }


def check_application_status(applicant_id: str) -> dict:
    """
    Checks the application status for an applicant
    
    Args:
        applicant_id: Applicant ID (e.g., APP-1042)
        
    Returns:
        Dictionary with application status or error message
    """
    if applicant_id in APPLICANTS_DB:
        app = APPLICANTS_DB[applicant_id]
        return {
            "success": True,
            "data": {
                "applicant_name": app.get('name'),
                "program_applied_to": app.get('program_applied_to'),
                "status": app.get('status'),
                "next_step": app.get('next_step'),
                "gpa": app.get('gpa'),
                "email": app.get('email'),
                "application_date": app.get('application_date')
            }
        }
    
    # Try case-insensitive match
    for key in APPLICANTS_DB:
        if key.upper() == applicant_id.upper():
            app = APPLICANTS_DB[key]
            return {
                "success": True,
                "data": {
                    "applicant_name": app.get('name'),
                    "program_applied_to": app.get('program_applied_to'),
                    "status": app.get('status'),
                    "next_step": app.get('next_step'),
                    "gpa": app.get('gpa'),
                    "email": app.get('email'),
                    "application_date": app.get('application_date')
                }
            }
    
    return {
        "success": False,
        "error": f"Applicant ID '{applicant_id}' not found. Total applicants in system: {len(APPLICANTS_DB)}"
    }


def get_deadlines(program_name: str) -> dict:
    """
    Retrieves deadlines for a specific program
    
    Args:
        program_name: Name of the program
        
    Returns:
        Dictionary with deadline information or error message
    """
    # Try exact match first
    if program_name in PROGRAMS_DB:
        prog = PROGRAMS_DB[program_name]
        return {
            "success": True,
            "data": {
                "application_deadline": prog.get('application_deadline'),
                "document_submission_deadline": prog.get('document_submission_deadline'),
                "decision_notification_date": prog.get('decision_notification_date')
            }
        }
    
    # Try case-insensitive match
    for key in PROGRAMS_DB:
        if key.lower() == program_name.lower():
            prog = PROGRAMS_DB[key]
            return {
                "success": True,
                "data": {
                    "application_deadline": prog.get('application_deadline'),
                    "document_submission_deadline": prog.get('document_submission_deadline'),
                    "decision_notification_date": prog.get('decision_notification_date')
                }
            }
    
    available_programs = ', '.join(PROGRAMS_DB.keys())
    return {
        "success": False,
        "error": f"Deadlines for '{program_name}' not found. Available programs: {available_programs}"
    }


def get_program_statistics() -> dict:
    """Get overall statistics about programs and applicants"""
    total_applicants = len(APPLICANTS_DB)
    total_programs = len(PROGRAMS_DB)
    
    status_breakdown = {}
    for app in APPLICANTS_DB.values():
        status = app.get('status', 'Unknown')
        status_breakdown[status] = status_breakdown.get(status, 0) + 1
    
    return {
        "success": True,
        "data": {
            "total_applicants": total_applicants,
            "total_programs": total_programs,
            "status_breakdown": status_breakdown,
            "programs_list": list(PROGRAMS_DB.keys())
        }
    }


# Tool registry
TOOLS = {
    "get_program_info": get_program_info,
    "check_application_status": check_application_status,
    "get_deadlines": get_deadlines
}


def execute_tool(tool_name: str, **kwargs) -> dict:
    """
    Execute a tool by name
    
    Args:
        tool_name: Name of the tool to execute
        **kwargs: Arguments to pass to the tool
        
    Returns:
        Tool execution result
    """
    if tool_name not in TOOLS:
        return {
            "success": False,
            "error": f"Tool '{tool_name}' not found"
        }
    
    try:
        result = TOOLS[tool_name](**kwargs)
        return result
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }
