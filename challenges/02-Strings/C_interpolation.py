# Lastly, we'll see how we can put some data into our strings

# Interpolation
## There are several ways python lets you stick data into strings, or combine
## them. A simple, but very powerful approach is to us the % operator. Strings
## can be set up this way to present a value we didn't know when we defined the
## string!

s = 'this string is %d characters long'

s_len = len(s)

## We can apply values to a string with an expression that goes:
## string % value(s)
## if there's more than one, put them in ()'s with commas between!

## Go ahead and compute the length of s and substitute it into the string:

print s % s_len

# conversion
## Adding a string and a number together doesn't make sense... for example,
## what's the right thing to do for '1.0' + 2? Let's explore both ways that
## could go. First, we need to do the conversion ourselves. Remember, you can
## use the type functions to do that, in this case, str() and float() - int()
## would lose the decimal point that is clearly there for a reason!

a = 1.0
b = 2

print str(a) + str (b)

print float(a) + float(b)

print 'as added numbers'
