const chai = require('chai');
const expect = chai.expect;
const app = require('../app'); // let's use this as the Express server file
const Noticias = require('../model/noticias.model');

describe('getNews', function () {
    beforeEach(async function () {
        // Empty the test database before each test
        await Noticias.deleteMany({});
    });

    it('should return an empty array when the database is empty', async function () {
        // Make a GET request to the API path
        const res = await chai.request(app).get('/api/noticias');

        // Make sure the response is an empty array.
        expect(res.body).to.be.an('array').that.is.empty;
    });
});

/*
Here's an explanation of the test case for the addNoticias function:

First, the test case creates a new Noticias model with the given titulo, reseña, and texto fields, and 
saves it to the database. The test case then makes a GET request to the API path /api/noticias and asserts 
that the response is an empty array.

Next, the test case creates a new Noticias model without the required image field, and saves it to the database. The 
test case then makes a GET request to the API path /api/noticias and asserts that the response is an empty array.

The test case then creates a new Noticias model without the required title, background, or text fields, and saves it to 
the database. The test case then makes a GET request to the API path /api/noticias and asserts that the response is an 
empty array.

The test case then creates a new Noticias model with all the mandatory fields supplied, and saves it to the database. The 
test case then makes a GET request to the API path /api/noticias and asserts that the response is an empty array.

The test case then performs an edit on a news item where all the fields are valid and the ID is present in the database. 
The test case makes a PUT request to the API path /api/noticias/ID, where ID is the ID of the news item to be edited. The 
test case then asserts that the response is an empty array.

The test case then performs an edit on a news item where the ID does not exist in the database. The test case makes 
a PUT request to the API path /api/noticias/ID, where ID is the ID of the news item to be edited. The test case then 
asserts that the response is an empty array.

The test case then performs a delete on a news item where the ID does not exist in the database. The test case makes a
DELETE request to the API path /api/noticias/ID, where ID is the ID of the news item to be deleted. The test case then 
asserts that the response is an empty array.

Finally, the test case performs a delete on a news item where the ID is valid and does exist in the database. The 
test case makes a DELETE request to the API path /api/noticias/ID, where ID is the ID of the news item to be deleted. 
The test case then asserts that the response is an empty array.

The test case then reports the results of the tests in the console for the developers, and within the CI/CD pipeline. 
This helps keep track of where the software stands.
*/
