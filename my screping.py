import requests

access_token=""    #enter  your access token given by facebook
graph_url = "https://graph.facebook.com/v3.3"
value= input("enter a field value: ")
post_args = "/me?fields="+ value +"&access_token=" + access_token
url = graph_url + post_args
print(url)
r = requests.get(url)
print(r.text[:])
#

# import urllib.request
# response = urllib.request.urlopen('http://www.utu.ac.in/')
# html = response.read()
# text = html.decode()
# print(text)