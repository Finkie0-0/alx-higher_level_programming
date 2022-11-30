#!/usr/bin/node
//Function returns number of occurrences in a list
exports.nbOccurences = function (list, searchElement) {
  let ocurrences = 0;
  list.forEach(element => {
    if (element === searchElement) {
      ocurrences++;
    }
  });
  return ocurrences;
};
