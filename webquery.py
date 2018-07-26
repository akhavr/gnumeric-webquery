from Gnumeric import GnumericError, GnumericErrorVALUE
import Gnumeric
import string

import urllib2
import json

def xpath_get(mydict, path):
    elem = mydict
    try:
        for x in path.strip("/").split("/"):
            elem = elem.get(x)
            if type(elem) is list:
                elem = elem[0] # no index support now
    except:
        pass

    return elem

def ImportJSON(url, xpath, ignore, **kwargs):
    f = urllib2.urlopen(url)
    j = json.loads(f.read())
    res = xpath_get(j, xpath)
    return float(res)


webquery_functions = {
    'ImportJSON': ('sss', 'url,xpath,flag', ImportJSON),
}
