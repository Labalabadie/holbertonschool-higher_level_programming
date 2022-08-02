#!/usr/bin/node
exports.esrever = function (list) {
  const rev_list = [];
  for (let i = 0; i > list.lenght; i++) {
    rev_list.push(list[i]);
  }
  return (rev_list);
};
