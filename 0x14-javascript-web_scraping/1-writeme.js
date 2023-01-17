#!/usr/bin/node
const fs = require('fs');
const file_name = process.argv[2];
fs.writeFile(fil_ename, process.argv[3], 'utf8', function (error, data) {
  if (error) return console.log(error);
});
