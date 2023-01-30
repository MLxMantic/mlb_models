# -*- coding: cp1252 -*-
from selenium import webdriver
import time
from bs4 import BeautifulSoup
import sys
import string
import time
import lxml
import httplib
import socket
import httplib
import mechanize
import cookielib
import os


### CHANGE ALL DATES, INCLUDING TEXT FILES BEFORE BEGINNING TO SCRAPE ###
Year = '2015'
cur_Date = '?date=04032015'
date = '2016-04-11'
date_File = '?date=04112016'


Names = open("PitchNames_2016_04_11.txt", 'w')
Names_Header = "Rating"+";"+"Year"+";"+"Date"+";"+"Player"+";"+"Salary"+";"+"Team"+";"+"Opponent"+"\n"
Names.write(Names_Header)

Player_Data= open("Pitch_Stats_2016_04_11.txt", 'w')
Player_Stat_Header = "WHIP"+";"+"HR/9"+";"+"SO/9"+";"+"SO/AB"+";"+"wOBA"+";"+"Pro"+";"+"My"+";"+"Ump"+";"+"Bargain"+";"+"K_Pred"+";"+"Park_Factor"+";"+"Runs"+";"+"Opp_Runs"+";"+"Triangle"+";"+"ML"+';'+"O_U"+";"+"ML%"+";"+"Temp"+";"+"WindSpd"+";"+"WindDir"+";"+"Humidity"+';'+"Precip"+";"+"Count_15"+";"+"Dist_15"+";"+"EV_15"+";"+"FB_15"+";"+"GB_15"+";"+"LD_15"+";"+"HH_15"+";"+"Speed_15"+";"+"K_Perc"+";"+"Dist_Delta"+";"+"EVDelta_15"+";"+"HHDelta_15"+";"+"Speed_Delta"+";"+"Air_15"+";"+"Count_Year"+";"+"Dist_Season"+";"+"EV_Season"+";"+"FB_Season"+";"+"GB_Season"+";"+"LD_Season"+";"+"HH_Season"+";"+"GB/FB_Season"+";"+"Speed_Season"+";"+"K%_Season"+";"+"Air_Season"+";"+"Season_PPG"+";"+"Season_Change"+";"+"Season_PlusMin"+";"+"Season_Consistency"+";"+"Season_Upside"+";"+"Season_Duds"+";"+"Season_Count"+';'+"Month_PPG"+";"+"Month_Change"+";"+"Month_Consistency"+";"+"Month_Up"+";"+"Month_Dud"+";"+"Month_Count"+"\n"
Player_Data.write(Player_Stat_Header)


url = "http://www.fantasylabs.com/account/login/"
chromedriver = "C:/Users/Tom/Downloads/chromedriver_win32/chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
#driver = webdriver.PhantomJS(executable_path="C:/Users/Tom/Downloads/phantomjs-2.1.1-windows/phantomjs-2.1.1-windows/bin/phantomjs")
driver.get(url)
time.sleep(3)

#Find and fill in username/password
username = driver.find_element_by_name('input')
password = driver.find_element_by_name('password')
username.send_keys('bmars4gv@gmail.com')
password.send_keys('Jiqc8111')

#Find and click on the submit button
login_attempt = driver.find_element_by_class_name("pull-right")
login_attempt.click()

## Initialize cookie session if needed
br = mechanize.Browser()

cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)

# wait 10 seconds for web page to load
time.sleep(10)

#  Find and click the MLB tab
link = driver.find_element_by_partial_link_text('MLB')
link.click()

time.sleep(3)
#  Find and click the Player Models tab
link = driver.find_element_by_partial_link_text('Player Models')
link.click()




# Figure out how to scrape and scroll the targeted container
time.sleep(5)

Date_url = driver.current_url
New_URL = Date_url+date_File
print New_URL

driver.get(New_URL)

time.sleep(10)
#  Find and click the Player Models tab
xpath = "//label[contains(., 'Pitchers')]"
pitch = driver.find_element_by_xpath(xpath)
pitch.click()
time.sleep(5)


#driver.maximize_window()

html2 = driver.page_source




