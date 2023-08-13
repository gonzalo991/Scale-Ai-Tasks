const fs = require('fs');
const path = require('path');
const { promisify } = require('util');
const readFileAsync = promisify(fs.readFile);
const writeFileAsync = promisify(fs.writeFile);

// Define the registry directory and file names
const registryDirectory = path.resolve(__dirname, 'registry');
const registryFile = 'registry.json';

// Define the registry data
const registryData = {
    // Add your registry data here
};

// Create the registry directory if it doesn't exist
fs.existsSync(registryDirectory) || fs.mkdirSync(registryDirectory);

// Write the registry data to a file
writeFileAsync(path.resolve(registryDirectory, registryFile), JSON.stringify(registryData, null, 2), { encoding: 'utf8' })
    .then(() => console.log('Registry updated'))
    .catch((error) => console.error('Registry update failed:', error));