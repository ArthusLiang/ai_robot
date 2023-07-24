import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder

from core import path_output, get_args

args = get_args()

def send_message(token, roomId, parentId):
    data = {
        "roomId": "3c70a030-26ee-11ee-a726-0f39761950a4",
        "parentId": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvZjMyYzJhNjAtMjljOC0xMWVlLWIxYzAtYTE1M2VmY2UyYmM5",
        "text": "test robot reply",
        'files': ('new.png', open(path_output, 'rb'), 'image/png')
    }

    url = "https://webexapis.com/v1/messages"
    m_data = MultipartEncoder(data)
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': m_data.content_type
    }

    response = requests.post(url, data=m_data, headers=headers)

    if response.status_code == 200:
        print("请求成功！")
        print("响应内容：", response.text)
    else:
        print("请求失败！状态码：", response.status_code)
        print("响应内容：", response.text)
        
send_message(args['token'],1,1)