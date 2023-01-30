#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 19:50:55 2023

@author: tom
"""


from time import sleep
from random import randint
from bs4 import BeautifulSoup

import sys
import string
import time
import lxml


#import cookielib
import os
import os.path
import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as bsoup


from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option(
    "prefs", {"download.default_directory": r"./"})
chrome_options.add_argument("--user-data-dir=other")
chrome_options.add_argument("--autoplay-policy=no-user-gesture-required")
binary = "/home/tom/mlb_models/chromedriver"
driver = webdriver.Chrome(binary)

# os.path.abspath(os.getcwd())


os.chdir('/home/tom/mlb_models/')
delay = 2


### CHANGE ALL DATES, INCLUDING TEXT FILES3BEFORE BEGINNING TO SCRAPE ###
dates = pd.read_csv('./data/dates_2021.csv')
dates['datetime'] = pd.to_datetime(dates['dates'])
dates['year'] = dates['datetime'].dt.year

Names = open("Names_" + '2021' + ".txt", 'w')
Names_Header = "Rating" + ";" + "Year" + ";" + "Date" + ";" + "Player" + ";" + "Salary" + \
    ";" + "Position" + ";" + "Bat_Order" + ";" + "Opp_Pitcher" + ";" + "Opp" + "\n"
Names.write(Names_Header)

Player_Data = open("Player_Stats_2021" + ".txt", 'w')
Player_Stat_Header = "Empty"+';'+"Team" + ';' + "Opponent" + ';' + "Empty2" + ';' + "Empty3" + ";" + "wOBA" + ";" + "wOBA_Diff" + ";" + "ISO" + ";" + "ISO_Diff" + ";" + "SLG" + ";" + "SO/AB" + ";" + "HR/AB" + ';' + "SB/G" + ";" + "Pro" + ";" + "My" + ";" + "Ump" + ";" + "Bargain" + ";" + "ParkRank" + ";" + "Runs" + ";" + "Opp_Run" + ";" + "Delta" + ";" + "ML" + ';' + "OU" + ";" + "ML%" + ";" + "Temp" + ";" + "Rating" + ";" + "WindSpd" + ";" + "WindDir" + ";" + "Humidity" + ";" + "Adv15_Cnt" + ";" + "Adv15_Dist" + ";" + "Adv15_EV" + ";" + "Adv15_FB" + ';' + "Adv15_GB" + ";" + "Adv15_LD" + ";" + "Adv15_HH" + ";" + \
    "Adv15_DistDelta" + ";" + "Adv15_EVDelta" + ";" + "Adv15_HHDelta" + ";" + "Adv15_Air" + ";" + "AdvYear_Cnt" + ";" + "AdvYear_Dist" + ";" + "AdvYear_EV" + ";" + "AdvYear_FB" + ";" + "AdvYear_GB" + ";" + "AdvYear_LD" + ";" + "AdvYear_HH" + ";" + "AdvYear_GB/FB"+';'+"AdvYear_Air" + ";" + "FantYear_PPG" + ";" + \
    "FantYear_Change" + ";" + "FantYear_PlusMinus" + ";" + "FantYear_Consist" + ";" + "FantYear_Upside" + ";" + "FantYear_Duds" + ";" + "FantYear_Count" + \
    ";" + "FantMonth_PPG" + ";" + "FantMonth_Change" + ";" + "FantMonth_Consist" + \
    ";" + "FantMonth_Upside" + ";" + "FantMonth_Duds"+';'+"FantMonth_Count"+"\n"
Player_Data.write(Player_Stat_Header)

# https://www.fantasylabs.com/mlb/player-models/?date=05-20-2022


# https://www.fantasylabs.com/account/login/
url = "https://www.fantasylabs.com/account/login/"
# driver = webdriver.PhantomJS(executable_path="C:/Users/Tom/Downloads/phantomjs-2.0.0-windows/phantomjs-2.0.0-windows/bin/phantomjs")
driver.get(url)
time.sleep(3)

# Find and fill in username/password

username = driver.find_element(By.NAME, 'input')
password = driver.find_element(By.NAME, 'password')
username.send_keys('thomas.booth@thedarkstargroup.com')
password.send_keys('PKPcgr0055')

# Find and click on the submit button
login_attempt = driver.find_element(By.CLASS_NAME, "pull-right")
login_attempt.click()


# wait 10 seconds for web page to load
time.sleep(5)


for i, x in zip(dates['dates'], dates['year']):
    iter_date = "date: {}, year= {}".format(i, x)
    print(iter_date)
    # Find and fill in username/passwor
    link = "https://www.fantasylabs.com/mlb/player-models/?date=" + i
#  Find and click the Player Models tab
#  Find and click the Player Models tab

    current = driver.get(link)
    time.sleep(3)
    driver.maximize_window()

    # For convenience
    is_loaded = EC.presence_of_element_located

    # Paths to target div containers
    data_path = "//div[@class='ag-body-container']/div"
    name_path = "//div[@class='ag-pinned-cols-container']/div"

    script = "return arguments[0].scrollIntoView();"

    # Exceptions we'll need to handle for robustness
    exceptions = (StaleElementReferenceException, WebDriverException)
    timeout = 20

    last_row = -1  # Row tracker
    last_div = None

    Year = str(x)
    date_str = str(i)
    # Format template for name output
    template = ';'.join(['{}', Year, date_str, '{}', '{}', '{}', '{}', '{}', '{}'])

    # To strip out not printable chars...encoding/decoding
    # just didn't work for me.
    import re
    rep = re.compile('[^\x00-\x7F]+')

    # Allows us to add null strings where they should be
    f = (lambda x: x.string if x.string else "")

    try:
        # count < 5:
        myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, "ag-row ag-row-even ag-row-level-0")))
        driver.execute_script("scrollBy(0,500);")
        sleep(randint(1,3))
        list_of_completed_urls.append(url)
            #count += 1
            #driver.refresh()
        #else:
            #pass
    except TimeoutException:
        pass

    name_divs = driver.find_elements(By.XPATH, name_path)
    if name_divs == []:
        gam = "No Games on Date: {}".format(x)
        print(gam)
        pass
    else:

        while True:

            # Break if last div processed

            # If we've scrolled, we use this xpath as a baseline. See
            # next comment...
            starting_div = data_path + "[@row='" + str(max(last_row, 0)) + "']"

            try:
                # Either this is our first pass, or we've scrolled;
                # if the last processed div is loaded after a scroll,
                # then any new divs should be loaded as well, good to go
                condition = is_loaded((By.XPATH, starting_div))
                WebDriverWait(driver, timeout).until(condition)

            finally:
                # Get next batch of rows for each side of table
                name_divs = driver.find_elements(By.XPATH, name_path)
                data_divs = driver.find_elements(By.XPATH, data_path)

            # If we've already seen the last div in a batch, we're done
            if data_divs[-1] == last_div:
                break

            # Iterate on names and data rows together
            for dt_div, nm_div in zip(data_divs, name_divs):
                stale = True  # Assume stale reference
                t = 1  # Timeout counter

                # While allows recovery of stale div element
                while stale and t <= timeout:
                    try:
                        row = int(dt_div.get_attribute('row'))

                        # Just make sure row indices agree
                        assert row == int(nm_div.get_attribute('row'))

                        # Ignore rows we've already seen
                        if row <= last_row:
                            break
                        else:
                            pass

                        # # Parse only if respective div texts are exposed
                        if dt_div.is_displayed() and nm_div.is_displayed():

                            # Parse the data rows and write out; beautiful soup
                            # provides the simplest way to account for null string
                            name = bsoup(nm_div.get_attribute(
                                "outerHTML")).strings
                            div = bsoup(dt_div.get_attribute("outerHTML"))

                            data = [rep.sub('', f(x))
                                    for x in div.find_all('div')]
                            Names.write(template.format(*list(name)) + '\n')
                            Player_Data.write(';'.join(list(data)) + '\n')

                            # Update info on last processed div
                            last_row = row
                            last_div = dt_div

                        # Element was valid and processed, let's move on
                        stale = False

                    # Stale nut, wait a second and retry
                    except exceptions as e:
                        print('Something went wrong', e.args)
                        sleep(1)
                        t += 1
                stale = True
                t = 1

                # Handles issues with page scrolling
                while stale and t <= timeout:

                    try:
                        # Use last div processed as a reference point
                        # for scrolling
                        driver.execute_script(script, last_div)
                        stale = False

                    except exceptions as e:
                        sleep(1)

                        if t == timeout:
                            err = 'Oops! Scrolling stopped working at row: {}\n{}'
                            print(err.format(str(last_row), str(e.args)))
                        t += 1

            # Names.close()
            # Player_Data.close()

            ans = 'n'

            time.sleep(3)
            # while ans != 'y':
            #	ans = raw_input('Quit WebDriver? (y/n): ')

Names.close()
Player_Data.close()
driver.quit()
