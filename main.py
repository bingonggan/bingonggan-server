import os
import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from packing import get_packed_item_list
from typing import List, Tuple

load_dotenv()


class ReqItem(BaseModel):
    itemName: str
    itemIndex: int
    itemScaleX: float
    itemScaleY: float
    itemScaleZ: float
    itemW: float
    itemH: float
    itemD: float
    loadBear: int


class Req(BaseModel):
    items: List[ReqItem]


class ResItem(BaseModel):
    itemName: str
    itemIndex: int
    itemScale: List[float]
    position: List[float]
    rotationType: int


class result(BaseModel):
    boxSize: Tuple[str, Tuple[int, int, int]]
    itemList: List[ResItem]


class Res(BaseModel):
    result: List[result]


app = FastAPI()

origins = [os.getenv("CLIENT_URL")]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "success"}


@app.post("/packing", response_model=Res)
async def packing(req: Req):
    if len(req.items) == 0:
        raise HTTPException(status_code=400, detail="아이템이 없습니다.")
    if len(req.items) > 15:
        raise HTTPException(
            status_code=400, detail="아이템 개수는 15개를 넘을 수 없습니다"
        )

    response = get_packed_item_list(req.items)
    return {"result": response}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
