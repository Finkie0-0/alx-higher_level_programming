#!/usr/bin/node
// script that reads and prints the content of a file.

const fs = require('fs');
const file_name = process.argv[2];
fs.readFile(file_name, 'utf8', function (error, data) {
  if (error) {
    return console.log(error);
  }
  console.log(data);
});

