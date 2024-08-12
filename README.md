# Public-Mobile-Referral-List-Checker
This Python script checks a specific Reddit page to see if a particular text is present. Initially developed to monitor updates on the /r/PublicMobile Referral List, the script can be easily customized to track any text on any Reddit page. By scraping the page at regular intervals, it helps you stay informed without manual checks.

## Features

- Scrapes a Reddit page for specific text.
- Prints a message to the command line if the text is found or not found.
- Configurable check interval for periodic monitoring.

## Prerequisites

Before you can run the script, you'll need to install the following Python libraries:

- `requests`
- `beautifulsoup4`

You can install these dependencies using pip:

```bash
pip install requests beautifulsoup4
