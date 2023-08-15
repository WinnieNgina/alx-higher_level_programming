#!/usr/bin/node
exports.callMeMoby = function (number, theFunction) {
  for (let i = 0; i < number; i++) {
    theFunction();
  }
};
