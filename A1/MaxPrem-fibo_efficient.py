import argparse
# Create Parser and Subparser
parser = argparse.ArgumentParser(description="calculate fibonacci number'")
subparser = parser.add_subparsers(dest='cmd', help="commands")

# Make Subparsers
fibonacciOne_parser = subparser.add_parser('n', help="function to print nth fibonacci number")
fibonacciOne_parser.add_argument("n", type=int, help='[n] fibonacci number')
fibonacciOne_parser.set_defaults(func='fibonacciOne')

fibonacciAll_parser = subparser.add_parser('a', help="function to print all numbers including nth ")
fibonacciAll_parser.add_argument("a", type=int, help='numbers up to nth position')
fibonacciAll_parser.set_defaults(func='fibonacciAll')

args = parser.parse_args()
print(args)

def fibonacci(n):
    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        n_minus1 = 1
        n_minus2 = 0
        for f in range(1, n):
            result = n_minus2 + n_minus1
            n_minus2 = n_minus1
            n_minus1 = result
    return result

def fibonacciOne(n):
   print('\n',fibonacci(n))

def fibonacciAll(a):
    for i in range(a+1):
        print(fibonacci(i), end=", ")

if args.func == 'fibonacciOne':    # if args.cmd=='add': also works
  fibonacciOne(args.n)
if args.func == 'fibonacciAll':
  fibonacciAll(args.a)