import json


with open('gpt_request.json') as json_file:
            data = json_file.read()
data=data.replace("{bot_i}", "ldjcndcn")
print(eval(data))
