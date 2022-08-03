#!/usr/bin/node

let AmountOfArgs = 0;
exports.logMe = function (item) {
  console.log(AmountOfArgs = ': ' + item);
  AmountOfArgs++;
};
