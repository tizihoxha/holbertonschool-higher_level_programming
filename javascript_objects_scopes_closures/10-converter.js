#!/usr/bin/node
/*
 function that converts a number from base 10
 */

exports.converter = function (base) {
  return function (number) {
    return number.toString(base);
  };
};
