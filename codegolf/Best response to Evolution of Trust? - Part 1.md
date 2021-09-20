## Backstory
I was fiddling around with the [Evolution of Trust][1] and thought of this.<br>**Warning**: I recommend you go [check it out first][1] before attempting this challenge.

## Summary for people who haven’t played
A quick summary of what it says [on the site][1]: there is a machine. If you put in one coin, your **opponent** gets **three** coins (and vice versa). You can either Cooperate (put in a coin) or Cheat (don't put in a coin).

## Challenge
Given the name of a strategy (`copycat`, `alwayscheat`, `alwayscooperate`, `grudger` or `detective`) and the number of rounds, return/output a list of truthy (Cooperate) and falsey (Cheat) values that, when put against that strategy, will give you the maximum possible amount of coins. (I'm using Y for cooperate and N for cheat in my examples)

For clarification, check the **Input and Output** section.

## Quick info for people who have played
The amount of rounds is given in the input. There are no mistakes, and the rewards for Cooperating/Cheating are the same as [the site][1] - see the image below.

![See https://i.stack.imgur.com/qyEIQ.jpg][2]

<sub>Yes, this is basically a Prisoner's Dilemma - [Nicky Case] says this in the “[feetnotes]” of the game.<br>Also, "Cheat" is basically the same as Defect.</sub>

## The characters
 * Copycat `copycat`
 * Always Cooperate `alwayscooperate`
 * Always Cheat `alwayscheat`
 * Grudger `grudger`
 * Detective `detective`

## The characters' strategies from [the site][1]
* Copycat: Hello! I start with Cooperate, and afterwards, I just copy whatever you did in the last round. *Meow*
* Always Cheat: *the strong shall eat the weak* (always cheats)
* Always Cooperate: Let's be best friends! <3 (always cooperates)
* Grudger: Listen, pardner. I'll start cooperatin', and keep cooperatin', but if y'all ever cheat me, **I'LL CHEAT YOU BACK 'TIL THE END OF TARNATION.** (cooperates until you cheat once, then cheats you back for the rest of the game)
* Detective: First: I analyze you. I start: Cooperate, Cheat, Cooperate, Cooperate. If you cheat back, I'll act like Copycat. If you never cheat back, I'll act like Always Cheat, to exploit you. Elementary, my dear Watson.

## Input and Output
Input is the name of the strategy and the amount of rounds in any order you specify, in a list, or a space-separated string.

Output is a list of truthy (Cooperate) and falsey (Cheat) values that, when put against the strategy, gives you the most amount of points.

## Test cases

```
"grudger 3" => "YYN" or [<2 truthy values>, falsey]
"detective 5" => "NNNYN" or [<3 falsey values,> truthy, falsey]
"alwayscheat 7" => "NNNNNNN" or [<7 falsey values>]
"alwayscooperate 99" => <insert 99 N's here> or [<99 falsey values>]
"copycat 7" => "YYYYYYN" or [<6 truthy values>, falsey]
"detective 4" => "NNNN" (4 N's) or [<4 falsey values>]
"alwayscheat 999" => 999 N's or [<999 falsey values>]
"grudger 1" => "N" or [falsey]
```

Easy copy paste:

```
grudger 3
detective 5
alwayscheat 7
alwayscooperate 99
copycat 7
detective 4
alwayscheat 999
grudger 1
```

## Rules
* This is <kbd>code-golf</kbd>, shortest answer wins, tiebreaks sorted by time(stamp) created
* Standard loopholes are not allowed, unless they are creative (e.g. asking for list input and using the fact that it is a *list* to shorten your code). No extra points are given for this

> WD

<kbd>code-golf</kbd> <kbd>game</kbd>

  [1]: https://ncase.me/trust "*trust* me, this is a tooltip (pun intended)"
  [2]: https://i.stack.imgur.com/qyEIQ.jpg
  [Nicky Case]: http://ncase.me/
  [feetnotes]: https://ncase.me/trust/notes/
