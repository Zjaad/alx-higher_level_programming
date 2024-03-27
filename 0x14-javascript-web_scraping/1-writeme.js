#!/usr/bin/node

const f = require('fs');
const path = process.argv[2];
const c = process.argv[3];

f.writeFile(path, c, 'utf8', (e) => {
	if (e) {
		console.error(e);
	}
});
