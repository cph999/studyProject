# coding=utf-8
import requests
import xlwt
from bs4 import BeautifulSoup


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


category = []
index = 0
p_index = 0
l_index = 0
columns = ["category_level", "parent_category_id", "category_id", "category_name"]
if __name__ == "__main__":
    headers = {
        "Cookie": "__jdu=1670124196295939057958; o2State={%22webp%22:true%2C%22avif%22:true}; areaId=3; PCSYCityID=CN_120000_120100_0; shshshfpa=bc01c0fa-92ad-45e5-bb44-85c1b23be8bf-1670124198; shshshfpb=eVZVfX6NFKE4kPE-WhhladQ; unpl=JF8EAMdnNSttCB9UV0kES0FHHwgBW1gLTB8EbjIBXFxfTVANEwNJERl7XlVdXhRLFB9uYRRXXFNLUQ4fASsSEXteXVdZDEsWC2tXVgQFDQ8VXURJQlZAFDNVCV9dSRZRZjJWBFtdT1xWSAYYRRMfDlAKDlhCR1FpMjVkXlh7VAQrAhwUEUteUV5VD0gfB2dlDVVZXkNQDCsDKxUge21QVlwKTCcCX2Y1FgkESVMFHwIcXxBMW1VeXg1LHwRsbwFcX1BKUAMTBhIiEXte; __jdv=76161171|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_ae1cc7abfedd4426960d590675990c28|1670415294663; __jda=122270672.1670124196295939057958.1670124196.1670124196.1670415295.2; __jdc=122270672; token=f7d743ba478e5f1b5a15dac85e76bcce,2,928008; __tk=iMPOiURxRUAKV0ACR0RwixAFVMpxVDjLicnFiUzwnln,2,928008; jsavif=1; shshshfp=de6869b88aa65b1bc6e19da4648d0d43; ip_cityCode=51039; ipLoc-djd=3-51043-55894-0; joyytokem=babel_4AfQf3FkPRGHhtqqKh9tsWyV97syMDFodU9oUjk5MQ==.WUN4WGZZQHxcYV9DfRZqXRAaPGFaBXpZLFlZeURjREQxWixZCyo+CD4TF14cLj4KXDk4MGI/OgAZLgwDFgs=.69962e24; shshshsID=db3a0dedb48722a18b75915b25201768_3_1670415345443; joyya=1670415344.1670415826.20.12xylgm; __jdb=122270672.10.1670124196295939057958|2.1670415295; 3AB9D23F7A4B3C9B=QM342VW3QYI4ETVMI5QKV3QO7JVDFGOELRXGFFZQDL5RGJ4ERJV6GWQVVH56EJLV46STSOC77IAZBAS4DEQMQQVQ24",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
        "Connection": "keep-alive",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Language": "zh,en;q=0.9,zh-TW;q=0.8,en-US;q=0.7,zh-CN;q=0.6",
    }
    response = requests.get(url="https://www.jd.com/allSort.aspx", headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    mainBox = soup.select("div.category-item.m")

    for box in mainBox:
        parent_category = box.select(".item-title")[0].span.text
        l_index += 1
        p_id = l_index
        result = [1, 0, l_index, parent_category]
        category.append(result)

        for dt_now in box.find_all(name="dt"):
            l_index += 1
            pp_id = l_index
            result = [2, p_id, l_index, dt_now.a.text]
            category.append(result)
            dd = dt_now.find_next(name="dd")
            for a in dd.select("a"):
                l_index += 1
                result = [3, pp_id, l_index, a.text]
                category.append(result)
    to_excel(columns, category).save("./category.xls")




