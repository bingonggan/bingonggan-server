from py3dbp import Packer, Bin, Item
import constants


def get_packed_item_list(item_list):
    packed_item_list = []
    box_max_size = len(constants.BOX_SIZE) - 1

    items = get_items(item_list)

    def get_item_info(items):
        item_list = items
        size = 0

        while True:
            unfitted_items = check_box_sizes(item_list, size)

            if not unfitted_items:
                break

            size += 1

            if size > box_max_size:
                get_item_info(unfitted_items)
                for item in unfitted_items:
                    item_list.remove(item)
                size -= 1
                break

        packer = pack_box(item_list, size)

        for box in packer.bins:
            req_item = {
                "boxSize": (
                    box.partno,
                    [int(box.width), int(box.height), int(box.depth)],
                ),
                "itemList": [],
            }

            for item in box.items:
                req_item["itemList"].append(
                    {
                        "itemName": item.name["item_name"],
                        "itemIndex": item.name["item_index"],
                        "itemScale": item.partno,
                        "position": calculate_position(item),
                        "rotationType": item.rotation_type,
                    }
                )

            packed_item_list.append(req_item)

    get_item_info(items)

    return packed_item_list


def calculate_position(item):
    if item.rotation_type == 1:
        item.position = [
            item.position[0] + item.height,
            item.position[1],
            item.position[2],
        ]
    if item.rotation_type == 2:
        item.position = [
            item.position[0],
            item.position[1] + item.depth,
            item.position[2] + item.width,
        ]
    if item.rotation_type == 3:
        item.position = [
            item.position[0],
            item.position[1],
            item.position[2] + item.width,
        ]
    if item.rotation_type == 5:
        item.position = [
            item.position[0],
            item.position[1] + item.depth,
            item.position[2],
        ]

    return list(map(int, item.position))


def pack_box(items, size):
    packer = Packer()

    packer.addBin(
        Bin(
            partno=constants.BOX_SIZE[size][0],
            WHD=constants.BOX_SIZE[size][1],
            max_weight=100,
        )
    )

    for item in items:
        packer.addItem(item)

    packer.pack(
        bigger_first=True,
        fix_point=True,
        distribute_items=True,
        check_stable=False,
        support_surface_ratio=0.5,
        number_of_decimals=0,
    )

    return packer


def check_box_sizes(items, size):
    packer = Packer()

    packer.addBin(
        Bin(
            partno=constants.BOX_SIZE[size][0],
            WHD=constants.BOX_SIZE[size][1],
            max_weight=100,
        )
    )

    for item in items:
        packer.addItem(item)

    try:
        packer.pack(
            bigger_first=True,
            fix_point=True,
            distribute_items=True,
            check_stable=False,
            support_surface_ratio=0.5,
            number_of_decimals=0,
        )
    except ZeroDivisionError:
        return True

    for box in packer.bins:
        if len(box.unfitted_items) > 0:
            return box.unfitted_items
        else:
            return False


def get_items(items):
    packer_items = []

    for item in items:
        packer_item = Item(
            partno=(item.itemScaleX, item.itemScaleY, item.itemScaleZ),
            name={"item_name": item.itemName, "item_index": item.itemIndex},
            typeof="cube",
            WHD=(item.itemW, item.itemH, item.itemD),
            weight=1,
            level=1,
            loadbear=item.loadBear,
            updown=True,
            color="r",
        )

        packer_items.append(packer_item)

    return packer_items
