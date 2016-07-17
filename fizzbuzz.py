#!python

# Fizz Buzz:
# Iterate over numbers pringing Fizz if the numbers
# is divisible by 3 say Fizz
# if divisible by 5 say Buzz
# if divisible by 3 and 5 say Fizz Buzz
# if divisibly by neither say number

for number in range(0,16):
#    if (number % 3 == 0) and (number % 5 == 0):
#        print "Fizzbuzz"
    result = ""
    if number % 3 == 0:
        result += "Fizz"
    if number % 5 == 0:
        result += "Buzz"
    if len(result) == 0:
        result = number
    print result
