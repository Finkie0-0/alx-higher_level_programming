#!/usr/bin/node
const fs = require('fs');
const file_name = process.argv[2];
fs.readFile(fil_ename, 'utf8', function (error, data) {
  if (error) {
    return console.log(error);
  }
  console.log(data);
});
