#!/usr/bin/node
/*
 function that prints the number of arguments already printed
 */

let args = 0;
exports.logMee = function (item) {
  console.log(args + ':' + item);
  args++;
};
