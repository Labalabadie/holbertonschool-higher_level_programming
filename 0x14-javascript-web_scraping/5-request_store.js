#!/usr/bin/node

const axios = require('axios').default;
const fs = require('fs');

//const url = 'http://loripsum.net/api loripsum';

axios.get(process.argv[2])
  .then(function (response) {
    // handle success

    fs.writeFile(process.argv[3], response.data, 'utf-8', function (err, data) {
      if (err) {
        console.log(err);
      }
    });
  })
  .catch(function (error) {
    // handle error
    console.log(error);
  })
  .then(function () {
    // always executed
  });
