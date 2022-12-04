import requests
from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

user_results = []
if __name__ == "__main__":
    user_agent = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT6.1;Trident / 5.0)"}
    response = requests.get(url="https://www.acwing.com/user/myspace/index/70056/", headers=user_agent)

    soup = BeautifulSoup(response.text, 'html.parser')
    for user in soup.select(".user-myspace-base-person-visit-record-body-items"):
        user_id = user.get("data-user-id")
        username = user.select(".user-myspace-base-person-visit-record-body-items-username")[0].text
        user_photos = user.find_all(attrs={"class":"user-myspace-base-person-visit-record-body-items-photo"})[0].img.get("src")
        user_result = {"user_id":user_id, "username":username, "user_photos":user_photos}
        user_results.append(user_result)

    print(user_results[0]["username"])