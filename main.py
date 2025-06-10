from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import pickle
import pandas as pd

# Load model and encoders
model = pickle.load(open("rfc_model.pkl", "rb"))
encoders = pickle.load(open("encoders.pkl", "rb"))

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/predict", response_class=HTMLResponse)
async def predict(
    request: Request,
    network_packet_size: int = Form(...),
    protocol_type: str = Form(...),
    login_attempts: int = Form(...),
    session_duration: float = Form(...),
    encryption_used: str = Form(...),
    ip_reputation_score: float = Form(...),
    failed_logins: int = Form(...),
    browser_type: str = Form(...),
    unusual_time_access: int = Form(...)
):
    input_data = {
        "network_packet_size": [network_packet_size],
        "protocol_type": [protocol_type],
        "login_attempts": [login_attempts],
        "session_duration": [session_duration],
        "encryption_used": [encryption_used],
        "ip_reputation_score": [ip_reputation_score],
        "failed_logins": [failed_logins],
        "browser_type": [browser_type],
        "unusual_time_access": [unusual_time_access],
    }
    df = pd.DataFrame(input_data)

    for col, le in encoders.items():
        df[col] = df[col].map(lambda x: le.transform([x])[0] if x in le.classes_ else -1)

    prediction = model.predict(df)[0]
    result = "🚨 Malicious Activity Detected!" if prediction == 1 else "✅ Normal Session"
    return templates.TemplateResponse("index.html", {"request": request, "result": result})
