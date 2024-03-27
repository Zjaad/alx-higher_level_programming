#!/usr/bin/node

const f = require('fs');
const path = process.argv[2];

f.readFile(path, 'utf8', (e, d) => {
  if (e) {
    console.error(e);
    return;
  }
  console.log(d);
});
