from pydantic import BaseModel
from typing import Optional, List

# Request/Response Models
class MessageRequest(BaseModel):
    user_id: str
    message: str

class MessageResponse(BaseModel):
    agent_message: str
    tools_used: List[str]
    context_memory: dict

class ToolResponse(BaseModel):
    tool_name: str
    result: dict

class ProgramInfo(BaseModel):
    program_name: str
    duration: str
    tuition: float
    prerequisites: List[str]

class ApplicationStatus(BaseModel):
    applicant_name: str
    program_applied_to: str
    status: str
    next_step: str

class Deadlines(BaseModel):
    application_deadline: str
    document_submission_deadline: str
    decision_notification_date: str
