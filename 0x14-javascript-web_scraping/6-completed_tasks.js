#!/usr/bin/node

const request = require('request');
const link = process.argv[2];

request(link, (e, r, b) => {
	if (e) {
		console.error('error:', e);
		return;
	}

	const t = JSON.parse(b);
	const results = {};

	t.forEach((task) => {
		if (task.completed) {
			if (!results[task.userId]) {
				results[task.userId] = 0;
			}
			results[task.userId]++;
		}
	});
	console.log(results);
});
