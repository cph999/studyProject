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
    wbk = xlwt.Workbook(encoding = 'utf-8')
    sheet=wbk.add_sheet('sheet1')

    # 写入表头
    for filed in range(0, len(head_data)):
        sheet.write(0, filed, head_data[filed])
    print(records[0][0])
    # 写入数据记录
    for row in range(1, len(records) + 1):
        for col in range(0, len(head_data)):
            if len(records[row - 1]) > col:
                sheet.write(row, col, records[row-1][col])
            # # 设置默认单元格宽度
            # sheet.col(col).width = 256 * 15

    return wbk


if __name__ == "__main__":
    user_agent = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT6.1;Trident / 5.0)"}
    response = requests.get(url="http://www.china-yao.com/", headers=user_agent)
    soup = BeautifulSoup(response.text, 'html.parser')
    for param in soup.find_all(attrs={"data-id": 1}):
        params.append(param.text)
    print(params)
    index = 0
    for param in params:
        url = search_pre + param
        response = requests.get(url=url, headers=user_agent)
        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.select("div > table")[0]
        if index == 0:
            for thead in table.select("thead > tr"):
                for th_name in thead.select("tr > th"):
                    table_head.append(th_name.text)
        for tr in table.select("tbody > tr"):
            i = 0
            result = {}
            for td in tr.find_all(name="td"):
                result[i] = td.text
                i += 1
            search_results.append(result)
        index += 1

    to_excel(table_head, search_results).save("./医药价格.xls")


