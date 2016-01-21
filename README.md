# Additivity 

###Problem Statement
You are given a function 'secret()' that accepts a single integer parameter and returns an integer. In your favorite programming language, write a command-line program that takes one command-line argument (a number) and determines if the secret() function is additive [secret(x+y) = secret(x) + secret(y)], for all combinations x and y, where x and y are all prime numbers less than the number passed via the command-line argument.  Describe how to run your examples.

### Command-Line Application Usage

**NOTE: This program uses Python 2.7**

To see the help output, from within the root repository directory, run:

```
python additivity.py
```

This will produce the following output:

```
Usage: python assessment.py <integer_value>
	 <integer_value>     REQUIRED : Provide an integer value.
```

To execute the program, run:

```
python additivity.py <integer>
```

Setting the VERBOSE flag at the top of additivity.py to True will produce fine grained output as the program runs to provide more visibility into its status at various points along the way.

