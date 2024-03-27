#!/usr/bin/node

const request = require('request');
const link = process.argv[2];
const cId = '18';

request(link, (e, r, b) => {
	if (e) {
		console.error('error:', e);
		return;
	}
	const m = JSON.parse(b).results;
	let c = 0;
	m.forEach((film) => {
		if (film.characters.some((url) => url.includes(`/people/${cId}/`))) {
			c++;
		}
	});
	console.log(c);
});
