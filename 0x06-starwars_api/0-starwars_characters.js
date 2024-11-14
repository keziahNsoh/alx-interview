#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

// Check if movieId argument is provided
if (!movieId) {
  console.error('Please provide a movie ID');
  process.exit(1);
}

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  if (response.statusCode !== 200) {
    console.error(`Failed to fetch movie data, status code: ${response.statusCode}`);
    return;
  }

  const filmData = JSON.parse(body);
  const characters = filmData.characters;

  // Fetch and display each character's name in order
  fetchCharactersInOrder(characters, 0);
});

function fetchCharactersInOrder (characters, index) { // <-- Added space here
  if (index >= characters.length) return;

  request(characters[index], (error, response, body) => {
    if (error) {
      console.error(error);
      return;
    }
    if (response.statusCode === 200) {
      const characterData = JSON.parse(body);
      console.log(characterData.name);
      fetchCharactersInOrder(characters, index + 1);
    }
  });
}
