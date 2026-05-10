import requests

response = requests.get("https://api.github.com/users/radhi702")

data = response.json()

print(data)
print("Name: ", data["login"])
print("Public repos: ", data["public_repos"])
print("Status code: " , response.status_code)
