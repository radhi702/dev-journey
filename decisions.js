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

let persons = ["Rai", "billie", "Vegas", "Tinni"];

for (let i = 0; i < persons.length; i++) { 
    console.log("Helo " + persons[i]);

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
greetcustomer("Bunny", "free")
    


// creating dictionary

let singlecustomer = {
    name: "Radhika",
    email: "radhika@gmail.com",
    plan: "premium",
    active: "true"
};

console.log(singlecustomer.name)
console.log(singlecustomer["name"])
 
// list of dictionaries

let customers = [
    {name: "Priya", plan: "premium"},
    {name: "Rahul", plan: "free"},
    {name: "Yash", plan: "premium"}
];

let premium = customers.filter(c => c.plan === "premium");
console.log("Premium customers", premium.length)

// functions that returns a value

function calculatediscount(price, plan) {
    if (plan === "premium") {
        return price * 0.8;
    } else {
        return price;
    }
    }

let originalprice = 1000;
let finalprice = calculatediscount(originalprice, "premium");
console.log("finalprice: " + finalprice);