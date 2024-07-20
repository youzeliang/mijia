import os
import json
from .post_data import post_data
from .get_scenes import get_scenes


def run_scene(name: str) -> int:
    """
    运行场景
    :param name:
    :return:
    """
    global scene_id
    authorize = json.load(open('./json/authorize.json', 'r', encoding='utf-8'))
    if os.path.exists('./json/scenes.json'):
        scenes = json.load(open('./json/scenes.json', 'r', encoding='utf-8'))
    else:
        scenes = get_scenes(True)

    scenesList = scenes['result']['scene_info_list']
    for scene in scenesList:
        if scene['name'] == name:
            scene_id = scene['scene_id']
            break
    try:
        data = {"scene_id": scene_id, "trigger_key": "user.click"}
    except NameError:
        print("场景名称不存在")
        return -1
    msg = post_data('/appgateway/miot/appsceneservice/AppSceneService/RunScene', data, authorize)
    msg = json.loads(msg)
    if msg['result']:
        return 0
    else:
        print(msg)
        return -1
