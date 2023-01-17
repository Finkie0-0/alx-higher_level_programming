#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
let cnt = 0;
request(url, function (err, response, body) {
  if (response.statusCode === 200) {
    for (const res of JSON.parse(body).results) {
      for (const character of res.characters) {
        if (character.includes('18')) {
          cnt++;
        }
      }
    }
  } else {
    console.error(err);
  }
  console.log(cnt);
});
