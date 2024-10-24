from locust import HttpUser, task

class PackingUser(HttpUser):
    @task
    def packing(self):
        self.client.post("/packing", json=create_mock_data(20, styrofoam_box))


def create_mock_data(count, item):
    mock_data = {"items": []}

    for i in range(count):
        mock_data["items"].append(item)

    return mock_data


styrofoam_box = {
    "itemName": "styrofoam_box",
    "itemD": 200,
    "itemH": 230,
    "itemW": 200,
    "itemIndex": 0,
    "itemScaleX": 1,
    "itemScaleY": 1,
    "itemScaleZ": 1,
    "loadBear": 1000,
}
