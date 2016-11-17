from scrap import scrap
import urllib.request, urllib.error
from gi.repository import Notify

def notification():
	# Check internet connection
	try:
		urllib.request.urlopen('https://quran.com/')
	except urllib.error.URLError:
		return 0
	
	# Notification init
	Notify.init("Ayah notification")
	
	# Create the notification object
	SUMMARY_MSG = "Ayah of the day"
	BODY_MSG	= scrap()
	
	n = Notify.Notification.new(SUMMARY_MSG, BODY_MSG)

	# Set notification timeout
	Notify.Notification.set_timeout(n, 10000)

	# Show notification on screen
	n.show()

notification()
