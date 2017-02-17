import urllib.request

#python 3.5.2

# read and 200 byte print
with urllib.request.urlopen('http://www.google.com') as gurl:
	print(gurl.read(200))

print "finish"
