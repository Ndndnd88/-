import requests
 
headers = {
    "Accept": "*/*", 
    "Accept-Encoding": "identity;q=1, *;q=0", 
    "Accept-Language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,und;q=0.6", 
    "Host": "lurl-cc-di.ap-south-1.linodeobjects.com",
    "Sec-Fetch-Dest": "video", 
    "Sec-Fetch-Mode": "no-cors", 
    "Sec-Fetch-Site": "cross-site", 
    "Upgrade-Insecure-Requests": "1", 
    "If-Range": "c8e124eda2ab61a3588b69ed0ba4f0fe",
    "Range": "bytes=0-",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    "Referer": "https://lurl.cc/",
    "sec-ch-ua-platform": "Windows",
    "sec-ch-ua-mobile": "?0",
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    "Connection": "keep-alive",
    "Cache-Control": "no-cache",
    "Pragma": "no-cache"
}

url = 'https://lurl-cc-di.ap-south-1.linodeobjects.com/20230216/84b7df2d9884a81f58bd04676fd445c4.mov'
r = requests.get(url, headers=headers ,stream=True)
with open("test.mov",'wb') as f:
    f.write(r.content)

