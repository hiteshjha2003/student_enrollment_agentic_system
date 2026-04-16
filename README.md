# Student Enrollment Assistant Agent - Production Ready

A full-stack agentic AI system for handling student enrollment inquiries. Built with **FastAPI** (Python backend), **React** (interactive frontend), and containerized with **Docker** for easy deployment. Supports **100+ real student data** in JSON format.

**Status**: ✅ Production Ready | 🐳 Fully Dockerized | 📊 100+ Student Records | ⚡ High Performance

---

## 🎯 Project Features

### Intelligent Agent System
- ✅ **Multi-turn conversations** - Maintains context across multiple user interactions
- ✅ **Agentic tools** - Calls specialized tools for program info, application status, and deadlines
- ✅ **Context memory** - Remembers applicant IDs and programs across sessions
- ✅ **Graceful escalation** - Directs users to counselors for out-of-scope questions

### Data Management
- ✅ **100+ Student records** - Comprehensive applicant database in JSON
- ✅ **5 Programs** - Computer Science, Business Admin, Mechanical Eng, Data Science, Civil Eng
- ✅ **Real-world statuses** - Accepted, Under Review, Documents Pending, Rejected
- ✅ **Detailed applicant info** - GPA, email, application date, next steps

### Modern Tech Stack
- ✅ **FastAPI** - High-performance async Python framework
- ✅ **React 18** - Modern frontend with hooks
- ✅ **Docker & Docker Compose** - Production-ready containerization
- ✅ **Neon UI Theme** - Bright, interactive, modern design
- ✅ **RESTful APIs** - Clean API contracts

### Available Tools:
1. **get_program_info** - Program details (duration, tuition, prerequisites)
2. **check_application_status** - Applicant status (name, program, status, next steps, GPA, email)
3. **get_deadlines** - Important dates for programs

---

## 📋 Prerequisites

