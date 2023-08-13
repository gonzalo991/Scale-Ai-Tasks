/**
 generate code in javascript using node js to make a controller which get the list of all the employees 
 of the software department with its _id, name, surname, department, start_date and age from the mongoDB database 
 called company_employees

Here is a sample code in JavaScript using Node.js to retrieve the list of all employees in the software department 
from the MongoDB database called company_employees:
*/

const { MongoClient } = require('mongodb');
const { MONGODB_URI, MONGODB_DBNAME } = process.env;

// Function to retrieve a list of employees from the 'company_employees' collection
async function getEmployeeList() {
    try {
        // Create a new MongoDB client with the provided URI
        const client = new MongoClient(MONGODB_URI, { useUnifiedTopology: true });

        // Connect to the MongoDB server
        await client.connect();

        // Get the specified database using the provided database name
        const dbName = client.db(MONGODB_DBNAME);

        // Find employees in the 'company_employees' collection with the specified department
        const employees = await dbName.collection('company_employees').find({
            department: 'software',
        }).toArray();

        // Prepare the result array to store the required employee details
        const result = [];
        for (const employee of employees) {
            // Extract necessary employee details
            const { _id, name, surname, department, start_date, age } = employee;

            // Push the extracted details into the result array
            result.push({
                _id,
                name,
                surname,
                department,
                start_date,
                age,
            });
        }

        // Close the MongoDB client connection
        await client.close();

        // Return the result containing employee details
        return result;
    } catch (error) {
        // Handle errors by logging the error message and returning an empty array
        console.error('Error:', error);
        return [];
    }
}

// Export the getEmployeeList function to make it accessible from other modules
module.exports = {
    getEmployeeList,
};

/*
The code uses the MongoDB client library to connect to the database and retrieve the list of employees 
in the software department. The result is an array of objects with the properties _id, name, surname, department, 
start_date, and age.

now generate a controller to add an employee

Here is a sample code in JavaScript using Node.js to add an employee to the MongoDB database called company_employees:
*/

const { MongoClient } = require('mongodb');
const { MONGODB_URI, MONGODB_DBNAME } = process.env;

// Function to add an employee to the 'company_employees' collection
async function addEmployee(employee) {
    try {
        // Create a new MongoDB client with the provided URI
        const client = new MongoClient(MONGODB_URI, { useUnifiedTopology: true });

        // Connect to the MongoDB server
        await client.connect();

        // Get the specified database using the provided database name
        const dbName = client.db(MONGODB_DBNAME);

        // Define the employee document
        const employeeDocument = {
            _id: new require('mongodb').ObjectID(),
            name: employee.name,
            surname: employee.surname,
            department: employee.department,
            start_date: employee.start_date,
            age: employee.age,
        };

        // Insert the employee document into the 'company_employees' collection
        const result = await dbName.collection('company_employees').insertOne(employeeDocument);

        // Close the MongoDB client connection
        await client.close();

        // Return the result of the update operation
        return result;
    } catch (error) {
        // Handle errors by logging the error message and returning a null value
        console.error('Error:', error);
        return null;
    }
}

// Export the addEmployee function to make it accessible from other modules
module.exports = {
    addEmployee,
};

/*
This code uses the MongoDB client library to connect to the database and add an employee to the company_employees 
collection. The employee document is defined with the properties _id, name, surname, department, start_date, and age. 
Then it is inserted into the database using the insertOne() function.


i want you to generate the controller for updating an employee


Here is a sample code in JavaScript using Node.js to update an employee in the MongoDB database called company_employees:
*/


const { MongoClient } = require('mongodb');
const { MONGODB_URI, MONGODB_DBNAME } = process.env;

