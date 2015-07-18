#http://api.donorschoose.org/common/json_feed.html?state=NC&community=10007:3&APIKey=DONORSCHOOSE
#importing modules
from urllib2 import Request, urlopen, URLError
import urllib

#url data
url_string = "http://api.donorschoose.org/common/json_feed.html?state=%s&community=%s&APIKey=DONORSCHOOSE" % ("NC","10007:3")
main_url = "http://api.donorschoose.org/common/json_feed.html"
values ={'state': 'NC',
         'community': "10007:3",
         'APIKey': "DONORSCHOOSE"
}

# getting the json value
data= urllib.urlencode(values)
request = Request(main_url,data)
response = urlopen(request)
print response.read()
