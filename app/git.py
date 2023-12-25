import json
from os import abort

from flask import Blueprint, request, jsonify

from config.config import WEBHOOK_VERIFY_TOKEN
from service.chat_review import review_code
from utils.LogHandler import log

git = Blueprint('git', __name__)
"""
git的蓝图

主要功能：获取gitlab的webhook，进行代码检查
"""


@git.route('/api')
def question():
    return 'hello world'


@git.route('/webhook', methods=['GET', 'POST'])
def webhook():
    """
    gitlab的webhook,用来接受gitlab的推送
    http://192.168.96.19:5000/git/webhook
    """
    if request.method == 'GET':
        # 获取gitlab的webhook的token
        verify_token = request.headers.get('X-Gitlab-Token')

        # gitlab的webhook的token验证
        if verify_token == WEBHOOK_VERIFY_TOKEN:
            return jsonify({'status': 'success'}), 200
        else:
            return jsonify({'status': 'bad token'}), 401

    elif request.method == 'POST':
        """
        webhook的主要逻辑,获取gitlab的推送信息
        """
        # 获取gitlab的推送信息
        gitlab_message = request.data.decode('utf-8')
        # 将gitlab的推送信息转换为字典
        gitlab_message = json.loads(gitlab_message)
        # 获取项目的类型
        object_kind = gitlab_message.get('object_kind')
        # 获取gitlab的webhook的token
        verify_token = request.headers.get('X-Gitlab-Token')

        """
        项目为commit时，才进行代码检查，目前我只实现了commit的检查，后续可以添加merge和tag的检查
        
        涵盖push（commit）、merge（合并请求）和tag（标签创建）等三种代码提交方式
        """
        # 项目为commit时，才进行代码检查
        if verify_token == WEBHOOK_VERIFY_TOKEN and object_kind == 'push':
            # 验证通过，获取commit的信息
            print(gitlab_message)
            # 获取项目id
            project_id = gitlab_message.get('project')['id']
            # 获取所有的commit的id
            project_commit_id = gitlab_message.get('commits')
            # 获取项目的分支
            version = gitlab_message.get('ref').split('/')[-1]
            # 定义一个空列表，用来存放commit的id
            commit_list = []
            # 定义一个空列表，用来存放commit的url
            commit_list_url = []

            title = project_commit_id[0]['title']
            branch = gitlab_message.get('ref')
            user_name = gitlab_message.get('user_username')
            time = project_commit_id[0]['timestamp']

            # 遍历commit的id
            for i in project_commit_id:
                commit_list.append(i['id'])
                commit_list_url.append(i['url'])

            # print(project_id, version, commit_list)
            log.info(f"项目id: {project_id}，分支: {version}，commit_id: {commit_list} ")
            # 440 dev ['df4fa64a43f9b227c90d46a71556b717812635ca']
            log.info(f"项目id: {project_id}，commit_url: {commit_list_url}")
            log.info(f"项目id: {project_id}，commit_id: {commit_list} 开始进行ChatGPT代码补丁审查")
            review_code(project_id, commit_list, commit_list_url, title, branch, user_name, time)

            return jsonify({'status': 'success'}), 200

        else:
            log.error("项目不是push")
            return jsonify({'status': 'bad token'}), 401

    else:
        abort(400)
