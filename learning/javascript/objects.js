const phone = {
    brand: "Samsung",
    model: "Samsung S21",
    price: 25000
};
console.log(phone)

const laptop = {}
laptop.brand = "HP"
laptop.ram = "8GB"

console.log(laptop)

// Accessing Values — Dot vs Bracket Notation
// Two ways to get a value from an object:

const car = { 
    Brand: "Toyota",
    model: "Innova",
    year: 2025
};

// Way 1: Dot notation
console.log(car.Brand);

// Way 2: Bracket notation
console.log(car["model"]);

// When you MUST use brackets — key is stored in a variable
const key = "year";
console.log(car[key]);
