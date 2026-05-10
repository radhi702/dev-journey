import requests

try:
    response = requests.get("https://api.github.com/users/radhi702")
    data = response.json()
    print("Success Username: ", data["login"])

except Exception as error:
    print("Something went wrong, error")

## force an error to see it is working

try:
    response = requests.get("https://api.github.com/users/THISUSERDOESNOTEXIST99999")
    data = response.json()

    if response.status_code == 404:
        print("User not found!")
    else:
        print("Succes! Username: ", data["login"])

except Exception as rror:
    print("Something went wrong, error")

# specific error types in python

try:
    response = requests.get("https://api.github.com/users/radhi702")
    data = response.json()
    print(data["login"])

except requests.ConnectionError:
    print("No internet connection")

except TimeoutError:
    print("Request took too long!")

except KeyError:
    print("EXpected key is not found in response!")

except Exception as error:
    print("Unknowm error: ", error)

# finally block - always run

try:
    response = requests.get("https://api.github.com/users/radhi702")
    data = response.json()
    print("Success!")

except Exception as error:
    print("Failed : ", error)

finally:
    print("This always runs - Success or Failure")