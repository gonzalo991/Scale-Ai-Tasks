/*
function isValidEmail(email) {
    // Creates a regular expression from a constructor since ES6
    let regex = new RegExp(/\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,6}\b/);

    // Validate if there's a coincidence and return a boolean
    if (email.match(regex)) {

        return regex.test(email);

    } else {

        return false;

    }
}


const email = 'valid_email934@example.another.com.ar';
const isValid = isValidEmail(email);

console.log(isValid); // true



function isValidEmail(email) {
    // Creates a regular expresion
    let regex = new RegExp(/\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,6}\b/);

    //Validate if the parameter is an array
    if (Array.isArray(email)) {
        for (let i = 0; i < email.length; i++) {
            if (!regex.test(email[i])) {
                return false;
            }
        }
        return true;
    } else {
        // Test if there's a match and returns a boolean
        return regex.test(email);
    }
}

const emails = ['valid_email@example.com', 'another_valid_email@example.com'];
const isValid = isValidEmail(emails);

console.log(isValid); // true
*/

function isValidEmail(email) {
    // Creates a regular expresion
    let regex = new RegExp(/\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,6}\b/);

    // If the parameter is an array, then we validate each email in the array
    if (Array.isArray(email)) {
        let results = []; // Create an empty array to store the valid emails

        try {
            for (let i = 0; i < email.length; i++) {
                // If the email is valid, then we add it to the results array
                if (regex.test(email[i])) {
                    results.push(email[i]);
                } else {
                    console.log(`Invalid email detected: ${email[i]}`);
                    return false;
                }
            }
        } catch (error) {
            console.error(error);
        } finally {
            // Return the results array
            return results;
        }
    } else {
        // Test if there's a match and returns a boolean
        return regex.test(email);
    }
}

const emails = ['valid_email@example.com', 'another_valid_email@example.com'];
const isValid = isValidEmail(emails);

console.log(isValid);