import requests

from Scraper import Scraper

url = "https://marseif2.pythonanywhere.com/revs"
reviews = requests.get(url).json()

for review in reviews:
    scraper = Scraper()
    scraper.email = review['email']
    scraper.first_name = review['first_name']
    scraper.last_name = review['last_name']
    scraper.review_title = review['review_title']
    scraper.review = review['review']
    scraper.service = review['service']
    scraper.job = review['job']
    scraper.post_code = review['post_code']
    scraper.tlf = review['phone_number']
    scraper.business = review['business']
    scraper.quality = review['quality']
    scraper.reliability = review['reliability']
    scraper.courtesy = review['courtesy']
    scraper.tidiness = review['tidiness']

    #scraper.add_review_checkatrade()
    scraper.add_review_yell()
    requests.get(f"https://marseif2.pythonanywhere.com/delete/{review['id']}")

