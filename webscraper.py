import requests
from bs4 import BeautifulSoup

# URL of Arcane's Wikipedia page
url = "https://en.wikipedia.org/wiki/Arcane_(TV_series)"

# Send a request to fetch the webpage content
response = requests.get(url)

if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all paragraph tags
    paragraphs = soup.find_all("p")

    # Find the first non-empty paragraph
    summary = ""
    for p in paragraphs:
        text = p.text.strip()
        if text:  # If the paragraph is not empty
            summary = text
            break

    if summary:
        print("📺 Arcane (Netflix Animation) - Wikipedia Summary\n")
        print(summary)
    else:
        print("No valid summary found.")

else:
    print("Failed to retrieve the Wikipedia page. Please check the URL or try again later.")

