import json
import requests

# Working with JSON Data in Python
def jprint(jsObj):
    # create a formatted string of the Python JSON object
    text = json.dumps(jsObj, sort_keys=True, indent=4)
    print(text)

response1 = requests.get("http://api.open-notify.org/astros.json")
# printing readable text of the people currently in space
# jprint(response1.json())

# Using an API Query Parameters

# You can directly add parameters into the URL like this:
# http://api.open-notify.org/iss-pass.json?lat=40.71&lon;=-74
# But it's almost always preferable to setup the parameters as a
# dictionary, because requests takes care of some things that come up,
# like properly formatting the query parameters, and we don't need to 
# worry about inserting the values into the URL string.
parameters = {
    "lat": 40.71,
    "lon": -74
}

response2 = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)
# jprint(response2.json())

# Let’s extract the pass times from our JSON object: 
pass_times = response2.json()['response']
jprint(pass_times)

risetimes = []

for d in pass_times:
    time = d['risetime']
    risetimes.append(time)

print(risetimes)