from fastapi.testclient import TestClient
import mock_data
from main import app


client = TestClient(app)


def test_root():
    res = client.get("/")
    assert res.status_code == 200
    assert res.json() == {"message": "success"}


def test_packing():
    normal_res = client.post("/packing", json=mock_data.normal_items)
    assert normal_res.status_code == 200
    assert normal_res.json() == mock_data.normal_items_res

    empty_res = client.post("/packing", json=mock_data.empty_items)
    assert empty_res.status_code == 400
    assert empty_res.json() == {"detail": "아이템이 없습니다."}

    long_res = client.post("/packing", json=mock_data.long_items)
    assert long_res.status_code == 400
    assert long_res.json() == {"detail": "아이템 개수는 15개를 넘을 수 없습니다"}
