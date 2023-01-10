import os
import time
import requests
import dothat.lcd as lcd

while True:
    # Set the background color to red
    lcd.set_backlight_rgb(255, 0, 0)

    # Get the current price of Bitcoin in USD
    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice/BTC.json')
    price = r.json()['bpi']['USD']['rate']

    # Clear the LCD and display the price
    lcd.clear()
    lcd.write(price)

    # Wait 30 seconds before updating the price again
    time.sleep(30)
