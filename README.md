# Code Review
https://github.com/nangongchengfeng/Chat-CodeReview/tree/main
#### 原本的项目虽然功能已经很完善，但是还有一些场景没有满足需求，下面是针对原本项目 Chat-CodeReview 做了以下优化：
- 增加飞书 Webhook 配置。
- 增加过滤文件后缀配置。
- 增加Review的文件数量配置。
- 增加 Prompt 提示词配置。
- 修改一次提交最多只能同时处理一个commit。
- 优化处理 commit 信息方式。
#### 优化后的代码仓库：https://git.n.xiaomi.com/dasen/code-review.git
```
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

# 过滤文件包含
review_file_contain = ['.g.dart', 'i18n.dart']

# 最多同时review的文件数量
review_file_count = 5

# Prompt 提示词配置
review_prompt = "你是一位资深Flutter编程专家，gitlab的commit代码变更将以git diff 字符串的形式提供，注意：代码中：- 表示删除的代码，+ 表示新增的代码 # 表示代码注释，以格式「变更评分：实际的分数」给变更打分，分数区间为0~100分。输出格式：然后，以精炼的语言、严厉的语气指出存在的问题。如果你觉得必要的情况下，可直接给出修改后的内容。你的反馈内容必须使用严谨的markdown格式。"

```
