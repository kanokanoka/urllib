import urllib.request

# read and 200 byte print
with urllib.request.urlopen('http://www.google.com') as gurl:
	print(gurl.read(200))

