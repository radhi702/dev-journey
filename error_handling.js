async function getdata() {
    try {
        let response = await fetch("https://api.github.com/users/radhi702");
        let data = await response.json();
        console.log("Success Username: ", data.login);

    } catch(error) {
        console.log("Something went wrong, error.message")
    }
}

getdata();


async function getData() {
    try {
        response = await fetch("https://api.github.com/users/THISUSERDOESNOTEXIST99999");
        data = await response.json();

        if (response.status === 404) {
            console.log("User not found!");
        } else {
            console.log("Success! Username: ", data.login);
        }

    } catch (error) {
            console.log("Something went wrong:", error.message);
        } 
    }
    
    getData();


// finally block - always runs  use for safety and close the system 
async function getdata() {
    try {
        let response = await fetch("https://api.github.com/users/radhi702");
        let data = await response.json();
        console.log("Success!");

    } catch (error) {
        console.log("Failed: ", error.message);

    } finally {
        console.log("This always runs!");
    }
}

getdata();