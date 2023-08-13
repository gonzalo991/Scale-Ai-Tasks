const fs = require('fs').promises;
const path = require('path');

// Define the registry directory and file names
const registryDirectory = path.resolve(__dirname, 'registry');
const registryFile = 'registry.json';

// Define the destination directories (populate with actual data)
const destinationDirectories = {
    '.txt': path.resolve(__dirname, 'txtFiles'),
    '.csv': path.resolve(__dirname, 'csvFiles'),
};

(async () => {
    try {
        // Create the registry directory if it doesn't exist
        await fs.mkdir(registryDirectory, { recursive: true });

        // Check if the registry file exists
        const registryFilePath = path.resolve(registryDirectory, registryFile);
        try {
            await fs.access(registryFilePath, fs.constants.F_OK);
        } catch (error) {
            // Create the registry file if it doesn't exist
            await fs.writeFile(registryFilePath, JSON.stringify({ files: [] }), {
                encoding: 'utf8',
            });
        }

        // Read the registry data from the file
        const registryData = JSON.parse(await fs.readFile(registryFilePath, 'utf8'));

        // Classify the files based on their extension or type
        const fileExtensionsOrTypes = Object.keys(destinationDirectories);
        const classifiedFiles = registryData.files.filter((file) => {
            return fileExtensionsOrTypes.includes(path.extname(file.path));
        });

        // Move the classified files to their respective destination directories
        await Promise.all(
            classifiedFiles.map(async (file) => {
                const destinationDirectory =
                    destinationDirectories[path.extname(file.path)];
                const destinationPath = path.resolve(destinationDirectory, file.name);
                try {
                    await fs.mkdir(destinationDirectory, { recursive: true });
                    await fs.rename(file.path, destinationPath);
                    console.log(`File '${file.name}' moved to ${destinationDirectory}`);
                } catch (error) {
                    console.error(`Error moving file '${file.name}':`, error);
                }
            })
        );
    } catch (error) {
        console.error('An error occurred:', error);
    }
})();