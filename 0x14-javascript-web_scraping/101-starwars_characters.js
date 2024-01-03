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

    let count = 0;

    function printCharacter () {
      if (count < characters.length) {
        const characterUrl = characters[count];
        request(characterUrl, (charError, charResponse, charBody) => {
          if (charError) {
            console.error(charError);
          } else {
            const character = JSON.parse(charBody);
            console.log(character.name);
            count++;
            printCharacter();
          }
        });
      }
    }

    printCharacter();
  }
});
