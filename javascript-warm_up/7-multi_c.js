#!/usr/bin/node
/*
 script that prints My number: <first argument converted in integer>
 */

const number = parseInt(process.argv[2]);

if (!number) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < process.argv[2]; i++) {
    console.log('C is fun');
  }
}
