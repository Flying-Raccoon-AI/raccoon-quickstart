import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from tasks import schedule_order


class ScheduleOrderSchema(BaseModel):
    item_url: str
    additional_info: str
    name: str
    phone: str
    address: dict
    order_time: str


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def hello():
    return "Welcome to Ride Hailing API"


@app.post("/schedule")
def schedule(body: ScheduleOrderSchema):
    result = schedule_order(body.item_url, body.additional_info, body.name, body.phone, body.address, body.order_time)
    return result


if __name__ == '__main__':
    uvicorn.run(app, port=5001, host="0.0.0.0")
