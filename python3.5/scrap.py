from bs4 import BeautifulSoup
import urllib.request
import random

def scrap():
	# Pick random surah
	surah =  (random.randint(1, 114))
	
	# Set URL
	url = 'https://quran.com/' + str(surah)
	
	# Request URL
	r = urllib.request.urlopen(url).read()

	# Use soup
	soup = BeautifulSoup(r,"html.parser")

	# Find all ayah
	smalltag = soup.find_all("small")
	
	# Pick random ayah
	ayah = random.randint(0, (len(smalltag) - 1))

	return ("\"" + smalltag[ayah].string + "\" [" + str(surah) + ":" + str(ayah + 1) + "]")


