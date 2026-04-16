"""
Agent Logic for Student Enrollment Assistant
Implements the agent loop with multi-turn conversation support
"""

import json
import re
from typing import List, Dict, Tuple
from tools import execute_tool, PROGRAMS_DB, APPLICANTS_DB

class StudentEnrollmentAgent:
    """
    Agentic AI system for handling student enrollment queries
    """
    
    def __init__(self):
        self.session_memory = {}  # Stores context per user session
        self.tool_definitions = {
            "get_program_info": {
                "description": "Get information about a specific program including name, duration, tuition, and prerequisites",
                "parameters": ["program_name"]
            },
            "check_application_status": {
                "description": "Check the application status for a specific applicant using their applicant ID",
                "parameters": ["applicant_id"]
            },
            "get_deadlines": {
                "description": "Get important deadlines for a program including application deadline, document submission deadline, and decision notification date",
                "parameters": ["program_name"]
            }
        }
    
    def get_or_create_session(self, user_id: str) -> dict:
        """Create or retrieve a user session"""
        if user_id not in self.session_memory:
            self.session_memory[user_id] = {
                "applicant_id": None,
                "current_program": None,
                "conversation_history": []
            }
        return self.session_memory[user_id]
    
    def extract_entities(self, user_message: str) -> Dict[str, str]:
        """Extract entities like program names and applicant IDs from user message"""
        entities = {}
        
        # Extract applicant ID (format: APP-XXXX)
        applicant_id_match = re.search(r'APP-\d{4}', user_message)
        if applicant_id_match:
            entities['applicant_id'] = applicant_id_match.group()
        
        # Extract program names (case-insensitive)
        for program_name in PROGRAMS_DB.keys():
            if program_name.lower() in user_message.lower():
                entities['program_name'] = program_name
                break
        
        return entities
    
    def decide_tools_to_call(self, user_message: str, session_context: dict) -> List[Tuple[str, Dict]]:
        """
        Decide which tools to call based on the user message and context
        Returns a list of tuples: (tool_name, tool_arguments)
        """
        tools_to_call = []
        message_lower = user_message.lower()
        
        # Extract entities from message
        entities = self.extract_entities(user_message)
        
        # Logic to determine which tools to call
        if any(keyword in message_lower for keyword in ["program", "offer", "course", "study"]):
            # Query: Get program information
            if "program" in message_lower or "computer science" in message_lower:
                # Try to find program name
                for prog_name in PROGRAMS_DB.keys():
                    if prog_name.lower() in message_lower:
                        tools_to_call.append(("get_program_info", {"program_name": prog_name}))
                        session_context['current_program'] = prog_name
                        break
                else:
                    # If no specific program found, check if user mentioned CS or similar
                    if "computer science" in message_lower or "cs" in message_lower:
                        tools_to_call.append(("get_program_info", {"program_name": "Computer Science"}))
                        session_context['current_program'] = "Computer Science"
        
        if any(keyword in message_lower for keyword in ["deadline", "when", "due date", "submit"]):
            # Query: Get deadlines
            if entities.get('program_name'):
                tools_to_call.append(("get_deadlines", {"program_name": entities['program_name']}))
            elif session_context.get('current_program'):
                tools_to_call.append(("get_deadlines", {"program_name": session_context['current_program']}))
        
        if any(keyword in message_lower for keyword in ["status", "application", "applied", "check"]):
            # Query: Check application status
            if entities.get('applicant_id'):
                tools_to_call.append(("check_application_status", {"applicant_id": entities['applicant_id']}))
                session_context['applicant_id'] = entities['applicant_id']
            elif session_context.get('applicant_id'):
                tools_to_call.append(("check_application_status", {"applicant_id": session_context['applicant_id']}))
        
        if any(keyword in message_lower for keyword in ["documents", "submit", "required", "need"]):
            # This might need application status to provide document requirements
            if entities.get('applicant_id'):
                tools_to_call.append(("check_application_status", {"applicant_id": entities['applicant_id']}))
                session_context['applicant_id'] = entities['applicant_id']
            elif session_context.get('applicant_id'):
                tools_to_call.append(("check_application_status", {"applicant_id": session_context['applicant_id']}))
        
        return tools_to_call
    
    def execute_tools(self, tools_to_call: List[Tuple[str, Dict]]) -> Dict[str, dict]:
        """Execute the decided tools and collect results"""
        tool_results = {}
        
        for tool_name, tool_args in tools_to_call:
            result = execute_tool(tool_name, **tool_args)
            tool_results[tool_name] = result
        
        return tool_results
    
    def generate_response(self, user_message: str, tool_results: Dict[str, dict], session_context: dict) -> str:
        """
        Generate a natural language response based on tool results
        """
        # If no tools were called, try to formulate a generic response
        if not tool_results:
            # Check if this is a question we can't answer
            if any(keyword in user_message.lower() for keyword in ["fee waiver", "financial aid", "scholarship", "discount"]):
                return "I'd recommend speaking with an enrollment counselor for financial aid options like fee waivers and scholarships. Would you like me to connect you with someone from our financial aid office?"
            
            if any(keyword in user_message.lower() for keyword in ["other question", "anything else", "help"]):
                return "I'm here to help! I can answer questions about programs, application deadlines, and check your application status. What would you like to know?"
            
            return "I'm not sure how to answer that question. I can help you with information about programs, deadlines, and your application status. Could you rephrase your question?"
        
        # Build response from tool results
        response_parts = []
        
        for tool_name, result in tool_results.items():
            if not result.get('success'):
                response_parts.append(result.get('error', 'An error occurred'))
                continue
            
            data = result.get('data', {})
            
            if tool_name == "get_program_info":
                program = data
                response_parts.append(
                    f"Here's the information about {program['program_name']}:\n"
                    f"• Duration: {program['duration']}\n"
                    f"• Tuition: ${program['tuition']:,} per year\n"
                    f"• Prerequisites: {', '.join(program['prerequisites'])}"
                )
            
            elif tool_name == "get_deadlines":
                deadlines = data
                response_parts.append(
                    f"Important deadlines for {session_context.get('current_program', 'the program')}:\n"
                    f"• Application Deadline: {deadlines['application_deadline']}\n"
                    f"• Document Submission Deadline: {deadlines['document_submission_deadline']}\n"
                    f"• Decision Notification Date: {deadlines['decision_notification_date']}"
                )
            
            elif tool_name == "check_application_status":
                app = data
                response_parts.append(
                    f"Your application status:\n"
                    f"• Name: {app['applicant_name']}\n"
                    f"• Program Applied To: {app['program_applied_to']}\n"
                    f"• Current Status: {app['status']}\n"
                    f"• Next Step: {app['next_step']}"
                )
        
        if response_parts:
            return "\n\n".join(response_parts)
        
        return "I wasn't able to find the information you're looking for. Could you provide more details?"
    
    def process_message(self, user_id: str, user_message: str) -> Dict:
        """
        Main agent loop: Receive message, decide tools, execute, and generate response
        """
        # Get or create session
        session = self.get_or_create_session(user_id)
        
        # Decide which tools to call
        tools_to_call = self.decide_tools_to_call(user_message, session)
        
        # Execute tools
        tool_results = self.execute_tools(tools_to_call)
        
        # Generate response
        agent_response = self.generate_response(user_message, tool_results, session)
        
        # Update conversation history
        session['conversation_history'].append({
            "user_message": user_message,
            "agent_response": agent_response,
            "tools_used": [t[0] for t in tools_to_call]
        })
        
        return {
            "agent_message": agent_response,
            "tools_used": [t[0] for t in tools_to_call],
            "context_memory": {
                "applicant_id": session['applicant_id'],
                "current_program": session['current_program']
            }
        }


# Global agent instance
agent = StudentEnrollmentAgent()