names = []
time.sleep(2)
soup = BeautifulSoup(html2, "lxml", from_encoding="utf-8")
div = soup.find_all('div', {'class':'ag-pinned-cols-container'})
for i in div:
    div_even = soup.find_all('div', {'class':'ag-row ag-row-even ag-row-level-0'})
    div_odd = soup.find_all('div', {'class':'ag-row ag-row-odd ag-row-level-0'})
    row = div_even + div_odd
    for i in row:
        empty = []
        time.sleep(1)
        div = i.find_all('div')
        div0 = div[0].text.encode('ascii', 'ignore').decode('ascii')
        div1 = div[1].text.encode('ascii', 'ignore').decode('ascii')
        div2 = div[2].text.encode('ascii', 'ignore').decode('ascii')
        div3 = div[3].text.encode('ascii', 'ignore').decode('ascii')
        div4 = div[4].text.encode('ascii', 'ignore').decode('ascii')
        div5 = div[5].text.encode('ascii', 'ignore').decode('ascii')
        div6 = div[6].text.encode('ascii', 'ignore').decode('ascii')
        left1 = div2+';'+Year+';'+date+';'+div3+';'+div4+';'+div5+';'+div6+'\n'
        if div1 == "":   
            Names.write(left1)
            print left1
        else:
            pass
    break

