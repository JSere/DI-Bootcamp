import time
import requests

def get_page_load_time(url):
    """Measures the time it takes to get a complete response from a webpage."""
    start_time = time.time()
    try:
        # Send a GET request with a timeout
        response = requests.get(url, timeout=10)
        response.raise_for_status() # Raise an error for bad status codes (4xx or 5xx)
        end_time = time.time()
        
        load_time = end_time - start_time
        return load_time
    except requests.exceptions.RequestException as e:
        print(f"Failed to connect to {url}. Error: {e}")
        return None

# List of sites to test
websites = [
    "https://www.google.com",
    "https://www.ynet.co.il",
    "https://www.imdb.com"
]

print("Measuring webpage load times...\n")

for site in websites:
    elapsed_time = get_page_load_time(site)
    if elapsed_time is not None:
        print(f"Loaded {site} in {elapsed_time:.4f} seconds")