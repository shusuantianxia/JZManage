#-*- coding = utf-8 -*-
from bs4 import BeautifulSoup
import re
import urllib.request
import urllib.error
import xlwt
import numpy as np


def main():
    baseUrl = "http://fund.eastmoney.com/trade/"
    #1.爬取网页
    dataList = getData(baseUrl)
    #2.解析数据
    savepath = ".\\jj.xls"
    #3.保存数据
    # saveData(savepath)

findLinkTd = re.compile(r'<td(.*?)</td>')

#爬取网页
def getData(baseUrl):
    jjList = ["pg", "gp", "hh", "zq", "zs", "qdii", "fof", "dkzq"]
    jj = ["xf", "lc", "hb", "hd"]
    for i in range(0, 8):
        url = baseUrl + jjList[i] + ".html"
        if i > 7:
            html = askURL(url, "utf-8")
        else:
            html = askURL(url, "gbk")
        # 解析
        soup = BeautifulSoup(html, "html.parser")
        thdata = ['基金代码', '基金名称', '单位净值', '日增长率', '近1周', '近1月', '近3月', '近6月', '近1年', '近2年', '近3年', '今年来', '成立来', '手续费|起购金额', '操作']
        tddata = []
        for item in soup.find_all("tr"):
            item = str(item)
            tdlink = re.findall(findLinkTd, item)
            if len(tdlink) > 0:
                tddata.append(tdlink)
        tdarray = np.array(tddata).reshape(-1, 15)
        tharray = np.array(thdata).reshape(-1, 15)
        for j in range(len(tdarray)):
            for k in range(15):
                if k == 2:
                    p = str(tdarray[j, k]).split("</span>")[0]
                    q = str(tdarray[j, k]).split("</span>")[1]
                    tdarray[j, k] = p.split(">")[-1] + "/" + q.split(">")[-1]
                else:
                    tdarray[j, k] = str(tdarray[j, k]).split("</")[0]
                    tdarray[j, k] = str(tdarray[j, k]).split(">")[-1]
        jjArray = np.concatenate((tharray, tdarray), axis=0)
        saveData(jjList[i] + ".xls", jjList[i], jjArray)

#得到指定一个URL的网页内容
def askURL(url, code):
    head = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0"}
    request = urllib.request.Request(url, headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode(code)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html

# 保存数据
def saveData(savePath, filename, jjarray):
    # 创建 Workbook 对象
    excel = xlwt.Workbook(encoding='utf-8')
    # 创建工作表
    sheet = excel.add_sheet(filename)

    for i in range(len(jjarray)):
        for j in range(15):
            sheet.write(i, j, jjarray[i, j])
    excel.save(savePath)

if __name__ == "__main__":
    main()