 const fs = require('fs');

  fs.writeFileSync('hello.txt', 'Line 1: Hello!\n');

  fs.appendFileSync('hello.txt', 'Line 2: This was added later\n');

  fs.appendFileSync('hello.txt', 'Line 3: And this too!\n');

  const content = fs.readFileSync('hello.txt', 'utf8');

  console.log(content);