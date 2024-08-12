import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime

def send_discord_message(webhook_url, message):
    data = {"content": message}
    response = requests.post(webhook_url, json=data)
    if response.status_code == 204:
        print("Message sent successfully to Discord.")
    else:
        print(f"Failed to send message to Discord. Status code: {response.status_code}")

def check_text_in_reddit_page(url, text_to_find, webhook_url, current_datetime, mention):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        page_text = soup.get_text()
        
        if text_to_find in page_text:
            message = f"{current_datetime} | STATUS | Your referral code {text_to_find} is still on the list."            
        else:
            message = (
                f"{current_datetime} | ALERT | {mention} Your referral code '{text_to_find}' is NOT on the list.\n"
                f"Please renew your code here: https://www.reddit.com/message/compose/?to=pmreferralbot&subject=Renewal&message={text_to_find}")
        send_discord_message(webhook_url, message)
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")

# URL of the Reddit page
url = "https://old.reddit.com/r/PublicMobile/wiki/referrals-nextmonth"
# Referral code to find on the list
text_to_find = "XXXXXX"
# Your Discord webhook URL
webhook_url = "https://discord.com/api/webhooks/XXXXXXXXXXXXXX/XXXXXXXXXXXXXXXXXXXXXX-XXXXXXXXXXXX-XXXXXXXXXXXXXX/XX-XX/XXXXXXXXXXXXXXXXXX"
# Your discord user ID
mention = "<@XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX>"  

# Loop to check periodically
while True:
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M")
    check_text_in_reddit_page(url, text_to_find, webhook_url, current_datetime, mention)
    # Wait for 6 hours (21,600 seconds) before checking again
    time.sleep(21600)
