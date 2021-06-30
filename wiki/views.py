from django.shortcuts import render
import random
import requests
from requests.adapters import HTTPAdapter

from bs4 import BeautifulSoup as BSoup
from django.shortcuts import redirect
from wiki.models import Article

# import re    #regex library

requests.packages.urllib3.disable_warnings()

#scraping function using classic django
def scrape(url):

	response = requests.get(
		url=url,
	)
	session = requests.Session()
	session.mount('https://en.wikipedia.org', HTTPAdapter(max_retries=5))
	soup = BSoup(response.content, 'html.parser')
	title = soup.find(id="firstHeading")
	# print(title.text)
	article = soup.find(id="bodyContent").find_all("a")
	random.shuffle(article)
	linkToScrape = 0

	for link in article:
		# random wiki articles
		linkToScrape = link
		topics = Article()
		urlLink =("https://en.wikipedia.org" + linkToScrape['href'])
		# title =linkToScrape.title
		topics.url = urlLink
		title = linkToScrape.get_text()
		print(title)
		print(urlLink)
		topics.title = title
		topics.save()
		break
	scrape("https://en.wikipedia.org" + linkToScrape['href'])
	return redirect("../")

# scrape("https://en.wikipedia.org/wiki/Main_Page")

def news_list(request):
	headlines = Article.objects.all()[::-1]
	# headlines = Article.objects.all()[0:100]
	context = {
		'object_list': headlines,
	}
	return render(request, "wiki/home.html", context)