#!/usr/bin/node
const request = require('request');
const filmId = process.argv[2];
request('https://swapi-api.alx-tools.com/api/films/' + filmId, function (err, response, body) {
  if (response.statusCode === 200) {
    console.log(JSON.parse(body).title);
  } else {
    console.error(err);
  }
});

