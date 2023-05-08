import os
from PIL import Image
import openai
import requests
from io import BytesIO
import json
with open("imagenum.json", "r") as f:
    jsonfile = json.load(f)
fledir = os.getcwd()+"\ScriptImages"
PROMPT = str(input("enter prompt: "))
print("loading...")
openai.api_key = 'OPEN_AI_KEY'
response = openai.Image.create(
    prompt=PROMPT,
    n=1,
    size="256x256",
)
response = requests.get(response['data'][0]['url'])
img = Image.open(BytesIO(response.content))
img.show()
save = str(input("would you like to save the image file? (y/n): "))
if save.lower() == "y" or save.lower() == "yes":
    while True:
        if os.path.exists(fledir):

            with open("imagenum.json", "w") as f:
                currentnum = int(jsonfile["file"])
                if currentnum == 0:
                    fledir = os.getcwd() + f"\ScriptImages\image.png"
                else:
                    fledir = os.getcwd() + f"\ScriptImages\image{currentnum}.png"
                file = os.getcwd() + "\ScriptImages"
                img.save(fledir)
                count1 = currentnum + 1
                count1 = str(count1)
                jsonfile["file"] = count1

                json.dump(jsonfile, f, indent=2)
            if currentnum == 0:
                print(f"Image saved, check: {file}\image.png")
            else:
                print(f"Image saved, check: {file}\image{currentnum}.png")
            break
        else:
            os.mkdir("ScriptImages")
            print(f'File not found so created one in: {fledir}')
