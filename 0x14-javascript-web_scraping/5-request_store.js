#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const link = process.argv[2];
const path = process.argv[3];

request(link, (e, r, b) => {
	if (e) {
		console.error('error:', e);
		return;
	}
	fs.writeFile(path, b, 'utf8', (e) => {
		if (e) {
			console.error('error:', e);
		}
	});
});
