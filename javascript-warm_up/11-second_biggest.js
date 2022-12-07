#!/usr/bin/node
/*
 script that searches the second biggest integer in the list of arguments
 */

function numberCompare (a, b) {
  return a - b;
}
const args = process.argv.length;
if (args === 2 || args === 3) {
  console.log('0');
} else {
  const array = [];
  for (let i = 2; i < args; i++) {
    array.push(process.argv[i]);
  }
  array.sort(numberCompare);
  console.log(array[array.length - 2]);
}
