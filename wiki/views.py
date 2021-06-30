from django.shortcuts import render
import random
import requests
from requests.adapters import HTTPAdapter

from bs4 import BeautifulSoup as BSoup
from django.shortcuts import redirect
from wiki.models import Article, Visitor
from wiki.serializers import VisitorSerializer

from rest_framework import serializers, viewsets
# import re    #regex library

from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from wiki.forms import VisitorForm

class VisitorListView(ListView):
    model = Visitor
    context_object_name = 'people'


class VisitorCreateView(CreateView):
    model = Visitor
    fields = ('name', 'email', 'job_title', 'bio')
    success_url = reverse_lazy('person_list')


class VisitorUpdateView(UpdateView):
    model = Visitor
    form_class = VisitorForm
    template_name = 'wiki/visitor_update_form.html'
    success_url = reverse_lazy('person_list')



class VisitorViewset(viewsets.ModelViewSet):
    queryset = Visitor.objects.all()
    model = Visitor
    serializers = VisitorSerializer



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

# def news_list(request):
# 	headlines = Article.objects.all()[::-1]
# 	# headlines = Article.objects.all()[0:100]
# 	context = {
# 		'object_list': headlines,
# 	}
# 	return render(request, "wiki/home.html", context)