# 🚀 Student Enrollment Assistant - Quick Start Guide

## ⚡ Fastest Way to Run (Docker - 2 seconds to startup)

```bash
cd d:\edmo
docker-compose up --build
```

Then open: **http://localhost:3000**

✅ That's it! Application is running with 102 students.

---

## 📋 What's Included

✅ **102 Student Records** - Complete applicant database  
✅ **5 Programs** - Computer Science, Business, Engineering, Data Science, Civil Engineering  
✅ **AI Agent** - Conversational enrollment assistant  
✅ **3 Core Tools** - Program info, application status, deadlines  
✅ **Neon UI** - Modern, interactive interface  
✅ **Production Ready** - Error handling, validation, logging  

---

## 🔧 Local Development (Without Docker)

### Backend Setup
```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python main.py
```
Backend runs at: **http://localhost:8000**

### Frontend Setup (New Terminal)
```bash
cd frontend
npm install
npm run dev
```
Frontend runs at: **http://localhost:3000**

---

## 📊 Test Data

**Applicant IDs**: APP-1001 to APP-1102  
**Programs**: Computer Science, Business Administration, Mechanical Engineering, Data Science, Civil Engineering

**Try these applicants**:
- APP-1001 (Under Review, GPA 3.8)
- APP-1042 (Under Review, GPA 3.8)
- APP-1089 (Accepted, GPA 3.9)

---

## 🎯 Test Conversation

1. **"Hi, what programs do you offer in computer science?"**
   
   
2. **"What's the application deadline for that?"**
   
   
3. **"Can I get a fee waiver?**
   
   
4. **"What documents do I still need to submit?"**
   

---

## ✨ Key Features

- **Multi-turn conversation** - Agent remembers context
- **100+ student database** - Complete applicant management
- **Smart tool selection** - Agent decides which tools to use
- **Session memory** - Maintains user context
- **Neon UI theme** - Cyan, Pink, Green, Purple colors
- **Production ready** - Docker containerization included

---

## 📖 Full Documentation

For detailed setup, troubleshooting, and API reference:
→ See **README.md**

For implementation architecture details:
→ See **IMPLEMENTATION_GUIDE.md**

---

## 🆘 Troubleshooting

**Docker issues?**
```bash
docker-compose logs -f
```

**Port already in use?**
```bash
docker-compose down
docker-compose up --build
```

**Backend not responding?**
```bash
curl http://localhost:8000/api/health
```

**Check application data loaded?**
```bash
curl http://localhost:8000/api/statistics
# Should show: 102 applicants, 5 programs
```

---

## 📞 Support

1. Check **README.md** troubleshooting section
2. Review browser console (F12) for errors
3. Check Docker logs: `docker-compose logs -f`

---

**Ready to run?** 👉 `docker-compose up --build` 👈
