
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse


def extract_job_text(url):
    # Check whether the URL is valid
    parsed_url = urlparse(url)

    if parsed_url.scheme not in ("http", "https") or not parsed_url.hostname:
        raise ValueError("Please enter a valid HTTP or HTTPS URL.")

    # Fetch the webpage
    response = requests.get(
        url,
        headers={"User-Agent": "Mozilla/5.0 SmartHire/1.0"},
        timeout=15
    )

    # Report HTTP errors, such as 404
    response.raise_for_status()

    # Read the HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # Remove elements that usually do not contain job details
    for element in soup(["script", "style", "noscript", "svg"]):
        element.decompose()

    # Extract readable text
    page_text = soup.get_text(separator=" ", strip=True)

    return page_text
