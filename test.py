#http://api.donorschoose.org/common/json_feed.html?state=NC&community=10007:3&APIKey=DONORSCHOOSE
#importing modules
from urllib2 import Request, urlopen, URLError
import urllib
import json

#url data
#url_string = "http://api.donorschoose.org/common/json_feed.html?state=%s&community=%s&APIKey=DONORSCHOOSE" % ("NC","10007:3")
main_url = "http://api.donorschoose.org/common/json_feed.html"
def get_data(main_url,values):
    data= urllib.urlencode(values)
    request = Request(main_url,data)
    response = urlopen(request)
    website_data = json.loads(response.read())
    print "working"
    return website_data

max_value = 20
proposals = []
for i in range(max_value):
    values ={
             'APIKey': "DONORSCHOOSE",
             'max':'50',
             'index': str(i*50 + 1)
    }
    website_data = get_data(main_url,values)
    for proposal in website_data['proposals']:
        proposals.append(proposal['fulfillmentTrailer'])
