# coding=utf-8
import string

import requests
import xlwt
from bs4 import BeautifulSoup
import json


def to_excel(head_data, records):
    # 工作表
    wbk = xlwt.Workbook(encoding='utf-8')
    sheet = wbk.add_sheet('sheet1')

    # 写入表头
    for filed in range(0, len(head_data)):
        sheet.write(0, filed, head_data[filed])
    # 写入数据记录
    print(records[0][0])
    for row in range(1, len(records) + 1):
        for col in range(0, len(head_data)):
            if len(records[row - 1]) > col:
                sheet.write(row, col, records[row - 1][col])
            # # 设置默认单元格宽度
            # sheet.col(col).width = 256 * 15

    return wbk


detail_headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    "sec-ch-ua-platform": "Windows",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "cookie": "__jdu=1670124196295939057958; PCSYCityID=CN_120000_120100_0; shshshfpa=bc01c0fa-92ad-45e5-bb44-85c1b23be8bf-1670124198; shshshfpb=eVZVfX6NFKE4kPE-WhhladQ; unpl=JF8EAMdnNSttCB9UV0kES0FHHwgBW1gLTB8EbjIBXFxfTVANEwNJERl7XlVdXhRLFB9uYRRXXFNLUQ4fASsSEXteXVdZDEsWC2tXVgQFDQ8VXURJQlZAFDNVCV9dSRZRZjJWBFtdT1xWSAYYRRMfDlAKDlhCR1FpMjVkXlh7VAQrAhwUEUteUV5VD0gfB2dlDVVZXkNQDCsDKxUge21QVlwKTCcCX2Y1FgkESVMFHwIcXxBMW1VeXg1LHwRsbwFcX1BKUAMTBhIiEXte; __jdv=76161171|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_ae1cc7abfedd4426960d590675990c28|1670415294663; jsavif=1; areaId=1; ipLoc-djd=1-2901-55561-0; shshshfp=de6869b88aa65b1bc6e19da4648d0d43; jsavif=1; __jda=122270672.1670124196295939057958.1670124196.1670415295.1670587650.3; __jdc=122270672; ip_cityCode=51039; token=b9b258236dbc59469e9faee0165a0da4,2,928106; __tk=k0KwibRaRjB3qabVkyCnYzfxk1OmlypikDKOZlzuky9mly8Jkz3tqkRan1p3nD2CSk36qkRn,2,928106; shshshsID=f3905250bb79a12fc114a942d3dfacfc_19_1670592573166; chat.jd.com=20170206; mba_muid=1670124196295939057958; mba_sid=16705929556076039516709309978.1; __jdb=122270672.23.1670124196295939057958|3.1670587650; 3AB9D23F7A4B3C9B=QM342VW3QYI4ETVMI5QKV3QO7JVDFGOELRXGFFZQDL5RGJ4ERJV6GWQVVH56EJLV46STSOC77IAZBAS4DEQMQQVQ24; wlfstk_smdl=f5q51pa7scoad129xerykkgpv2il6qmm"}
url_pre = "https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=%s&score=0&sortType=5&page=0&pageSize=15&isShadowSku=0&fold=1"
results = []
head_data = ["书名", "Spu", "作者", "价格", "店铺"]
if __name__ == "__main__":
    comment_len = 10
    headers = {
        "cookie": "__jdu=1670124196295939057958; PCSYCityID=CN_120000_120100_0; shshshfpa=bc01c0fa-92ad-45e5-bb44-85c1b23be8bf-1670124198; shshshfpb=eVZVfX6NFKE4kPE-WhhladQ; unpl=JF8EAMdnNSttCB9UV0kES0FHHwgBW1gLTB8EbjIBXFxfTVANEwNJERl7XlVdXhRLFB9uYRRXXFNLUQ4fASsSEXteXVdZDEsWC2tXVgQFDQ8VXURJQlZAFDNVCV9dSRZRZjJWBFtdT1xWSAYYRRMfDlAKDlhCR1FpMjVkXlh7VAQrAhwUEUteUV5VD0gfB2dlDVVZXkNQDCsDKxUge21QVlwKTCcCX2Y1FgkESVMFHwIcXxBMW1VeXg1LHwRsbwFcX1BKUAMTBhIiEXte; __jdv=76161171|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_ae1cc7abfedd4426960d590675990c28|1670415294663; jsavif=1; jsavif=1; __jda=122270672.1670124196295939057958.1670124196.1670415295.1670587650.3; __jdc=122270672; shshshfp=de6869b88aa65b1bc6e19da4648d0d43; rkv=1.0; token=e877ac43df2ee3459115e32face39a59,2,928104; __tk=jujDjrfskuAqkYkqjYApAchuBUnEAuhrAYa1jrGDBc4,2,928104; ip_cityCode=51039; areaId=1; ipLoc-djd=1-2901-55561-0; avif=1; qrsc=3; __jdb=122270672.6.1670124196295939057958|3.1670587650; shshshsID=f3905250bb79a12fc114a942d3dfacfc_6_1670588475013; 3AB9D23F7A4B3C9B=QM342VW3QYI4ETVMI5QKV3QO7JVDFGOELRXGFFZQDL5RGJ4ERJV6GWQVVH56EJLV46STSOC77IAZBAS4DEQMQQVQ24",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
        "sec-ch-ua-platform": "Windows",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"}
    url = "https://search.jd.com/Search?keyword=kubernetes&enc=utf-8&wq=kubernetes&pvid=a29911fcfe504fbc9c3c4d4c97c3097c"
    response = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    book_container = soup.find(attrs={"id": "J_goodsList"})
    for book_info in book_container.select("ul > li > div"):
        book_result = []
        detail_url = book_info.find(attrs={"class": "p-img"}).a["href"]
        detail_number = detail_url[14:len(detail_url) - 5]
        book_price = book_info.find(attrs={"class": "p-price"}).text
        outlet_name = book_info.find(attrs={"class": "p-shopnum"})
        if outlet_name and outlet_name is not None:
            outlet_name = outlet_name.a
            if outlet_name and outlet_name is not None:
                outlet_name = outlet_name["title"]
        tips = ""
        for tip in book_info.find(attrs={"class": "p-icons"}).find_all(name="i"):
            tips += tip["data-tips"] + ";"
        detail_book_info = requests.get(url="https:" + detail_url, headers=detail_headers)
        detail_book_info = BeautifulSoup(detail_book_info.text, "html.parser")
        book_name = detail_book_info.find(attrs={"class": "sku-name"}).text
        author_name = detail_book_info.find(attrs={"class": "p-author"}).text

        book_name = book_name[75:150]
        book_result.append(book_name)
        book_result.append(author_name)
        book_result.append(detail_number)
        book_result.append(book_price)
        book_result.append(outlet_name)
        # to operate the detail data
        url_comment = url_pre % detail_number
        response = requests.get(url=url_comment, headers=detail_headers)
        response_result = response.text.replace("fetchJSON_comment98", "")
        response_result = response_result[1:len(response_result) - 2]
        response_json_result = json.loads(response_result)
        comment_len = len(response_json_result["comments"])
        comment_len = max(comment_len, 10)
        for comment in response_json_result["comments"]:
            result = {"nickname": comment["nickname"], "content": comment["content"],
                      "creationTime": comment["creationTime"], "userImage": comment["userImage"]}
            if comment.has_key("videos"):
                result["videos"] = comment["videos"]
            if comment.has_key("images"):
                result["images"] = comment["images"]
            result = str(result)
            book_result.append(result)
        results.append(book_result)
        print(book_result)
    for i in range(1, comment_len):
        head_data.append("评价"+str(i))
    to_excel(head_data, results).save("./k8s.xls")
