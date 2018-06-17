from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from datetime import datetime
from pytz import timezone

def lunch():
    #Set Timezone to Seoul and get Current Time
    error = 0
    fmt = "%Y.%m.%d"
    fmtDay = "%A"
    time_KST = datetime.now(timezone('Asia/Seoul'))
    day_KST = datetime.now(timezone('Asia/Seoul'))
    day = day_KST.strftime(fmtDay)
    
    #Open Neis Meal Server Page and Get HTML Code
    url = "http://stu.sen.go.kr/sts_sci_md01_001.do?schulCode=B100000470&schulCrseScCode=4&schulKndScCode=04&schMmealScCode=2&schYmd=" + time_KST.strftime(fmt)
    html = urlopen(url).read()

    #Parse HTML Code
    soup = BeautifulSoup(html, "html.parser")
    meal_table = soup.find("table", class_="tbl_type3")
    meal_thead = meal_table.find_all("thead")
    trs = meal_table.tbody.find_all("tr")
    meal_tr = trs[1]
    menus = meal_tr.find_all("td", class_="textC")

    #Get Meal Text 1 is Monday, 2 is Tuesday and more
    try:
        meal_mon = menus[1].text
        meal_tue = menus[2].text
        meal_wed = menus[3].text
        meal_thu = menus[4].text
        meal_fri = menus[5].text
    except IndexError:
        error = 1
        pass
    if error == 1:
        returnValue = "중식이 없습니다."
    else:
        #0 is Monday, 1 is Tuesday, and 5, 6 is Saturday and Sunday
        if day == "0":
            returnValue = (meal_mon)
        elif day == "1":
            returnValue = (meal_tue)
        elif day == "2":
            returnValue = (meal_wed)
        elif day == "3":
            returnValue = (meal_thu)
        elif day == "4":
            returnValue = (meal_fri)
        elif day == "Monday":
            returnValue = (meal_mon)
        elif day == "Tuesday":
            returnValue = (meal_tue)
        elif day == "Wednesday":
            returnValue = (meal_wed)
        elif day == "Thursday":
            returnValue = (meal_thu)
        elif day == "Friday":
            returnValue = (meal_fri)
        else:
            returnValue = "중식이 없습니다."
    return (returnValue)

def dinner():
    #Set Timezone to Seoul and get Current Time
    error = 0
    fmt = "%Y.%m.%d"
    fmtDay = "%A"
    time_KST = datetime.now(timezone('Asia/Seoul'))
    day_KST = datetime.now(timezone('Asia/Seoul'))
    day = day_KST.strftime(fmtDay)
    
    #Open Neis Meal Server Page and Get HTML Code
    url = "http://stu.sen.go.kr/sts_sci_md01_001.do?schulCode=B100000470&schulCrseScCode=4&schulKndScCode=04&schMmealScCode=3&schYmd=" + time_KST.strftime(fmt)
    html = urlopen(url).read()

    #Parse HTML Code
    soup = BeautifulSoup(html, "html.parser")
    meal_table = soup.find("table", class_="tbl_type3")
    meal_thead = meal_table.find_all("thead")
    trs = meal_table.tbody.find_all("tr")
    meal_tr = trs[1]
    menus = meal_tr.find_all("td", class_="textC")

    #Get Meal Text 1 is Monday, 2 is Tuesday and more
    try:
        meal_mon = menus[1].text
        meal_tue = menus[2].text
        meal_wed = menus[3].text
        meal_thu = menus[4].text
        meal_fri = menus[5].text
    except IndexError:
        error = 1
        pass
    if error == 1:
        returnValue = "석식이 없습니다."
    else:
        #0 is Monday, 1 is Tuesday, and 5, 6 is Saturday and Sunday
        if day == "0":
            returnValue = (meal_mon)
        elif day == "1":
            returnValue = (meal_tue)
        elif day == "2":
            returnValue = (meal_wed)
        elif day == "3":
            returnValue = (meal_thu)
        elif day == "4":
            returnValue = (meal_fri)
        else:
            returnValue = "석식이 없습니다."
    return (returnValue)
