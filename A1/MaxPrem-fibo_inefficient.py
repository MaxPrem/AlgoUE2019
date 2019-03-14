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

def fib(n):
    """F(n) = F(n-1) + F(n-2) """

    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)

def fibonacciOne(n):
   print('\n',fib(n))

def fibonacciAll(a):
    for i in range(a+1):
        print(fib(i), end=", ")

if args.func == 'fibonacciOne':    # if args.cmd=='add': also works
  fibonacciOne(args.n)
if args.func == 'fibonacciAll':
  fibonacciAll(args.a)