const fs = require('fs');
const path = require('path');
const { promisify } = require('util');
const readFileAsync = promisify(fs.readFile);
const writeFileAsync = promisify(fs.writeFile);

// Define the backup directory and file names
const backupDirectory = path.resolve(__dirname, 'backups');
const backupFile = 'backup.json';

// Define the backup data
const backupData = {
    // Add your backup data here
};

// Create the backup directory if it doesn't exist
fs.existsSync(backupDirectory) || fs.mkdirSync(backupDirectory);

// Write the backup data to a file
writeFileAsync(path.resolve(backupDirectory, backupFile), JSON.stringify(backupData, null, 2), { encoding: 'utf8' })
    .then(() => console.log('Backup successful'))
    .catch((error) => console.error('Backup failed:', error));