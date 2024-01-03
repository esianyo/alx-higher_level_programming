#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const movie = JSON.parse(body);
    const characters = movie.characters;

    const characterNames = [];
    const requests = characters.map((characterUrl) => {
      return new Promise((resolve) => {
        request(characterUrl, (charError, charResponse, charBody) => {
          if (charError) {
            console.error(charError);
          } else {
            const character = JSON.parse(charBody);
            characterNames.push(character.name);
            resolve();
          }
        });
      });
    });

    Promise.all(requests).then(() => {
      characterNames.forEach((name) => {
        console.log(name);
      });
    });
  }
});
