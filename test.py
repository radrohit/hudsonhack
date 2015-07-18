#http://api.donorschoose.org/common/json_feed.html?state=NC&community=10007:3&APIKey=DONORSCHOOSE
#importing modules
from urllib2 import Request, urlopen, URLError
import urllib
import json

#url data
url_string = "http://api.donorschoose.org/common/json_feed.html?state=%s&community=%s&APIKey=DONORSCHOOSE" % ("NC","10007:3")
main_url = "http://api.donorschoose.org/common/json_feed.html"
values ={
         'APIKey': "DONORSCHOOSE",
         'max':'50',
         'index': '0'
}


# getting the json value
data= urllib.urlencode(values)
request = Request(main_url,data)
response = urlopen(request)
website_data = json.loads(response.read())

for proposal in website_data['proposals']:
    print proposal['fulfillmentTrailer']
