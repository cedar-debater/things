# [Python 2][py2], 76 bytes

[Try it online!][tio]

[Test cases (but they’re Python 3.8)]

<!-- language-all: lang-python -->

    a,b=input();y='Y'*b;print{'c':y,'g':y,'d':'N'*3+y,'a':'N'*b}[a[0]][:b-1]+'N'

Example input: `['detective',5]`

Example output: NNNYN

I expect this to be golfed quickly, as it’s just an example and it’s my first post. Here’s an explanation:

```
a,b=input(); # equivalent to this: # a,b = eval(raw_input())

y='Y'*b; # add this to the end when you want
# to cooperate for the rest of the game (apart
# from the last move)

print # print everything after this and
# before a newline/semicolon

{…}[a[0]]… # get the first letter and index it in the dictionary

{ # a dictionary

'c':y, # always cooperate for copycat, except last
# (see below)

'g':y, # same thing

'd':'N'*3+y, # cheat 3 time, then cooperate for the rest
# because detective acts like copycat after 4 if
# you cooperate or else always cheats, you don’t want, so
# add coop to end so detective copies that and cooperate

'a':'N'*b # always Cheat/Cooperate doesn’t care what you do, so just always cheat back for best score

}

[:b-1] # remove all the excess, so it’s nearly done
# but there’s one missing move, that one is

+'N' # this - always cheat on the last round because there is no time for the other player/strategy/“hat person” to retaliate

```

[py2]: https://docs.python.org/2/
[tio]: https://tio.run/##LYzLCoMwFET3/YqLLq6vgtad4i@4l5BF1FhDJQnmWgil325FuzkcZoaxnmajH3sIStuNQDkQsChHB14SGA7G@kEQZiW/hWA2@q@CLoDJrOClg4jWjWYfg9AjBO1VaAPRJBYnfbyLrG/O/yiufYMdJn1tV6XpgwNWPsPnyRErbDEp08PF5f2XCZZzzqr@XvD0iPad4ShJDqTeErMiz/kP
[Test cases (but they’re Python 3.8)]: https://tio.run/##ZZDBasMwDIbveQqRHpS0WVlpx5aUvkLvxeTgxG5iltnGVjrM2LNn8TK2wi5C@vTrF5IN1Bu9f7FuWoHSdiRQHjgMytMcXiUwbI0NLScs9nWyAjPSjyq9pHA1DoL0kJEbqQ85cC0gPS8NbSC78sHLkE/qzRpH4INPYkvNy2Kx9SSU3jrJxaC09FleJcCL5iRvfMhUfgwnvOC6OVqnNGUf2GIVCuy@o8AKz7jeb@acL3nzyTh7rGtWNQ@7ejOjfJoYdm4UnXRYwHwDQyFJtqRucgZPEfDhnQff9jKeCc93yBgrHaeoLMvIf7@xyO6tDv@tymXob/@u/gI
