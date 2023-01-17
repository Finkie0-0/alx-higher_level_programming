#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const filename = process.argv[3];
request(url, function (err, response, body) {
  if (response.statusCode === 200) {
    fs.writeFile(filename, body, 'utf8', function (err, data) {
      if (err) return console.log(err);
    });
  } else {
    console.error(err);
  }
});
