import requests                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    try:
        response = requests.get(url, timeout=10)  
        response.raise_for_status()  
        soup = BeautifulSoup(response.text, 'html.parser')
        text_content = soup.get_text(separator=' ', strip=True)  
        return text_content
    except requests.exceptions.SSLError as ssl_err:
        print(f"SSL error occurred: {ssl_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
    except Exception as e:
        print(f"An error occurred: {e}")

def answer_query(query, scraped_data):
    results = []
    for url, content in scraped_data.items():
        if query.lower() in content.lower():  
            results.append((url, content))
    return results
urls = [
    "https://www.uchicago.edu/",
    "https://www.washington.edu/",
    "https://www.stanford.edu/",
    "https://und.edu/"
]

scraped_data = {}
for url in urls:
    content = scrape_website(url)
    if content:
        print(f"Successfully scraped content from {url}")
        scraped_data[url] = content 

user_query = input("Enter your query: ")
results = answer_query(user_query, scraped_data)
if results:
    print("\nResults found:")
    for url, content in results:
        print(f"\nFrom {url}:\n{content[:200]}...")  
else:
    print("No results found for your query.")
