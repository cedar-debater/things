# Numberless

## Input and Output

Your program should print the one-digit numbers (`0123456789`) in any order.

## Restrictions

If you remove all occurrences of a number from your code, your code should print that number. It is allowed to then raise an error (for convenience) - no extra marks for this though.

## Scoring

Lowest number of bytes wins (this *is* <kbd>code-golf</kbd>, after all)

## Sanbdox things

<!-- pls keep the typo -->

* Anything I should change?

## Example

### [Python 3.8 (pre-release)], 103 bytes

<!-- language-all: lang-python -->

    k = '0123456789'
    for i in'abcdefghij':
     if str(j:=ord(i)-ord('a'))not in k:print(j);break
    else:print(k)
    
Explain:

    k = '0123456789' # all the numbers (possibly) minus one number
    for i in 'abcdefghij':
     ... j := ord(i) - ord('a')
    # equal to:
    # for j in range(10)
    # but we can't put numbers here
    # then:
    for j in range(10):
     if str(j) not in k:
      print(j); break #print the removed number and break
    else:
     # this is run if no break
     # that means all numbers are there
     # so print the numbers
     print(k)
    

[Try it online!][TIO-ktt93g9y]

<kbd>code-golf</kbd>

[Python 3.8 (pre-release)]: https://docs.python.org/3.8/
[TIO-ktt93g9y]: https://tio.run/##LcpBDsIgEEDRPaeY3TCLJmqrrZgehrZgBwyQKRtPj5q4@snLL@@659RPRVqLMAOezpd@uN7G6Y7KZwEGTmiXdXP@uXNAo4A9HFV0MHOWTTN1v6BFopTrd4doinCqOtBjEWejcq/D/S1Sax8 "Python 3.8 (pre-release) – Try It Online"
