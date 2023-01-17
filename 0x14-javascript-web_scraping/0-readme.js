#!/usr/bin/node
const fs = require('fs');
const filename = process.argv[2];
fs.readFile(filename, 'utf8', function (error, data) {
  if (error) {
    return console.log(error);
  }
  console.log(data);
});
