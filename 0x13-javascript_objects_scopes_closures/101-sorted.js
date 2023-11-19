#!/usr/bin/node

const { dict } = require('./101-data');

const s = {};

for (const userId in dict) {
  const o = dict[userId].toString();

  if (!s[o]) {
    s[o] = [];
  }

  s[o].push(userId);
}

console.log(s);
