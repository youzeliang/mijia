import os
import json
from .post_data import post_data
from .get_rooms import get_rooms


def getcons_items(save: bool, room_idx=0) -> dict:
    """
    获取设备耗材
    :param save:
    :param roomIdx:
    :return:
    """
    authorize = json.load(open('./json/authorize.json', 'r', encoding='utf-8'))
    if os.path.exists('./json/rooms.json'):
        rooms = json.load(open('./json/rooms.json', 'r', encoding='utf-8'))
    else:
        rooms = get_rooms(save)
    try:
        homeId = rooms['result']['homelist'][room_idx]['id']
    except IndexError:
        print('房间号超出范围')
        return
    data = {"home_id": int(homeId), "owner_id": authorize['userId']}
    msg = post_data('/v2/home/standard_consumable_items', data, authorize)
    consItems = json.loads(msg)
    if save:
        with open('./json/consItems.json', 'w', encoding='utf-8') as f:
            f.write(json.dumps(consItems, indent=4, ensure_ascii=False))
    return consItems
