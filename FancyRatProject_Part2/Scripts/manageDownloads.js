const fs = require('fs');
const path = require('path');

// Define the directory where the downloaded files are stored
const downloadDirectory = path.resolve(__dirname, 'download');

// Define the extension of the downloaded files
const fileExtension = '.pdf';

// Define the destination directory where the sorted files should be stored
const destinationDirectory = path.resolve(__dirname, 'sorted');

// Define the maximum age of files to be deleted in days
const maxAge = 30; // 30 days

// Define the current date
const currentDate = new Date();

// Define the files to be deleted
const filesToDelete = [];

// Define the files to be sorted
const filesToSort = [];

// Create the destination directory if it doesn't exist
if (!fs.existsSync(destinationDirectory)) {
    fs.mkdirSync(destinationDirectory);
}

// Iterate through the files in the download directory
for (const file of fs.readdirSync(downloadDirectory)) {
    const fullPath = path.resolve(downloadDirectory, file);
    const fileStat = fs.statSync(fullPath);
    const fileAgeInDays = Math.floor(
        (currentDate - fileStat.mtime) / (24 * 60 * 60 * 1000)
    );

    if (fileAgeInDays > maxAge) {
        filesToDelete.push(fullPath);
    } else if (path.extname(file) === fileExtension) {
        filesToSort.push(fullPath);
    }
}

// Iterate through the files to be deleted
for (const fileToDelete of filesToDelete) {
    try {
        fs.unlinkSync(fileToDelete);
        console.log(`File deleted: ${fileToDelete}`);
    } catch (error) {
        console.error(`Error deleting file '${fileToDelete}':`, error);
    }
}

// Iterate through the files to be sorted
for (const fileToSort of filesToSort) {
    const destinationPath = path.resolve(
        destinationDirectory,
        path.basename(fileToSort)
    );

    try {
        fs.renameSync(fileToSort, destinationPath);
        console.log(`File sorted: ${fileToSort} -> ${destinationPath}`);
    } catch (error) {
        console.error(`Error sorting file '${fileToSort}':`, error);
    }
}

// Write the date of the last sort to a file
try {
    fs.writeFileSync(
        path.resolve(__dirname, 'lastSortDate.txt'),
        currentDate.toISOString().substr(0, 10),
        { encoding: 'utf8' }
    );
} catch (error) {
    console.error('Error writing lastSortDate:', error);
}

// Log the number of files deleted and sorted
console.log(`Number of files deleted: ${filesToDelete.length}`);
console.log(`Number of files sorted: ${filesToSort.length}`);