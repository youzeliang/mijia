import json
from .post_data import post_data


def get_dev_att(devs: list) -> dict:
    """
    获取设备属性
    getDevAtt(devs) -> dict.
    :param devs:
    :return:
    """
    authorize = json.load(open('./json/authorize.json', 'r', encoding='utf-8'))
    data = {"params": devs}
    msg = post_data('/miotspec/prop/get', data, authorize)
    res = json.loads(msg)
    return res


def set_dev_att(devs: list) -> str:
    """
    设置设备属性
    :param devs:
    :return:
    """
    authorize = json.load(open('./json/authorize.json', 'r', encoding='utf-8'))
    data = {"params": devs}
    msg = post_data('/miotspec/prop/set', data, authorize)
    return msg
