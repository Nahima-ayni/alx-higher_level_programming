const fs = require('fs');

// The first argument is the file path
const filePath = process.argv[2];

//second argument is the string to write
const content = process.argv[3];

fs.writeFile(filePath, content, 'utf8', function (err) {
  if (err) {
    // If an error occurred during writing, print the error object
    console.error(err);
  }
});