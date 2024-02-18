#!/usr/bin/node

const util = require('util');
const request = util.promisify(require('request'));

// get movie id from command line
const movieId = process.argv[2];

async function getMovieCharacters (movieId) {
  const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;
  let movieData = await (await request(url)).body;
  movieData = JSON.parse(movieData);
  const characters = movieData.characters;

  for (const character of characters) {
    let characterData = await (await request(character)).body;
    characterData = JSON.parse(characterData);
    console.log(characterData.name);
  }
}

getMovieCharacters(movieId);
