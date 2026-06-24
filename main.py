
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import time
from pydantic import BaseModel

app = FastAPI()

faq = {
    "return policy": "You can return products within 30 days of delivery.",
    "refund": "Refunds are processed within 5-7 business days.",
    "shipping": "Standard shipping takes 3-5 business days.",
    "payment": "We accept UPI, Credit Cards, Debit Cards, and Net Banking."
}

def customer_support_agent(user_message):
    msg = user_message.lower()

    if "return" in msg:
        return faq["return policy"]

    elif "refund" in msg:
        return faq["refund"]

    elif "shipping" in msg or "delivery" in msg:
        return faq["shipping"]

    elif "payment" in msg:
        return faq["payment"]

    elif "order" in msg and "track" in msg:
        return "Please provide your Order ID to track your order."

    else:
        return "I'm sorry, I couldn't understand your request."

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def home():
    return {"message": "Customer Support Agent Running"}

@app.post("/chat")
def chat(request: ChatRequest):
    response = customer_support_agent(request.message)
    return {"response": response}


@app.get("/stream")
def stream_response():

    def generate():
        text = "Hello! How can I help you today?"
        for word in text.split():
            yield word + " "
            time.sleep(0.2)

    return StreamingResponse(generate(), media_type="text/plain")
