ITEM_LIST = {
    "shoes_box": {
        "itemName": "shoes_box",
        "itemIndex": 0,
        "itemScaleX": 1,
        "itemScaleY": 1,
        "itemScaleZ": 1,
        "itemW": 310,
        "itemH": 130,
        "itemD": 200,
        "loadBear": 2000,
    },
    "book": {
        "itemName": "book",
        "itemIndex": 1,
        "itemScaleX": 1,
        "itemScaleY": 1,
        "itemScaleZ": 1,
        "itemW": 152,
        "itemH": 200,
        "itemD": 15,
        "loadBear": 500,
    },
    "styrofoam_box": {
        "itemName": "styrofoam_box",
        "itemIndex": 2,
        "itemScaleX": 1,
        "itemScaleY": 1,
        "itemScaleZ": 1,
        "itemW": 200,
        "itemH": 230,
        "itemD": 200,
        "loadBear": 1000,
    },
}


empty_items = {"items": []}

normal_items = {
    "items": [ITEM_LIST["shoes_box"], ITEM_LIST["book"], ITEM_LIST["styrofoam_box"]]
}


normal_items_res = {
    "result": [
        {
            "boxSize": ["5호", [480, 340, 380]],
            "itemList": [
                {
                    "itemName": "shoes_box",
                    "itemIndex": 0,
                    "itemScale": [1, 1, 1],
                    "position": [0, 0, 0],
                    "rotationType": 0,
                },
                {
                    "itemName": "styrofoam_box",
                    "itemIndex": 2,
                    "itemScale": [1, 1, 1],
                    "position": [230, 130, 0],
                    "rotationType": 1,
                },
                {
                    "itemName": "book",
                    "itemIndex": 1,
                    "itemScale": [1, 1, 1],
                    "position": [310, 0, 0],
                    "rotationType": 0,
                },
            ],
        }
    ]
}


long_items = {"items": []}

for i in range(16):
    long_items["items"].append(ITEM_LIST["shoes_box"])
