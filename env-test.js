
  require('dotenv').config();

  const name = process.env.MY_NAME;
  const city = process.env.MY_CITY;

  console.log("Name:", name);
  console.log("City:", city);