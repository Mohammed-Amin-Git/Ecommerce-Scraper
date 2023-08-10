from bs4 import BeautifulSoup
import requests
import re

class Proxies:
	def __init__(self):
		self.all_proxies = []
		self.working_proxies = []

	# Fetching proxy ip addresses from www.sslproxies.org, Filtering using RegEx.
	def fetch_proxies(self):
		self.all_proxies = re.findall("\d+\.\d+\.\d+\.\d+:\d+", requests.get("https://www.sslproxies.org/").text)

	# Testing if proxy server is working
	def test_proxy(self, proxy_url):
		try:
			res = requests.get("http://ipinfo.io/json", proxies = {
					"http": proxy_url,
					"https": proxy_url
				}) 
			return True
		except:
			return False

	# Filtering for only working proxies
	def filter_working_proxies(self):
		self.working_proxies = filter(self.test_proxy, self.all_proxies)

proxies = Proxies()
proxies.fetch_proxies()
proxies.filter_working_proxies()

print(proxies.all_proxies)
print("\n\n\n")
print(list(proxies.working_proxies))