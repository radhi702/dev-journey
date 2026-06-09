// -----Arrays in depth------ //

// forEach
const fruits = [ "apple", "grapes", "banana", "cherry", "mango"];

fruits.forEach(function(fruit) {
    console.log(fruit);
});

fruits.forEach(function(fruit, index) {
    console.log(index + "->" + fruit);
});

// map

const articles = ["AI takes over coding", "Bitcoin hits 100k", "India wins World Cup"];

articles.forEach(function(article) {
    console.log(article);
});

articles.forEach(function(article, index) {
    console.log(index + "->" + article);
});

const prices = [100, 200, 3000, 500];

const doubled = prices.map(function(price) {
    return price * 2
});
console.log("Original prices", prices);
console.log("Doubled prices", doubled);

const withrupee = prices.map(function(price) {
    return "₹" + price;
});
console.log(withrupee)

const rawNames = [ " radhika " , "AMIT", "  priya "];
const cleanNames = rawNames.map(function(names)  {
    return names.trim().toLowerCase();
});
console.log("Before cleaning", rawNames);
console.log("After cleaning", cleanNames);

// filter

const numbers = [100, 130, 70, 50];
const bigNumbers = numbers.filter(function(num) {
    return num > 10;
});
console.log("Big numbers", bigNumbers);

// reduce

scores = [10, 20, 30, 40]
const total = scores.reduce(function(acc, score) {
    return acc + score
}, 0);
console.log("Total score:", total);


/// we can replace function word in every method with arrow =>

//const tripled = prices.map((price) => price * 2);
//console.log("Tripled:", tripled);

 // Chaining — using filter + map together
  // First filter expensive items, then add rupee symbol
const expensiveFormatted = prices
    .filter((price) => price >= 500)
    .map((price) => "₹" + price);
console.log("Expensive formatted:", expensiveFormatted);