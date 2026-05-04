let response = await fetch("https://api.github.com/users/radhi702/repos");
let repos = await response.json();

console.log("Total repos: " + repos.length);

for (let i = 0; i < repos.length; i++) {
  console.log(repos[i].name + " - " + repos[i].visibility);
  }
