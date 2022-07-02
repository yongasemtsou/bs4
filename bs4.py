import requests
r=requests.get('https://www.sciencedirect.com/search?qs=Diagnosing%20Lung%20disease%20Conditions%20in%20Bovines')
print(dir(r))