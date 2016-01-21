# author: Ashley Scripka Beavers, ashley.scripka@gmail.com
# date: 1/21/16

import sys

VERBOSE = True

# include dummy secret function for testing purposes
def secret(i):
    return i

# The Sieve of Eratosthenes
def get_primes(max_value):
    # iniitialize list of values 0..max_value with each element set to True
    values = [True] * max_value
    # 0 and 1 are not prime, so set these elements to False
    values[0] = False
    values[1] = False
    # iterate through the elements in the list
    for v, primality in enumerate(values):
        # check for primality
        # by definition, we know multiples of a prime number are not prime
        if primality:
            # yield that value, since it is prime and we only want to 
            # "return" values from this generator that are indeed prime numbers
            yield v
            # set primality to False for all multiples of the prime number
            # start with the square of the prime number for optimization
            for n in xrange(v*v, max_value, v):
                values[n] = False

# check for each combination of prime numbers if the secret function is additive
def is_secret_additive(secret, max_value):
    # list comprehension for extracting prime numbers from the get_primes generator objct
    primes = [i for i in get_primes(max_value)]
    # write out the prime numbers below the max_value
    if VERBOSE:
        print "Prime numbers below %i:" % (max_value), primes
    # iterate over the list of prime numbers
    # xrange is great, since it doesn't consume unncessary memory
    for x in xrange(len(primes)):
        # we only need to compare x to y values that are beyond x,
        # since the order of x and y is irrelevant 
        # (i.e. secret(x) + secret(y) = secret(y) + secret(x))
        for y in xrange(x+1, len(primes)):
            if VERBOSE:
                print "Comparing secret(%i) + secret(%i) to secret(%i + %i)..." %\
                    (primes[x], primes[y], primes[x], primes[y])
            # does this pair of values violate additivity? 
            if secret(primes[x]) + secret(primes[y]) != secret(primes[x] + primes[y]):
                if VERBOSE:
                    print "NOT ADDITIVE"
                # we're done! 
                return False
            # we need to keep looking through more pairs of values
            else:
                if VERBOSE:
                    print "ADDITIVE"
    # we were unable to find any pair that violated additivity, 
    # therefore the secret function is additive for these values
    return True

def parse(argv):
    # if no arguments are passed in, show the help
    if len(argv) == 1:
        print "Usage: python assessment.py <integer_value>"
        print "\t <integer_value>: Provide an integer value."
        sys.exit(0)

    # try to convert first value to integer
    try:
        max_value = int(argv[1])
        if max_value <= 2:
            print "ERROR: There are no prime numbers less than %i" % (max_value)
            exit(0)

    # if it cannot be converted, show error and exit
    except ValueError:
        print "ERROR: Input value must be an integer!"
        sys.exit(0)

    # great, we got what we needed
    return max_value

# main program
if __name__ == "__main__":
    # parse the command line arguments
    max_value = parse(sys.argv)
    # determine if the secret function is addtive or not
    additive = is_secret_additive(secret, max_value)
    if additive:
        print "secret function IS additve!"
    else:
        print "secret function is NOT additive!"

