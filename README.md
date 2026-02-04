# Smart Billing System - AI-Agentathon Project

## Overview
A simple agentic AI-enabled billing system for retail that demonstrates autonomous agent decision-making.

## Features
- **Generate bills** with random items and totals
- **3 AI Agents** that make autonomous decisions:
  1. **Print Decision Agent** - Decides whether to print receipt
  2. **Network Status Agent** - Checks if system is online/offline
  3. **Error Detection Agent** - Detects duplicate bills

## Project Structure
```
AIAG03-SmartBilling/
├── backend/
│   ├── main.py                 # FastAPI server
│   ├── routes/
│   │   └── billing.py          # Bill generation endpoint
│   ├── agents/
│   │   ├── agent_manager.py    # Coordinates all agents
│   │   ├── print_agent.py      # Print decision logic
│   │   ├── offline_agent.py    # Network status logic
│   │   └── error_agent.py      # Error detection logic
│   └── requirements.txt        # Python dependencies
└── frontend/
    ├── index.html              # Simple UI
    ├── script.js               # Frontend logic
    └── style.css               # Styling
```

## How to Run

### Step 1: Install Dependencies
```bash
cd backend
pip install -r requirements.txt
```

### Step 2: Start Backend
```bash
python main.py
```
The backend will run on `http://localhost:8000`

### Step 3: Open Frontend
Open `frontend/index.html` in your web browser (just double-click the file)

## How to Use
1. Click the **"Generate Bill"** button
2. The system will:
   - Generate a random bill with items
   - Send it to all 3 AI agents
   - Display their autonomous decisions
3. You'll see:
   - Bill ID and total amount
   - Whether to print (Print Agent decision)
   - Online/Offline status (Network Agent decision)
   - Any errors detected (Error Agent decision)

## How the AI Agents Work

### Print Decision Agent
- **Rule 1**: If bill > ₹100 → Always print (high-value)
- **Rule 2**: Otherwise → 60% chance to print (simulates printer availability)

### Network Status Agent
- **Simulation**: 80% chance online, 20% chance offline
- **Online**: Enables cloud sync, email receipts, online payments
- **Offline**: Only local storage and printing available

### Error Detection Agent
- **Checks**: Compares new bill with last 5 bills
- **Detects**: Duplicate bills (same total + same item count)
- **Reports**: Error if duplicate found

## Key Points for Judges
1. **Agentic Design**: Each agent makes independent decisions
2. **Rule-Based AI**: Simple, explainable logic (not black-box ML)
3. **Autonomous**: Agents decide on their own, frontend just displays
4. **Scalable**: Easy to add more agents (inventory check, fraud detection, etc.)
5. **Production-Ready Concept**: Could be deployed with real printer/network APIs

## Tech Stack
- **Backend**: Python + FastAPI
- **Frontend**: HTML + CSS + Vanilla JavaScript
- **Storage**: In-memory (list)
- **AI**: Rule-based agents

## Future Enhancements
- Add more agents (inventory, loyalty points, fraud detection)
- Connect to real printer API
- Use actual network status check
- Add database (SQLite/PostgreSQL)
- Add user authentication

## Troubleshooting

**Backend won't start?**
- Make sure Python 3.7+ is installed
- Install dependencies: `pip install -r requirements.txt`

**Frontend can't connect?**
- Make sure backend is running on port 8000
- Check browser console for errors (F12)

**CORS errors?**
- Backend has CORS enabled for all origins
- Try running from the same folder

## Team
AI-Agentathon 2024 - Student Project

## License
MIT License - Educational purposes
```

---

## 📋 Folder Structure to Create
```
AIAG03-SmartBilling/
├── backend/
│   ├── agents/
│   │   ├── __init__.py (empty file)
│   │   ├── agent_manager.py
│   │   ├── print_agent.py
│   │   ├── offline_agent.py
│   │   └── error_agent.py
│   ├── routes/
│   │   ├── __init__.py (empty file)
│   │   └── billing.py
│   ├── main.py
│   └── requirements.txt
├── frontend/
│   ├── index.html
│   ├── script.js
│   └── style.css
└── README.md
