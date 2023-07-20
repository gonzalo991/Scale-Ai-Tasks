## Testing Strategy for News Controllers

## Summary
The News Controller testing strategy for this application is described in this document. It details the guidance for
the tests to be carried out on each of the functions within the controller.

## Testing Tools
We will use a combination of Mocha (testing framework), Chai (assertion library) and Sinon (for duplicating tests) for testing. 
and Sinon (for duplicating tests) for unit testing.

## Test environment
Tests should be run in a test environment that is separate from the production and pre-production environments, 
with a test database.

## Test cases

## getNews
- With the database empty, test the driver.
- When the database has a news article, test the operation of the driver.
- If the database has multiple news articles, test if the driver returns the news list.

### addNews
- Create a newsitem from the control with all mandatory fields supplied.
- Create a news item without the required `image` field.
- Create a news item without the required `title', `background' or `text' fields.
- Identification of an error in the saving process.

### updateNews
- If the given ID does not exist in the database, edit a news item.
- Edit a news item that does not have the mandatory `image` field.
- Edit without the mandatory `title`, `review` or `text` fields.
- Carry out an edit on a news item where all the fields are valid and the ID is present in the database.
- Identification if there is an error during the update process.

### deleteNews
- Perform a test of the driver if the ID provided does not exist in the database.
- Delete a news item if the ID provided is valid and does exist in the database.
- Detect if there is an error during the delete operation.

## Dummy Data
For all test cases, create dummy data.

## Error Handling
Test the application's handling of errors: the application should not crash and should have a useful error message.

## Test execution
Before merging code into the main branch, tests should be run. They should also be run after 
run after every change to the code. This includes bug fixes and new features.

## Reporting
The results of the tests should be reported in the console for the developers, and within the CI/CD pipeline. 
to help keep track of where the Software stands.
