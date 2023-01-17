#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
request('https://swapi-api.alx-tools.com/api/films/' + id, function (err, response, body) {
  if (response.statusCode === 200) {
    for (const url of JSON.parse(body).characters) {
      request(url, function (error, res, bod) {
        if (response.statusCode === 200) {
          console.log(JSON.parse(bod).name);
        } else {
          console.error(error);
        }
      });
    }
  } else {
    console.error(err);
  }
});
