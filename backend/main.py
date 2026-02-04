"""
Smart Billing System - Main Backend
Simple FastAPI application for AI-Agentathon hackathon
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.billing import router as billing_router

# Create FastAPI app
app = FastAPI(title="Smart Billing System")

# Enable CORS so frontend can talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for local development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include billing routes
app.include_router(billing_router, prefix="/api")

@app.get("/")
def root():
    """Simple health check"""
    return {"message": "Smart Billing System API is running"}

if __name__ == "__main__":
    import uvicorn
    print("Starting Smart Billing System...")
    print("Backend running at: http://localhost:8000")
    uvicorn.run(app, host="0.0.0.0", port=8000)
