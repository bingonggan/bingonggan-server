import os
import math
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from py3dbp import Packer, Bin, Item

load_dotenv()

class Req(BaseModel):
  items: list

class Res(BaseModel):
  box_size: list

app = FastAPI()

origins = [
    os.getenv("CLIENT_URL")
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/", response_model=Req)
async def root(req: Req):
  print(calculate_boxSize(req.items))
  return req


def get_box_and_item(items):
  packer = Packer()

  box = Bin(
    partno="box",
    WHD=calculate_boxSize(items)[1],
    max_weight=16,
  )

  packer.addBin(box)

  for item in get_items(items):
    packer.addItem(item)

  packer.pack(
    bigger_first=True,
    fix_point=True,
    distribute_items=False,
    check_stable=False,
    support_surface_ratio=0.5,
    number_of_decimals=0
  )

def calculate_boxSize(items):
  box_volume = 0

  for item in items:
    box_volume += item["itemX"] * item["itemY"] * item["itemZ"]

  box_len = math.ceil(box_volume**(1/3))

  if box_volume <= 3762000:
    return "1호", [220, 190, 90]
  elif box_volume <= 7290000:
    return "2호", [270, 180, 150]
  elif box_volume <= 875000:
    return "2-1호", [350, 250, 100]
  elif box_volume <= 17850000:
    return "3호", [340, 250, 210]
  elif box_volume <= 35588000:
    return "4호", [410, 310, 280]
  elif box_volume <= 38304000:
    return "5-1호", [480, 380, 210]
  elif box_volume <= 62016000:
    return "5호", [480, 380, 340]
  elif box_volume <= 99840000:
    return "6호", [520, 480, 400]
  else:
    return "커스텀 상자", [box_len, box_len, box_len]

def get_items(items):
  packer_items = []

  for i, item in enumerate(items):
    packer_item = Item(
      partno=i,
      name=item["itemTitle"],
      typeof="cube",
      WHD=(item["itemX"], item["itemY"], item["itemZ"]),
      weight=1,
      level=1,
      loadbear=1,
      updown=True,
      color="r",
    )

    packer_items.append(packer_item)

  return packer_items

