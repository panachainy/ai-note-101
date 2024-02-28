import json
from urllib import request, parse
import random


class ComfyClient:

    def queue_prompt(prompt):
        f = open('feat/comfy_client/workflows/default_workflow_api.json')
        data = json.load(f)

        p = {"prompt": data}
        data = json.dumps(p).encode('utf-8')
        # print(data)
        req = request.Request(
            "http://127.0.0.1:8188/prompt", data=data, method='POST')
        y = json.dumps(req)
        print(y)
        request.urlopen(req)


# prompt = json.loads(prompt_text)
# #set the text prompt for our positive CLIPTextEncode
# prompt["6"]["inputs"]["text"] = "masterpiece best quality man"

# #set the seed for our KSampler node
# prompt["3"]["inputs"]["seed"] = 5


# queue_prompt(prompt)
