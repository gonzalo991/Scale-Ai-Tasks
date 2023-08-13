const fs = require('fs').promises;
const path = require('path');

async function main() {
    try {
        // Define the directory to be scanned
        const directory = path.resolve(__dirname, 'directory');

        // Define the maximum age of files to be deleted in days
        const maxAge = 30; // 30 days

        // Define the current date
        const currentDate = new Date();

        // Get the list of directory entries
        const directoryEntries = await fs.readdir(directory);

        // Define the files to be deleted
        const filesToDelete = [];

        // Iterate through the directory entries
        for (const directoryEntry of directoryEntries) {
            // Get the full file path
            const fullPath = path.resolve(directory, directoryEntry);

            // Get the file's stat object
            const fileStat = await fs.stat(fullPath);

            // Calculate the age of the file in days
            const fileAgeInDays = Math.floor(
                (currentDate - fileStat.mtime) / (24 * 60 * 60 * 1000)
            );

            // Compare the file's age to the maximum age
            if (fileAgeInDays > maxAge) {
                // If the file is older than the maximum age, add it to the list of files to be deleted
                filesToDelete.push(fullPath);
            }
        }

        // Iterate through the files to be deleted
        for (const fileToDelete of filesToDelete) {
            // Remove the file from the file system
            await fs.unlink(fileToDelete);
        }

        // Write the date of the last scan to a file
        const lastScanDate = new Date().toISOString().substr(0, 10);
        await fs.writeFile(
            path.resolve(__dirname, 'lastScanDate.txt'),
            lastScanDate,
            { encoding: 'utf8' }
        );

        // Log the number of files deleted
        console.log(`Number of files deleted: ${filesToDelete.length}`);
    } catch (error) {
        console.error('An error occurred:', error);
    }
}

main();