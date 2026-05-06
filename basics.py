# conditionals
plan = "premium"

if plan == "premium":
    print("Send VIP email")
elif plan == "free":
    print("Send upgrade offer")
else:
    ("unknown plan")


# loops
customers = ["Radhika", "Gavy", "Ravi", "Nari"]

for customer in customers:
    print("Hello " + customer)


# functions
def greetcustomer(name, plan):
    if plan == "premium":
        print("Welcome VIP " + name)
    else:
        print("Welcome " + name)

greetcustomer("Anny", "premium")
greetcustomer("fredick", "free")


# creating dictionary
customer = {
    "name": "Radhika",
    "email": "radhika@gmail.com",
    "plan": "premium",
    "active": "True"
}

# accessing values
print(customer["name"])
print(customer["plan"])

# adding new keys
customer["age"] = 20
print(customer)

# updating existing keys
customer["plan"] = "free"
print(customer["plan"])

# looping through dictionary
for key in customer:
    print(key + " : " + str(customer[key]))
    

# list of dictionary
customers = [
    {"name": "Radhika", "plan": "premium"},
    {"name": "Priya", "plan": "free"},
    {"name": "Amit", "plan": "premium"}
]

# get all premium customers
premium = []
for customer in customers:
    if plan == "premium":
        premium.append(customer)

print("Premium customers:", len(premium))
for p in premium:
    print(p["name"])

# functions that returns a value

def calculate_discount(price, plan):
    if plan == "premium":
        return price * 0.8      # 20% discount
    else:
        return price

# using the returned value
original_price = 1000
final_price = calculate_discount(original_price, "premium")
print("final_price:" + str(final_price))