div_body = soup.find_all('div', {'class':'ag-body-container'})
for i in div_body:
    div_even2 = i.find_all('div', {'class':'ag-row ag-row-even ag-row-level-0'})
    div_odd2 = i.find_all('div', {'class':'ag-row ag-row-odd ag-row-level-0'})
    row2 = div_even2 + div_odd2
    count = 0
    for i in row2:
        time.sleep(1)
        div = i.find_all('div')
        div0 = str(div[0].text.encode('ascii', 'ignore').decode('ascii'))
        div1 = str(div[1].text.encode('ascii', 'ignore').decode('ascii'))
        div2 = str(div[2].text.encode('ascii', 'ignore').decode('ascii'))
        div3 = str(div[3].text.encode('ascii', 'ignore').decode('ascii'))
        div4 = str(div[4].text.encode('ascii', 'ignore').decode('ascii'))
        div5 = str(div[5].text.encode('ascii', 'ignore').decode('ascii'))
        div6 = str(div[6].text.encode('ascii', 'ignore').decode('ascii'))
        div7 = str(div[7].text.encode('ascii', 'ignore').decode('ascii'))
        div8 = str(div[8].text.encode('ascii', 'ignore').decode('ascii'))
        div9 = str(div[9].text.encode('ascii', 'ignore').decode('ascii'))
        div10 = str(div[10].text.encode('ascii', 'ignore').decode('ascii'))
        div11 = str(div[11].text.encode('ascii', 'ignore').decode('ascii'))
        div12 = str(div[12].text.encode('ascii', 'ignore').decode('ascii'))
        div13 = str(div[13].text.encode('ascii', 'ignore').decode('ascii'))
        div14 = str(div[14].text.encode('ascii', 'ignore').decode('ascii'))
        div15 = str(div[15].text.encode('ascii', 'ignore').decode('ascii'))
        div16 = str(div[16].text.encode('ascii', 'ignore').decode('ascii'))
        div17 = str(div[17].text.encode('ascii', 'ignore').decode('ascii'))
        div18 = str(div[18].text.encode('ascii', 'ignore').decode('ascii'))
        div19 = str(div[19].text.encode('ascii', 'ignore').decode('ascii'))
        div20 = str(div[20].text.encode('ascii', 'ignore').decode('ascii'))
        div21 = str(div[21].text.encode('ascii', 'ignore').decode('ascii'))
        div22 = str(div[22].text.encode('ascii', 'ignore').decode('ascii'))
        div23 = str(div[23].text.encode('ascii', 'ignore').decode('ascii'))
        div24 = str(div[24].text.encode('ascii', 'ignore').decode('ascii'))
        div25 = str(div[25].text.encode('ascii', 'ignore').decode('ascii'))
        div26 = str(div[26].text.encode('ascii', 'ignore').decode('ascii'))
        div27 = str(div[27].text.encode('ascii', 'ignore').decode('ascii'))
        div28 = str(div[28].text.encode('ascii', 'ignore').decode('ascii'))
        div29 = str(div[29].text.encode('ascii', 'ignore').decode('ascii'))
        div30 = str(div[30].text.encode('ascii', 'ignore').decode('ascii'))
        div31 = str(div[31].text.encode('ascii', 'ignore').decode('ascii'))
        div32 = str(div[32].text.encode('ascii', 'ignore').decode('ascii'))
        div33 = str(div[33].text.encode('ascii', 'ignore').decode('ascii'))
        div34 = str(div[34].text.encode('ascii', 'ignore').decode('ascii'))
        div35 = str(div[35].text.encode('ascii', 'ignore').decode('ascii'))
        div36 = str(div[36].text.encode('ascii', 'ignore').decode('ascii'))
        div37 = str(div[37].text.encode('ascii', 'ignore').decode('ascii'))
        div38 = str(div[38].text.encode('ascii', 'ignore').decode('ascii'))
        div39 = str(div[39].text.encode('ascii', 'ignore').decode('ascii'))
        div40 = str(div[40].text.encode('ascii', 'ignore').decode('ascii'))
        div41 = str(div[41].text.encode('ascii', 'ignore').decode('ascii'))
        div42 = str(div[42].text.encode('ascii', 'ignore').decode('ascii'))
        div43 = str(div[43].text.encode('ascii', 'ignore').decode('ascii'))
        div44 = str(div[44].text.encode('ascii', 'ignore').decode('ascii'))
        div45 = str(div[45].text.encode('ascii', 'ignore').decode('ascii'))
        div46 = str(div[46].text.encode('ascii', 'ignore').decode('ascii'))
        div47 = str(div[47].text.encode('ascii', 'ignore').decode('ascii'))
        div48 = str(div[48].text.encode('ascii', 'ignore').decode('ascii'))
        div49 = str(div[49].text.encode('ascii', 'ignore').decode('ascii'))
        div50 = str(div[50].text.encode('ascii', 'ignore').decode('ascii'))
        div51 = str(div[51].text.encode('ascii', 'ignore').decode('ascii'))
        div52 = str(div[52].text.encode('ascii', 'ignore').decode('ascii'))
        div53 = str(div[53].text.encode('ascii', 'ignore').decode('ascii'))
        div54 = str(div[54].text.encode('ascii', 'ignore').decode('ascii'))
        div55 = str(div[55].text.encode('ascii', 'ignore').decode('ascii'))
        div56 = str(div[56].text.encode('ascii', 'ignore').decode('ascii'))
        div57 = str(div[57].text.encode('ascii', 'ignore').decode('ascii'))
        div58 = str(div[58].text.encode('ascii', 'ignore').decode('ascii'))
        div59 = str(div[59].text.encode('ascii', 'ignore').decode('ascii'))
        try:
            div60 = str(div[60].text.encode('ascii', 'ignore').decode('ascii'))
        except:
            div60 = '0'
        #div61 = str(div[61].text.encode('ascii', 'ignore').decode('ascii'))
        left2 = div1+';'+div2+';'+div3+';'+div4+';'+div5+';'+div6+';'+div7+';'+div8+';'+div9+';'+div10+';'+div11+';'+div12+';'+div13+';'+div14+';'+div15+';'+div16+';'+div17+';'+div18+';'+div19+';'+div20+';'+div21+';'+div22+';'+div23+';'+div24+';'+div25+';'+div26+';'+div27+';'+div28+';'+div29+';'+div30+';'+div31+';'+div32+';'+div33+';'+div34+';'+div35+';'+div36+';'+div37+';'+div38+';'+div39+';'+div40+';'+div41+';'+div42+';'+div43+';'+div44+';'+div45+';'+div46+';'+div47+';'+div48+';'+div49+';'+div50+';'+div51+';'+div52+';'+div53+';'+div54+';'+div55+';'+div56+';'+div57+';'+div58+';'+div59+';'+div60+'\n'
        Player_Data.write(left2)
        print left2
            
