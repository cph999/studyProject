# coding=utf-8
import requests
import xlwt
from bs4 import BeautifulSoup

params = ["头孢", "葡萄糖", "阿莫西林"]
table_head = []
search_pre = "http://www.china-yao.com/?act=search&typeid=1&keyword="
search_results = []


def to_excel(head_data, records):
    # 工作表
    wbk = xlwt.Workbook(encoding='utf-8')
    sheet = wbk.add_sheet('sheet1')

    # 写入表头
    for filed in range(0, len(head_data)):
        sheet.write(0, filed, head_data[filed])
    # 写入数据记录
    for row in range(1, len(records) + 1):
        for col in range(0, len(head_data)):
            if len(records[row - 1]) > col:
                sheet.write(row, col, records[row - 1][col])
            # # 设置默认单元格宽度
            # sheet.col(col).width = 256 * 15

    return wbk


if __name__ == "__main__":
    # 伪装头部信息
    user_agent = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT6.1;Trident / 5.0)"}
    # 请求首页，拿到热词信息
    response = requests.get(url="http://www.china-yao.com/", headers=user_agent)
    soup = BeautifulSoup(response.text, 'html.parser')
    for param in soup.find_all(attrs={"data-id": 1}):
        params.append(param.text)
    # 用于添获取表头判断
    index = 0
    # 对所有词进行结果爬虫
    for param in params:
        # 请求第一页，获取页码和表头信息
        url = search_pre + param
        response = requests.get(url=url, headers=user_agent)
        soup = BeautifulSoup(response.text, 'html.parser')
        pagination = -1
        for pageul in soup.find_all(attrs={"class": "pagination"}):
            for a in pageul.select("li > a"):
                if a.text != u"»":
                    pagination = max(pagination, int(a.text))
            pagination = min(pagination, 5)
        # 获取表格
        table = soup.select("div > table")[0]
        if index == 0:
            for thead in table.select("thead > tr"):
                for th_name in thead.select("tr > th"):
                    table_head.append(th_name.text)
        # 获取数据
        for pageNum in range(1, pagination + 1):
            print(params[index])
            print(pageNum)
            url = search_pre + param + "&page=" + str(pagination)
            response = requests.get(url=url, headers=user_agent)
            soup = BeautifulSoup(response.text, 'html.parser')
            table = soup.select("div > table")[0]
            for tr in table.select("tbody > tr"):
                i = 0
                result = {}
                for td in tr.find_all(name="td"):
                    result[i] = td.text
                    i += 1
                search_results.append(result)
        index += 1

    to_excel(table_head, search_results).save("./medical_price.xls")
