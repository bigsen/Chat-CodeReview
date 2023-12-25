# -*- coding: utf-8 -*-
import platform


"""
这个文件是用来从apollo配置中心获取配置的，
如果没有apollo配置中心，需要删掉这一块
"""
#from config.apollo_config import gitlab_server_url, gitlab_private_token, openai_api_key


# openai-chatgpt 相关配置
model_quester_anster = "text-davinci-003"
model_gpt_35_turbo = "gpt-3.5-turbo"
model_programming_translate = "code-davinci-002"

sys_platform = platform.platform().lower()

# 错误类型
# 没有费用
ERROR_NO_FEE = {
    "error": 'You exceeded your current quota',
    "desc": "费用不足"
}
# 账号信息不对
ERROR_ACCOUNT_INFO = {
    "error": 'Incorrect API key provided',
    "desc": "账号API信息有误"
}
# 违法政策
ERROR_VIOLATION_POLICIES = {
    "error": 'Your access was terminated due to violation of our policies',
    "desc": "违反政策"
}

"""
这个文件是用来从apollo配置中心获取配置的，
如果没有apollo配置中心，可以直接在这里配置
"""

# Secret 令牌，GitLab 项目中可自定义一个。
WEBHOOK_VERIFY_TOKEN = "chatgpt"

# GitLab 服务器URL
gitlab_server_url = ""

# GitLab 访问令牌
gitlab_private_token = ""

# 用于访问OpenAI的API的密钥
openai_api_key = ""

# OpenAI 接口
openai_baseurl = "https://api.openai.com/v1"

# GPT 模型
openai_model_name = "gpt-3.5-turbo"

# 飞书Webhook地址
feishu_webhook = ""

# 过滤文件后缀配置
review_file_suffix = ['dart', 'm', 'swift' , 'kt' ,'java']

# 最多同时review的文件数量
review_file_count = 5

# Prompt 提示词配置
review_prompt = "你是一位资深的编程专家，gitlab的commit代码变更将以git diff 字符串的形式提供，注意：代码中：- 表示删除的代码，+ 表示新增的代码 # 表示代码注释，以格式「变更评分：实际的分数」给变更打分，分数区间为0~100分。输出格式：然后，以精炼的语言、严厉的语气指出存在的问题。如果你觉得必要的情况下，可直接给出修改后的内容。你的反馈内容必须使用严谨的markdown格式。"
