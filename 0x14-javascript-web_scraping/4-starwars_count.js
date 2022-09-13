#!/usr/bin/node

const axios = require('axios').default;

const url = 'https://swapi-api.hbtn.io/api/films/';

axios.get(process.argv[2])
  .then(function (response) {
    // handle success
    const films = response.data.results;
    console.log(films.filter((elem) =>
      elem.characters.includes('https://swapi-api.hbtn.io/api/people/18/')).length);
  })
  .catch(function (error) {
    // handle error
    console.log(error);
  })
  .then(function () {
    // always executed
  });
