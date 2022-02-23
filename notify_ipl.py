import time
import argparse
import pickle

"""
Add this to your .bashrc file to be notified every week when you need to do IPL.
I chose a 6 day period so I have a heads up one day early.
You should also create an alias. For example I added these lines:
alias ipl="python3 /home/taylor/Software/notify_ipl/notify_ipl.py"
python3 /home/taylor/Software/notify_ipl/notify_ipl.py -q

This code is CC0 licensed, aka public domain. Use this code for any purpose.
Created by Taylor Alexander
"""


NOTIFY_DAYS = 6
DAY_SECONDS = 24 * 60 * 60
DATE_FILE = "/home/taylor/Software/notify_ipl/dates.pkl"


IPL_TIME =(
""" ___ ____  _       _____ ___ __  __ _____
|_ _|  _ \| |     |_   _|_ _|  \/  | ____|
 | || |_) | |       | |  | || |\/| |  _|
 | ||  __/| |___    | |  | || |  | | |___
|___|_|   |_____|   |_| |___|_|  |_|_____|
""")


parser = argparse.ArgumentParser(description='Notify me when I need to do IPL.')
parser.add_argument('-q', '--quiet', action='store_true', help='Only print if it is time to do IPL')
parser.add_argument('-c', '--chest', action='store_true', help='Update the chest IPL date to today.')
parser.add_argument('-j', '--junk', action='store_true', help='Update the junk IPL date to today.')
parser.add_argument('-l', '--legs', action='store_true', help='Update the legs IPL date to today.')
args = parser.parse_args()

try:
    with open(DATE_FILE,'rb') as f:
        dates = pickle.load(f)
except:
    dates = {
    'chest':time.time(),
    'junk':time.time(),
    'legs':time.time()
    }

if args.chest:
    dates['chest'] = time.time()
if args.junk:
    dates['junk'] = time.time()
if args.legs:
    dates['legs'] = time.time()

with open(DATE_FILE,'wb') as f:
    pickle.dump(dates, f)

output = ""
notify = False

for key, value in dates.items():
    diff = time.time() - value
    diff_days = int(diff/DAY_SECONDS)
    if diff_days >= NOTIFY_DAYS:
        notify = True
    if args.quiet:
        if diff_days >= NOTIFY_DAYS:
            output += "| {} {} days |".format(key, diff_days)
    else:
        output += "| {} {} days |".format(key, diff_days)
if notify:
    print(IPL_TIME)
if len(output) > 1:
    print(output)
