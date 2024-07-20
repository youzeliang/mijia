import json
from .post_data import post_data


def get_devices(save: bool) -> dict:
    """
    获取设备列表
    :param save:
    :return:
    """
    authorize = json.load(open('./json/authorize.json', 'r', encoding='utf-8'))
    data = {"getVirtualModel": False, "getHuamiDevices": 0}
    msg = post_data('/home/device_list', data, authorize)
    devs = json.loads(msg)
    if save:
        with open('./json/devices.json', 'w', encoding='utf-8') as f:
            f.write(json.dumps(devs, indent=4, ensure_ascii=False))
    return devs