while True:
    xpath = "//div[@class='ag-body-container']/div"
    divs = driver.find_elements_by_xpath(xpath)

    driver.execute_script('arguments[0].scrollIntoView();', divs[-1])
    time.sleep(5)
    html2 = driver.page_source


    names = []
    time.sleep(5)
    soup = BeautifulSoup(html2, "lxml", from_encoding="utf-8")
    div = soup.find_all('div', {'class':'ag-pinned-cols-container'})
    for i in div:
        div_even = soup.find_all('div', {'class':'ag-row ag-row-even ag-row-level-0'})
        div_odd = soup.find_all('div', {'class':'ag-row ag-row-odd ag-row-level-0'})
        row = div_even + div_odd
        for i in row:
            time.sleep(1)
            div = i.find_all('div')
            div0 = div[0].text.encode('ascii', 'ignore').decode('ascii')
            div1 = div[1].text.encode('ascii', 'ignore').decode('ascii')
            div2 = div[2].text.encode('ascii', 'ignore').decode('ascii')
            div3 = div[3].text.encode('ascii', 'ignore').decode('ascii')
            div4 = div[4].text.encode('ascii', 'ignore').decode('ascii')
            div5 = div[5].text.encode('ascii', 'ignore').decode('ascii')
            div6 = div[6].text.encode('ascii', 'ignore').decode('ascii')
            left3 = div2+';'+Year+';'+date+';'+div3+';'+div4+';'+div5+';'+div6+'\n'
            if div1 == "":   
                Names.write(left3)
                print left3
            else:
                pass
        break

    div_body = soup.find_all('div', {'class':'ag-body-container'})
    for i in div_body:
        div_even2 = i.find_all('div', {'class':'ag-row ag-row-even ag-row-level-0'})
        div_odd2 = i.find_all('div', {'class':'ag-row ag-row-odd ag-row-level-0'})
        row2 = div_even2 + div_odd2
        count = 0
        for i in row2:
            time.sleep(1)
            div = i.find_all('div')
            div0 = str(div[0].text.encode('ascii', 'ignore').decode('ascii'))
            div1 = str(div[1].text.encode('ascii', 'ignore').decode('ascii'))
            div2 = str(div[2].text.encode('ascii', 'ignore').decode('ascii'))
            div3 = str(div[3].text.encode('ascii', 'ignore').decode('ascii'))
            div4 = str(div[4].text.encode('ascii', 'ignore').decode('ascii'))
            div5 = str(div[5].text.encode('ascii', 'ignore').decode('ascii'))
            div6 = str(div[6].text.encode('ascii', 'ignore').decode('ascii'))
            div7 = str(div[7].text.encode('ascii', 'ignore').decode('ascii'))
            div8 = str(div[8].text.encode('ascii', 'ignore').decode('ascii'))
            div9 = str(div[9].text.encode('ascii', 'ignore').decode('ascii'))
            div10 = str(div[10].text.encode('ascii', 'ignore').decode('ascii'))
            div11 = str(div[11].text.encode('ascii', 'ignore').decode('ascii'))
            div12 = str(div[12].text.encode('ascii', 'ignore').decode('ascii'))
            div13 = str(div[13].text.encode('ascii', 'ignore').decode('ascii'))
            div14 = str(div[14].text.encode('ascii', 'ignore').decode('ascii'))
            div15 = str(div[15].text.encode('ascii', 'ignore').decode('ascii'))
            div16 = str(div[16].text.encode('ascii', 'ignore').decode('ascii'))
            div17 = str(div[17].text.encode('ascii', 'ignore').decode('ascii'))
            div18 = str(div[18].text.encode('ascii', 'ignore').decode('ascii'))
            div19 = str(div[19].text.encode('ascii', 'ignore').decode('ascii'))
            div20 = str(div[20].text.encode('ascii', 'ignore').decode('ascii'))
            div21 = str(div[21].text.encode('ascii', 'ignore').decode('ascii'))
            div22 = str(div[22].text.encode('ascii', 'ignore').decode('ascii'))
            div23 = str(div[23].text.encode('ascii', 'ignore').decode('ascii'))
            div24 = str(div[24].text.encode('ascii', 'ignore').decode('ascii'))
            div25 = str(div[25].text.encode('ascii', 'ignore').decode('ascii'))
            div26 = str(div[26].text.encode('ascii', 'ignore').decode('ascii'))
            div27 = str(div[27].text.encode('ascii', 'ignore').decode('ascii'))
            div28 = str(div[28].text.encode('ascii', 'ignore').decode('ascii'))
            div29 = str(div[29].text.encode('ascii', 'ignore').decode('ascii'))
            div30 = str(div[30].text.encode('ascii', 'ignore').decode('ascii'))
            div31 = str(div[31].text.encode('ascii', 'ignore').decode('ascii'))
            div32 = str(div[32].text.encode('ascii', 'ignore').decode('ascii'))
            div33 = str(div[33].text.encode('ascii', 'ignore').decode('ascii'))
            div34 = str(div[34].text.encode('ascii', 'ignore').decode('ascii'))
            div35 = str(div[35].text.encode('ascii', 'ignore').decode('ascii'))
            div36 = str(div[36].text.encode('ascii', 'ignore').decode('ascii'))
            div37 = str(div[37].text.encode('ascii', 'ignore').decode('ascii'))
            div38 = str(div[38].text.encode('ascii', 'ignore').decode('ascii'))
            div39 = str(div[39].text.encode('ascii', 'ignore').decode('ascii'))
            div40 = str(div[40].text.encode('ascii', 'ignore').decode('ascii'))
            div41 = str(div[41].text.encode('ascii', 'ignore').decode('ascii'))
            div42 = str(div[42].text.encode('ascii', 'ignore').decode('ascii'))
            div43 = str(div[43].text.encode('ascii', 'ignore').decode('ascii'))
            div44 = str(div[44].text.encode('ascii', 'ignore').decode('ascii'))
            div45 = str(div[45].text.encode('ascii', 'ignore').decode('ascii'))
            div46 = str(div[46].text.encode('ascii', 'ignore').decode('ascii'))
            div47 = str(div[47].text.encode('ascii', 'ignore').decode('ascii'))
            div48 = str(div[48].text.encode('ascii', 'ignore').decode('ascii'))
            div49 = str(div[49].text.encode('ascii', 'ignore').decode('ascii'))
            div50 = str(div[50].text.encode('ascii', 'ignore').decode('ascii'))
            div51 = str(div[51].text.encode('ascii', 'ignore').decode('ascii'))
            div52 = str(div[52].text.encode('ascii', 'ignore').decode('ascii'))
            div53 = str(div[53].text.encode('ascii', 'ignore').decode('ascii'))
            div54 = str(div[54].text.encode('ascii', 'ignore').decode('ascii'))
            div55 = str(div[55].text.encode('ascii', 'ignore').decode('ascii'))
            div56 = str(div[56].text.encode('ascii', 'ignore').decode('ascii'))
            div57 = str(div[57].text.encode('ascii', 'ignore').decode('ascii'))
            div58 = str(div[58].text.encode('ascii', 'ignore').decode('ascii'))
            div59 = str(div[59].text.encode('ascii', 'ignore').decode('ascii'))
            try:
                div60 = str(div[60].text.encode('ascii', 'ignore').decode('ascii'))
            except:
                div60 = '0'
            #div61 = str(div[61].text.encode('ascii', 'ignore').decode('ascii'))
            left4 = div1+';'+div2+';'+div3+';'+div4+';'+div5+';'+div6+';'+div7+';'+div8+';'+div9+';'+div10+';'+div11+';'+div12+';'+div13+';'+div14+';'+div15+';'+div16+';'+div17+';'+div18+';'+div19+';'+div20+';'+div21+';'+div22+';'+div23+';'+div24+';'+div25+';'+div26+';'+div27+';'+div28+';'+div29+';'+div30+';'+div31+';'+div32+';'+div33+';'+div34+';'+div35+';'+div36+';'+div37+';'+div38+';'+div39+';'+div40+';'+div41+';'+div42+';'+div43+';'+div44+';'+div45+';'+div46+';'+div47+';'+div48+';'+div49+';'+div50+';'+div51+';'+div52+';'+div53+';'+div54+';'+div55+';'+div56+';'+div57+';'+div58+';'+div59+';'+div60+'\n'
            Player_Data.write(left4)
            print left4
            count+=1
            print count
            if count >= '200':
                break
            else:
                continue
            
