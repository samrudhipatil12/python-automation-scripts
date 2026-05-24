import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    try:
        # Send request
        response = requests.get(url)
        response.raise_for_status()

        # Parse HTML
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract data
        title = soup.title.string if soup.title else "No title found"

        print("Website URL:", url)
        print("Page Title:", title)

    except Exception as e:
        print("Error:", e)


# Run program
if __name__ == "__main__":
    website = input("Enter website URL: ")
    scrape_website(website)