### Option 1: Local Development
- **Python 3.8+** - [Download](https://www.python.org/)
- **Node.js 16+** - [Download](https://nodejs.org/)
- **npm** (comes with Node.js)

### Option 2: Docker (Recommended)
- **Docker** - [Download](https://docs.docker.com/get-docker/)
- **Docker Compose** - [Download](https://docs.docker.com/compose/install/)

Check installations:
```bash
python --version
node --version
npm --version
docker --version
docker-compose --version
```

---

## 🚀 Installation & Setup

### 🐳 Quick Start with Docker (Recommended) ⭐

#### 1. Navigate to Project
```bash
cd d:\edmo
```

#### 2. Start with Docker Compose
```bash
docker-compose up --build
```

This single command:
- Builds backend and frontend images
- Starts both services
- Configures networking
- Performs health checks

Expected output:
```
enrollment_assistant_backend  | INFO:     Uvicorn running on http://0.0.0.0:8000
enrollment_assistant_frontend | ⇨ listening on http://0.0.0.0:3000
```

#### 3. Open Browser
Navigate to `http://localhost:3000`

✅ **That's it! Application is ready to use.**

---

### Local Development Setup (Without Docker)

#### Step 1: Clone or Navigate to Project Directory

```bash
cd d:\edmo
```

### Step 2: Setup Backend (FastAPI)

#### 2.1 Create Python Virtual Environment

```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
# source venv/bin/activate
```

#### 2.2 Install Backend Dependencies

```bash
pip install -r requirements.txt
```

**Dependencies:**
- `fastapi` - Web framework for APIs
- `uvicorn` - ASGI server
- `pydantic` - Data validation
- `python-multipart` - Form parsing

#### 2.3 Verify Backend Setup

```bash
python main.py
```

You should see:
```
INFO:     Uvicorn running on http://127.0.0.1:8000
```

Press `Ctrl+C` to stop. Backend is ready!

---

### Step 3: Setup Frontend (React + Vite)

#### 3.1 Navigate to Frontend Directory

```bash
# From backend, go back to project root
cd ..
cd frontend
```

#### 3.2 Install Frontend Dependencies

```bash
npm install
```

This installs:
- `react` - UI library
- `react-dom` - React DOM rendering
- `axios` - HTTP client
- `vite` - Build tool
- `@vitejs/plugin-react` - React plugin for Vite

---

## ▶️ Running the Application

### Terminal 1: Start Backend Server

```bash
cd backend

# Activate virtual environment (if not already activated)
# Windows:
venv\Scripts\activate

# Start FastAPI server
python main.py
```

Expected output:
```
INFO:     Application startup complete
INFO:     Uvicorn running on http://127.0.0.1:8000
```

**Backend running at**: `http://localhost:8000`
**API Documentation**: `http://localhost:8000/docs` (Swagger UI)

### Terminal 2: Start Frontend Development Server

```bash
cd frontend

# Start Vite development server
npm run dev
```

Expected output:
```
  VITE v5.0.0  ready in 123 ms

  ➜  Local:   http://localhost:3000/
  ➜  press h + enter to show help
```

**Frontend running at**: `http://localhost:3000`

---

## 💬 Testing the Application

### Test Conversation (5 Turns)

Once both servers are running, open `http://localhost:3000` in your browser and test:


1. **"Hi, what programs do you offer in computer science?"**
   
   
2. **"What's the application deadline for that?"**
   
   
3. **"Can I get a fee waiver?**
   
   
4. **"What documents do I still need to submit?"**
   


## 🎨 UI Features

### Neon Bright Color Theme:
- **Neon Cyan** (#00f0ff) - Primary accent
- **Neon Pink** (#ff006e) - Secondary accent
- **Neon Green** (#39ff14) - Success states
- **Neon Purple** (#b300ff) - Interactive elements
- **Dark Background** - High contrast for readability

### Interactive Features:
✨ **Auto-scrolling** messages  
✨ **Real-time typing** indicators  
✨ **Tool badges** showing which tools were used  
✨ **Smooth animations** and transitions  
✨ **Responsive design** - Works on mobile and desktop  
✨ **User session management** - Maintains context across messages  

---

## 🔌 API Endpoints

### Main Chat Endpoint

**POST** `/api/chat`

Request:
```json
{
  "user_id": "USER-001",
  "message": "What programs do you offer?"
}
```

Response:
```json
{
  "agent_message": "Here's the information about Computer Science...",
  "tools_used": ["get_program_info"],
  "context_memory": {
    "applicant_id": null,
    "current_program": "Computer Science"
  }
}
```

### Other Available Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Welcome message |
| GET | `/api/health` | Health check |
| GET | `/api/available-programs` | List all programs |
| GET | `/api/session/{user_id}` | Get user session info |
| DELETE | `/api/session/{user_id}` | Clear user session |

---

## 📂 Project Structure

```
d:\edmo/
├── backend/
│   ├── main.py              # FastAPI application
│   ├── agents.py            # Agent logic & decision making
│   ├── tools.py             # Tool implementations with mock data
│   ├── models.py            # Pydantic data models
│   ├── requirements.txt      # Python dependencies
│   └── venv/                # Virtual environment (created after setup)
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   └── ChatMessage.jsx    # Message display component
│   │   ├── App.jsx          # Main React app component
│   │   ├── App.css          # Neon theme styling
│   │   └── main.jsx         # React entry point
│   ├── public/              # Static assets
│   ├── index.html           # HTML template
│   ├── vite.config.js       # Vite configuration
│   ├── package.json         # Node.js dependencies
│   └── node_modules/        # Installed packages (after npm install)
│
└── README.md                # This file
```

---

## 🔧 Backend Architecture

### Agent Loop Flow

```
User Input
    ↓
Extract Entities (program names, applicant IDs)
    ↓
Decide Tools to Call (based on user intent)
    ↓
Execute Tools (call specialized functions)
    ↓
Generate Response (format results naturally)
    ↓
Update Session Memory (remember context)
    ↓
Return to Frontend
```

### Key Components:

**StudentEnrollmentAgent** (`agents.py`)
- `get_or_create_session()` - Manages user context
- `extract_entities()` - Finds program names and applicant IDs
- `decide_tools_to_call()` - Determines which tools to use
- `execute_tools()` - Runs selected tools
- `generate_response()` - Creates natural language responses
- `process_message()` - Main agent loop orchestrator

**Tools** (`tools.py`)
- `get_program_info()` - Program details
- `check_application_status()` - Application status
- `get_deadlines()` - Important dates

---

## 🎓 How the Agent Works

### Context Memory

The agent remembers:
- **applicant_id**: Once provided, reused in subsequent messages
- **current_program**: Tracks which program user is asking about
- **conversation_history**: Stores all interactions in a session

Example:
```
Turn 1: "What about Computer Science?"
→ Agent remembers: current_program = "Computer Science"

Turn 2: "What's the deadline?"
→ Agent uses: current_program from memory (no need to specify again)
```

### Tool Decision Logic

The agent intelligently decides which tools to call:

| User Intent | Tools Called | Examples |
|------------|-------------|----------|
| Ask about programs | `get_program_info` | "Tell me about CS", "What programs?" |
| Ask about deadlines | `get_deadlines` | "When's the deadline?", "Application due date?" |
| Check status | `check_application_status` | "What's my status?", "Where's my app?" |
| Financial questions | None (escalate) | "Fee waiver?", "Scholarship?" |

### Escalation

For out-of-scope questions, the agent gracefully escalates:
```
Agent: "I'd recommend speaking with an enrollment counselor 
for that. Would you like me to connect you?"
```

---

## 🚨 Troubleshooting

### Docker Issues

**Container won't start**
```bash
# Check logs for errors
docker-compose logs -f backend
docker-compose logs -f frontend

# Rebuild without cache
docker-compose down
docker-compose build --no-cache
docker-compose up
```

**Port already in use**
```bash
# Check what's using the port
netstat -ano | findstr :8000    # Windows
lsof -i :8000                   # macOS/Linux

# Run on different ports
docker-compose -f docker-compose.yml -p enrollment2 up
```

**Health checks failing**
```bash
# Check backend health
docker exec enrollment_assistant_backend curl http://localhost:8000/api/health

# Check frontend health
docker exec enrollment_assistant_frontend wget -q -O- http://localhost:3000
```

**Network connectivity**
```bash
# Verify services can communicate
docker-compose ps    # Check status
docker network ls    # Check networks
docker network inspect enrollment_network  # Check connections
```

### Local Setup Issues

**Backend won't start**
```bash
# Problem: ModuleNotFoundError
# Solution: Ensure virtual environment is activated
venv\Scripts\activate

# Problem: Port 8000 already in use
# Solution: Kill process on port 8000 or use different port
uvicorn main:app --port 8001

# Problem: data.json not found
# Solution: Verify backend/data.json exists with 102 applicant records
```

**Frontend won't start**
```bash
# Problem: npm command not found
# Solution: Install Node.js from https://nodejs.org/

# Problem: Port 3000 already in use
# Solution: Kill process or specify different port in vite.config.js

# Problem: CORS errors
# Solution: Backend CORS is already configured, ensure backend is running
```

**API calls failing**
```bash
# Check backend is running
curl http://localhost:8000/api/health

# Check available programs
curl http://localhost:8000/api/available-programs

# Check statistics (should show 102 applicants)
curl http://localhost:8000/api/statistics
```

**Data not loading**
```bash
# Verify data.json exists and is valid JSON
cat backend/data.json | python -m json.tool

# Check if tools can access data
curl http://localhost:8000/api/statistics

# Should return: total_applicants: 102, total_programs: 5
```

### Common Messages

**"Cannot find applicant APP-XXXX"**
- Solution: Use applicants from APP-1001 to APP-1102
- Test with: APP-1001, APP-1042, APP-1089

**"Program not found"**
- Solution: Use exact program names:
  - Computer Science
  - Business Administration
  - Mechanical Engineering
  - Data Science
  - Civil Engineering

---

## 📊 Data Reference (100+ Students)

### Available Programs (5 total):

| Program | Duration | Tuition | Seats | Prerequisites |
|---------|----------|---------|-------|---|
| Computer Science | 4 years | $45,000 | 150 | Math 101, Physics 101, English 101 |
| Business Administration | 4 years | $40,000 | 200 | Economics 101, Business 101 |
| Mechanical Engineering | 4 years | $50,000 | 100 | Calculus I, Physics I, Chemistry I |
| Data Science | 4 years | $48,000 | 120 | Statistics 101, Python Programming, Math 201 |
| Civil Engineering | 4 years | $46,000 | 110 | Calculus II, Physics II, Materials Science |

### Applicant Dataset (102 total):

**Status Distribution**:
- ✅ Accepted: ~40 applicants (39%)
- 🔄 Under Review: ~35 applicants (34%)
- 📋 Documents Pending: ~15 applicants (15%)
- ❌ Rejected: ~12 applicants (12%)

**Sample Test Applicants** (from data.json):

| ID | Name | Program | Status | GPA |
|----|------|---------|--------|-----|
| APP-1001 | John Smith | Computer Science | Under Review | 3.8 |
| APP-1002 | Sarah Johnson | Business Administration | Accepted | 3.9 |
| APP-1003 | Michael Chen | Mechanical Engineering | Documents Pending | 3.7 |
| APP-1042 | (Full dataset) | Computer Science | Under Review | 3.8 |
| APP-1089 | (Full dataset) | Business Administration | Accepted | 3.9 |
| APP-1102 | Frances Wood | Mechanical Engineering | Documents Pending | 3.75 |

**Note**: Complete dataset of 102 applicants (APP-1001 to APP-1102) is stored in `backend/data.json`

---

## 🐳 Docker Commands

### Build and Run
```bash
# Build images
docker-compose build

# Start services
docker-compose up

# Start in background
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down

# Remove everything (including volumes)
docker-compose down -v
```

### Health Checks
```bash
# Check backend health
curl http://localhost:8000/api/health

# Check frontend health
curl http://localhost:3000

# Get system statistics (all 100+ students)
curl http://localhost:8000/api/statistics

# List all programs
curl http://localhost:8000/api/available-programs
```

### Individual Docker Commands
```bash
# Build backend only
docker build -f Dockerfile.backend -t enrollment-backend .

# Build frontend only
docker build -f Dockerfile.frontend -t enrollment-frontend .

# Run backend container
docker run -p 8000:8000 enrollment-backend

# Run frontend container
docker run -p 3000:3000 enrollment-frontend
```

---

## 🌟 Advanced Usage

### Starting Fresh Session

To clear history and start a new conversation:
1. Click "Change User" button in the UI
2. Enter a new user ID
3. Chat history will be cleared

### API Testing with cURL

```bash
# Test the chat API
curl -X POST http://localhost:8000/api/chat \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": "TEST-001",
    "message": "What programs do you offer?"
  }'

# Check session info
curl http://localhost:8000/api/session/TEST-001

# Get available programs
curl http://localhost:8000/api/available-programs
```

### Building for Production

```bash
# Build frontend
cd frontend
npm run build

# Output in: frontend/dist/

# Backend: Use production ASGI server like Gunicorn
pip install gunicorn
gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app
```

---

## 📝 Development Notes

### Extending the Agent

To add new tools:

1. **Add tool function** in `tools.py`:
```python
def new_tool_name(param: str) -> dict:
    return {"success": True, "data": {...}}
```

2. **Register tool** in `TOOLS` dict:
```python
TOOLS = {
    "new_tool_name": new_tool_name,
    ...
}
```

3. **Add decision logic** in `agents.py`:
```python
if "keyword" in message_lower:
    tools_to_call.append(("new_tool_name", {"param": value}))
```

4. **Add response formatting** in `generate_response()`:
```python
elif tool_name == "new_tool_name":
    response_parts.append(f"Formatted response: {data}")
```

---

## 🎯 Requirements Compliance

✅ **Agentic AI Architecture** - StudentEnrollmentAgent with multi-turn conversation loop  
✅ **Three Core Tools** - Program Info, Application Status, Deadlines (with 100+ student data)  
✅ **Multi-turn Support** - Session memory maintains applicant_id and conversation context  
✅ **Entity Extraction** - Automatically identifies applicant IDs and program names  
✅ **Smart Tool Selection** - Agent decides which tools to call based on user intent  
✅ **100+ Student Data** - 102 applicants in JSON format (APP-1001 to APP-1102)  
✅ **5 Programs** - Computer Science, Business, Mechanical, Data Science, Civil Engineering  
✅ **FastAPI Backend** - RESTful API with CORS, health checks, statistics endpoint  
✅ **React 18 Frontend** - Interactive UI with Vite, Axios, neon theme  
✅ **Connected APIs** - Frontend communicates with backend via REST  
✅ **Neon UI Theme** - Cyan, Pink, Green, Purple color scheme  
✅ **Docker Containerization** - Multi-stage Dockerfiles with health checks  
✅ **Docker Compose** - Complete orchestration for backend + frontend  
✅ **Comprehensive README** - Setup, Docker commands, data reference, API docs  
✅ **Production Ready** - Error handling, validation, logging, non-root containers  

---

## 📞 Support & Questions

For issues or questions:

1. Check the **Troubleshooting** section above
2. Review **API Endpoints** documentation
3. Check browser console (F12) for errors
4. Verify both servers are running:
   - Backend: `http://localhost:8000/api/health`
   - Frontend: `http://localhost:3000`
5. For Docker issues, run: `docker-compose logs -f`

---



---

**Built by Hitesh Jha with ❤️ using FastAPI, React, and Python**

Happy Enrolling! 🎓
