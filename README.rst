### About
This is a small project designed to solve the old 'Kevin Bacon' game the old-fashioned way - it doesn't rely on a local SQL database dump from IMDb, it uses pure web queries. It is also designed to attempt to process it film at a time - no parallel processing, just old fashioned 'line at a time' output. Looks great when you set it going in a terminal :)

### The Game
If you've never heard of it, the Kevin Bacon game comes from a phrase once uttered by Kevin Bacon - he said that he believes that he has worked with the most diverse range of actors in hollywood.

From that, people decided to put him to the test, and a game was devised. Whilst the origin for the rules of the game are based on garbage (the old '6 degrees of seperation' idea, which itself was based on fatally flawed data)

### The Rules
The rules are as follows:

2 or more people attempt to link 2 random actors/actresses, linking them through other actors that they have worked with.

For example, if the 2 random actors/actresses were:

Angelia Jolie & Kevin Costner

One solution would be:
```
Angelina Jolie & Brad Pitt - Mr & Mrs Smith
Brad Pitt & Christian Slater - Interview with a Vampire
Christian Slater & Kevin Costner - Robin Hood: Prince of Thieves
```
That would give you a score of **3**, or you have done it in 3 links. Normally the game is limited to 6 links, but that is down to personal choice - sometimes it is easier to allow more links when you first start playing the game.
