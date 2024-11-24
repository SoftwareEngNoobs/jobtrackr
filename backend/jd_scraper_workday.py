import requests
from bs4 import BeautifulSoup

headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }

def get_job_description(job_url):
        try:
            response = requests.get(job_url)
            soup = BeautifulSoup(response.text, 'html.parser')
            descriptions = soup.findAll('meta')
            descriptions = [desc for desc in descriptions if desc.get("property", None) not in ["og:title","og:type","og:url","og:image"]]
            if descriptions:
                content = [desc["content"] for desc in descriptions]
                return content[3:]
        except Exception as e:
            print(f"Error fetching job description: {e}")
            return "Failed to get job description."