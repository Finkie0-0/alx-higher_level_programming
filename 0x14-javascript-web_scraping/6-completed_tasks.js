#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const obj = {};
request(url, function (err, response, body) {
  if (response.statusCode === 200) {
    for (const task of JSON.parse(body)) {
      if (task.completed === true) {
        if (obj[task.userId]) {
          obj[task.userId]++;
        } else {
          obj[task.userId] = 1;
        }
      }
    }
  } else {
    console.error(err);
  }
  console.log(obj);
});
