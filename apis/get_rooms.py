import json
from .post_data import post_data


def get_rooms(save: bool) -> dict:
    """
    获取房间列表
    :param save:
    :return:
    """
    authorize = json.load(open('./json/authorize.json', 'r', encoding='utf-8'))
    data = {"fg": False, "fetch_share": True, "fetch_share_dev": True, "limit": 300, "app_ver": 7}
    msg = post_data('/v2/homeroom/gethome', data, authorize)
    rooms = json.loads(msg)
    if save:
        with open('./json/rooms.json', 'w', encoding='utf-8') as f:
            f.write(json.dumps(rooms, indent=4, ensure_ascii=False))
    return rooms
