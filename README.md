# meta-dice
Instead of creating a bot for our discord server I created this simple flask app that returns a number as the meta description of the page.

![The description on a Discord chat](/readme/preview.png)

The link to generate a number is https://meta-dice.herokuapp.com/number where `number` is the max. 

For instance:
https://meta-dice.herokuapp.com/20 will roll a 20 sides dice.

Beware of Discord's cache, to invalidate it you can add a random string at the end of the url like so: https://meta-dice.herokuapp.com/10?randomstring

Enjoy!