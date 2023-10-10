#!/usr/bin/node

const mainUrl = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
const request = require('request');

// Main Request
request(mainUrl, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const urlArray = JSON.parse(body).characters;
    myAsyn(urlArray);
  }
});

// Sub request function
function subRequest (url) {
  return new Promise(function (resolve, reject) {
    request(url, function (error2, response2, body2) {
      if (error2) {
        reject(error2);
      } else {
        resolve(JSON.parse(body2).name);
      }
    });
  });
}

// Asynchronous function awaits for
// sub request resolution after each iterations
async function myAsyn (urlArray) {
  for (const url of urlArray) {
    const character = await subRequest(url);
    console.log(character);
  }
}
