// conditionals

let plan = "premium"; 

if (plan === "premium") {
    console.log("Send VIP email");
} else if (plan === "free") {
    console.log("Send upgrade offer")
} else {
    console.log("unknown plan")
}



// loops

let customers = ["Rai", "billie", "Vegas", "Tinni"];

for (let i = 0; i < customers.length; i++) { 
    console.log("Helo " + customers[i]);

}

// functions

function greetcustomer(name, plan) {
    if (plan === "premium") {
        console.log("Welcome VIP " + name);
    } else {
        console.log("Welcome " + name);
        }
    }

greetcustomer("Honey", "premium")
greetcustomer("Bunny" + "free")
    


// creating dictionary

let customer = {
    name: "Radhika",
    email: "radhika@gmail.com",
    plan: "premium",
    active: "true"
};

console.log(customer.name)
console.log(customer["name"])
 
// list of dictionaries

let customers = [
    {name: "Priya", plan: "premium"},
    {name: "Rahul", plan: "free"},
    {name: "Yash", plan: "premium"}
];

let premium = customers.filter(c => c.plan === "premium");
console.log("Premium customers", premium.length)