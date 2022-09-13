#!/usr/bin/node

const axios = require('axios').default;

axios.get(process.argv[2])
  .then(function (response) {
    // handle success
    const films = response.data.results;
    let i = 0;
    let film, character;
    for (film in films) {
      for (character in films[film].characters) {
        if (films[film].characters[character].includes('/18/')) {
          i++;
        }
      }
    }
    console.log(i);
  })
  .catch(function (error) {
    // handle error
    console.log(error);
  })
  .then(function () {
    // always executed
  });
