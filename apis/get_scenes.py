import os
import json
from .post_data import post_data
from .get_rooms import get_rooms


def get_scenes(save: bool, room_idx=0) -> dict:
    """
    获取场景列表
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
    data = {"home_id": homeId}
    msg = post_data('/appgateway/miot/appsceneservice/AppSceneService/GetSceneList', data, authorize)
    scenes = json.loads(msg)
    if save:
        with open('./json/scenes.json', 'w', encoding='utf-8') as f:
            f.write(json.dumps(scenes, indent=4, ensure_ascii=False))
    return scenes
