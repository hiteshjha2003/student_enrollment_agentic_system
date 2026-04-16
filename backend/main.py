"""
FastAPI backend for Student Enrollment Assistant Agent
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
from agents import agent

# Define request/response models
class MessageRequest(BaseModel):
    user_id: str
    message: str

class MessageResponse(BaseModel):
    agent_message: str
    tools_used: List[str]
    context_memory: dict

# Initialize FastAPI app
app = FastAPI(
    title="Student Enrollment Assistant Agent",
    description="An agentic AI system for handling student enrollment queries",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173", "*"],  # Allow React dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API Endpoints

@app.get("/")
async def root():
    """Welcome endpoint"""
    return {
        "message": "Student Enrollment Assistant Agent API",
        "endpoints": {
            "chat": "/api/chat",
            "health": "/api/health"
        }
    }

@app.get("/api/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "service": "Student Enrollment Assistant Agent"
    }

@app.post("/api/chat", response_model=MessageResponse)
async def chat(request: MessageRequest):
    """
    Main chat endpoint for processing user messages through the agent
    
    Args:
        request: MessageRequest with user_id and message
        
    Returns:
        MessageResponse with agent message, tools used, and context memory
    """
    try:
        # Validate input
        if not request.user_id or not request.message:
            raise HTTPException(status_code=400, detail="user_id and message are required")
        
        if len(request.message.strip()) == 0:
            raise HTTPException(status_code=400, detail="Message cannot be empty")
        
        # Process message through agent
        result = agent.process_message(request.user_id, request.message)
        
        return MessageResponse(
            agent_message=result['agent_message'],
            tools_used=result['tools_used'],
            context_memory=result['context_memory']
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/available-programs")
async def get_available_programs():
    """Get list of all available programs"""
    from tools import PROGRAMS_DB
    return {
        "programs": list(PROGRAMS_DB.keys())
    }

@app.get("/api/session/{user_id}")
async def get_session_info(user_id: str):
    """Get session context for a user"""
    if user_id not in agent.session_memory:
        raise HTTPException(status_code=404, detail="Session not found")
    
    session = agent.session_memory[user_id]
    return {
        "user_id": user_id,
        "applicant_id": session['applicant_id'],
        "current_program": session['current_program'],
        "conversation_history_count": len(session['conversation_history'])
    }

@app.delete("/api/session/{user_id}")
async def clear_session(user_id: str):
    """Clear session for a user"""
    if user_id in agent.session_memory:
        del agent.session_memory[user_id]
        return {"message": f"Session for {user_id} cleared"}
    return {"message": "Session not found"}

@app.get("/api/statistics")
async def get_statistics():
    """Get overall statistics about programs and applicants"""
    from tools import get_program_statistics
    return get_program_statistics()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
