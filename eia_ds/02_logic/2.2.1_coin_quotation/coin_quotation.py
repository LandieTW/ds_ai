"""code a script that converts some BRL quantity to another coin value"""

# INSTRUCTIONS

"""
1 - Inputs BRL value to convert
2 - Inputs the coin iddentification as examplified in list 'coins'

Obs.:
    1 - Site information may change (button_class and value_class)
"""

# LIBS

import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# CONSTANTS

coins = ['EUR', 'USD', 'GBP', 'JPY', 'CHF', 'AUD', 'CNY', 'CAD', 'BRL']
link = 'https://br.tradingview.com/markets/currencies'
this_path = os.path.dirname(__file__)
driver_path = os.path.join(this_path, "Edge\\msedgedriver.exe")
options = webdriver.EdgeOptions()
options.use_chromium = True
options.add_argument('--headless')
options.add_argument('--disable-gpu')
button_class = "items-IJWxYDAe"
value_class = "last-JWoJqCpY"

# INPUTS

value_convert = float(input(f"Input BRL quantity to convert (float or int): \n"))
coin_convert = str(input(f"Input one option to convert BRL in: {coins} \n"))
text = coin_convert + " para BRL"

# METHODS



# CODE

# driver = webdriver.Edge(executable_path=driver_path, options=options)
driver = webdriver.Edge(service=webdriver.edge.service.Service(driver_path), options=options)

try:
    driver.get(link)
    time.sleep(5)

    div = driver.find_element(By.CLASS_NAME, button_class)
    links = div.find_elements(By.TAG_NAME, "a")

    for link in links:
        if text in link.text:
            link.click()
            time.sleep(5)
            break

    span = driver.find_element(By.CLASS_NAME, value_class)
    rate = span.text.split()[0] 
    print(f"{coin_convert} x BRL rate: {rate}")
    value = float(rate.replace(',', '.')) * value_convert
    print(f"{value_convert} BRL = {value} {coin_convert}")

finally:
    driver.quit()
