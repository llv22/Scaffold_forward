import os
from openai import OpenAI
from http import HTTPStatus
import dashscope
# pip install python-dotenv
from dotenv import load_dotenv
load_dotenv()
import base64
import mimetypes

def get_response():
    client = OpenAI(
        api_key=os.getenv("DASHSCOPE_API_KEY"),
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    )
    image1_path = 'data/examples/imgs/1.jpg'
    image2_path = 'data/examples/imgs/2.jpg'
    encoded_image1_str, encoded_image2_str = encode_image(image1_path), encode_image(image2_path)
        
    completion = client.chat.completions.create(
        model="qwen-vl-plus",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "What are those two pictures?"
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": encoded_image1_str
                        }
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": encoded_image2_str
                        }
                    }
                ]
            }
        ],
        top_p=0.8,
        # stream=True,
        # stream_options={"include_usage": True}
    )
    result = completion.choices[0].message.content
    print(result)

def encode_image(image_path):
    mime_type, _ = mimetypes.guess_type(image_path)
    if mime_type and mime_type.startswith('image'):
        with open(image_path, 'rb') as image_file:
            encoded_image = base64.b64encode(image_file.read())
            encoded_image_str = encoded_image.decode('utf-8')
            data_uri_prefix = f'data:{mime_type};base64,'
            encoded_image_str = data_uri_prefix + encoded_image_str
    else:
        print("MIME type unsupported or not found.")
        exit(1)
    return encoded_image_str

# Openai calling: https://help.aliyun.com/zh/dashscope/developer-reference/compatibility-of-openai-with-dashscope
def simple_multimodal_conversation_call():
    """Simple single round multimodal conversation call.
    """
    messages = [
        {
            "role": "user",
            "content": [
                {"image": "https://dashscope.oss-cn-beijing.aliyuncs.com/images/dog_and_girl.jpeg"},
                {"text": "What is this?"}
            ]
        }
    ]
    response = dashscope.MultiModalConversation.call(model='qwen-vl-plus', messages=messages)
    # The response status_code is HTTPStatus.OK indicate success,
    # otherwise indicate request is failed, you can get error code
    # and message from code and message.
    if response.status_code == HTTPStatus.OK:
        print(response.output.choices[0]['message']['content'][0]['text'])  # The response output.
    else:
        print(response.code)  # The error code.
        print(response.message)  # The error message.


if __name__ == '__main__':
    get_response()