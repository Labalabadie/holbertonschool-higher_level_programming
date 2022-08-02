#!/usr/bin/node
class Rectangle {
	constructor (w,h) {
		if (((w = parseInt) > 0) && ((h = parseInt(h)) > 0)) {
			this.width = w;
			this.height = h;
		}
	}
}
module.exports = Rectangle;
