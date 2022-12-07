#!/usr/bin/node
/*
 script that prints My number: <first argument converted in integer>
 */

const a = parseInt(process.argv[2]);
const b = parseInt(process.argv[3]);
const result = (a + b);

console.log(result);
