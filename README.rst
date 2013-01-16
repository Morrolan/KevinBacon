### About

**NOTE:**  This is still **pre-alpha** and doesn't currently work - the old version I was working on is now deprecated and it is being rewritten from scratch.

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


### The Maths

Based on the conservative average that an actor has starred in 25 films,
and each film has featured 25 actors:
  
We start with 1 actor,
who has starred in 25 films,
which have starred 625 actors,
who have starred in 15,625 films,
which have starred 390,625 actors,
who have starred in 9,765,625 films,
which have starred 244,140,625 actors,
who have starred in 6,103,515,625 films,
which have starred 152,587,890,625 actors,
who have starred in 3,814,697,265,625 films,
which have starred 95,367,431,640,625 actors,
who have starred in 2,384,185,791,015,620 films.
  
This gives us 2,384,185,791,015,620 possible combinations from 1 actor to another at 6 levels.

As you can see, the mathematics VERY quickly spiral out of control.  Note that this is a purely statistical calculation, and does not take into account that actors may have worked with each other multiple times, nor does it take into account the actual number of films made by Hollywood - it is purely the number of possible combinations (I think.)


