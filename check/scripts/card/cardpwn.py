
import os
import sys
import requests
from googlesearch import search

def cardpwn(card_number):
	urls = []
	qlist = []
	total_url = []
	paste_sites = ['cl1p.net', 'dpaste', 'dumpz.org', 'hastebin', 'ideone', 'pastebin', 'pw.fabian-fingerle.de','gist.github.com','https://www.heypasteit.com/','ivpaste.com','mysticpaste.com','paste.org.ru','paste2.org','sebsauvage.net/paste/','slexy.org','squadedit.com','wklej.se','textsnip.com']
	card = card_number
	try:
		val = int(card)
		if len(str(val)) >= 12 and len(str(val)) <= 19:
			for site in paste_sites:
				query = '{} {}'.format(site, card)
				qlist.append(query)
			for entry in qlist:
				for url in search(entry, pause=2.0, stop=20, user_agent='Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0'):
					urls.append(url)

			for item in urls:
				for site in paste_sites:
					if '{}'.format(site) in item:
						total_url.append(item)

		else:
			return {'error': 'Invaild Card Number'}

		total = len(total_url)
		if total == 0:
			return {'leaks': []}
		else:
			return { 'leaks': total_url, 'total': total }

	except ValueError:
		return {'error': 'Invaild Card Number Entered...'}
