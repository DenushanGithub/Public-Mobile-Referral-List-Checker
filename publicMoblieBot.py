import requests
from bs4 import BeautifulSoup
import time

def check_text_in_reddit_page(url, text_to_find):
    # Send a GET request to the URL
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    response = requests.get(url, headers=headers)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the page content
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Get the text content of the page
        page_text = soup.get_text()
        
        # Check if the specified text is in the page
        if text_to_find in page_text:
            print(f"The referral code '{text_to_find}' is on the list.")
        else:
            print(f"The referral code '{text_to_find}' is Not on the list. Please send a message to u/pmreferralbot to renew")
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")

# URL of the Reddit page
url = "https://old.reddit.com/r/PublicMobile/wiki/referrals-nextmonth"
# Public Mobile referral code
text_to_find = "XXXXXX"

# Loop to check periodically
while True:
    check_text_in_reddit_page(url, text_to_find)
    # Wait for 6 hour (21,600 seconds) before checking again
    time.sleep(21600)