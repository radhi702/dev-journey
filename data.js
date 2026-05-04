let customers = [
    {name: "Rahul", email: "rahul@gmail.com", plan: "premium"},
    {name: "priya", email: "priya@gmail.com", plan: "free"},
    {name: "Harsh", email: "harsh@gmail.com", plan: "premium"},
    {name: "Raj", email: "raj@gmail.com", plan: "free"}, 
];

for (let i = 0; i < customers.length; i++) {
    console.log(customers[i].name);
}

let premiumCustomers = customers.filter(function(customer) {
    return customer.plan === "premium";
});

console.log("premium customers: " + premiumCustomers.length);
console.log(premiumCustomers);


