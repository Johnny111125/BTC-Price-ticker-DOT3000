Display Bitcoin Price on Display-o-Tron 3000

This script displays the current price of Bitcoin on a Display-o-Tron 3000 with a red background. The price is updated every 30 seconds.
Prerequisites

    A Display-o-Tron 3000
    A Raspberry Pi
    Python 3
    The requests library: pip3 install requests
    The dothat library: pip3 install dothat

Running the script

To run the script, navigate to the directory where the script is saved and run the following command:

python3 script.py

The script will run in an infinite loop, updating the price of Bitcoin and refreshing the LCD screen every 30 seconds.
Resources

    CoinDesk Bitcoin Price Index (BPI) API: https://www.coindesk.com/api
    Display-o-Tron 3000 documentation: https://learn.pimoroni.com/tutorial/sandyj/getting-started-with-displayotron