// Function to update an employee in the 'company_employees' collection
async function updateEmployee(employee) {
    try {
        // Create a new MongoDB client with the provided URI
        const client = new MongoClient(MONGODB_URI, { useUnifiedTopology: true });

        // Connect to the MongoDB server
        await client.connect();

        // Get the specified database using the provided database name
        const dbName = client.db(MONGODB_DBNAME);

        // Update the employee document in the 'company_employees' collection
        const result = await dbName.collection('company_employees').updateOne(
            { _id: employee.id },
            {
                $set: {
                    name: employee.name,
                    surname: employee.surname,
                    department: employee.department,
                    start_date: employee.start_date,
                    age: employee.age,
                },
            }
        );

        // Close the MongoDB client connection
        await client.close();

        // Return the result of the update operation
        return result;
    } catch (error) {
        // Handle errors by logging the error message and returning a null value
        console.error('Error:', error);
        return null;
    }
}

// Export the updateEmployee function to make it accessible from other modules
module.exports = {
    updateEmployee,
};

/*
This code uses the MongoDB client library to connect to the database and update an employee in the company_employees 
collection. A MongoDB client is created using the provided MONGODB_URI, and a connection is made to the MongoDB server 
using MONGODB_DBNAME. Using MONGODB_DBNAME, it then retrieves the specified database. With the updated employee details, 
it then constructs an object called employeeDocument.

The employee document is defined with the properties _id, name, surname, department, start_date, and age. Then it is 
updated in the database using the updateOne() function. The filter and update parameters are used to define the criteria 
and changes to be made in the update operation.v

Finally, it returns the result of the update operation and, in the event of an error, the function will log the error 
message and return a zero value.


generate code to delete one


Here is a sample code in JavaScript using Node.js to delete an employee from the MongoDB database called company_employees:
*/

const { MongoClient, ObjectId } = require('mongodb');
const { MONGODB_URI, MONGODB_DBNAME } = process.env;

// Function to delete an employee from the 'company_employees' collection
async function deleteEmployee(id) {
    try {
        // Create a new MongoDB client with the provided URI
        const client = new MongoClient(MONGODB_URI, { useUnifiedTopology: true });

        // Connect to the MongoDB server
        await client.connect();

        // Get the specified database using the provided database name
        const dbName = client.db(MONGODB_DBNAME);

        // Convert the provided id to ObjectId
        const objectId = new ObjectId(id);

        // Delete the employee document in the 'company_employees' collection
        const result = await dbName.collection('company_employees').deleteOne({
            _id: objectId,
        });

        // Close the MongoDB client connection
        await client.close();

        // Return the result of the delete operation
        return result;
    } catch (error) {
        // Handle errors by logging the error message and returning a null value
        console.error('Error:', error);
        return null;
    }
}

// Export the deleteEmployee function to make it accessible from other modules
module.exports = {
    deleteEmployee,
};
/*
This code uses the MongoDB client library to connect to the database and delete an employee from the company_employees 
collection.

now i want code to het one employee


Here is a sample code in JavaScript using Node.js to retrieve one employee from the MongoDB database called company_employees:
*/

const { MongoClient } = require('mongodb');
const { MONGODB_URI, MONGODB_DBNAME } = process.env;

// Function to get one employee from the 'company_employees' collection
async function getEmployee(id) {
    try {
        // Create a new MongoDB client with the provided URI
        const client = new MongoClient(MONGODB_URI, { useUnifiedTopology: true });

        // Connect to the MongoDB server
        await client.connect();

        // Get the specified database using the provided database name
        const dbName = client.db(MONGODB_DBNAME);

        // Convert the provided id to ObjectId
        const objectId = new require('mongodb').ObjectID(id);

        // Get the employee document in the 'company_employees' collection using the provided id
        const result = await dbName.collection('company_employees').findOne({
            _id: objectId,
        });

        // Close the MongoDB client connection
        await client.close();

        // Return the result of the find operation
        return result;
    } catch (error) {
        // Handle errors by logging the error message and returning a null value
        console.error('Error:', error);
        return null;
    }
}

// Export the getEmployee function to make it accessible from other modules
module.exports = {
    getEmployee,
};

/*
This code uses the MongoDB client library to connect to the database and retrieve one employee from the company_employees 
collection.
*/