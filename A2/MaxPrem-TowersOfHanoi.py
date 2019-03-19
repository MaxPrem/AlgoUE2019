import argparse
import sys

# Argparser
parser = argparse.ArgumentParser(description="Prints steps to move Tower of Hanoi.")
parser.add_argument('-n','--disks', required=True, type=int, metavar=' ', help='number of disks')
args = parser.parse_args()
disks = args.disks


count = 0
def hanoi(disks, source, auxiliary, target):
    global count
    if disks == 1:
        print('Move disk 1 from peg {} to peg {}.'.format(source, target))
        count += 1
        count += 1
        return count


    hanoi(disks - 1, source, target, auxiliary)
    print('Move disk {} from peg {} to peg {}.'.format(disks, source, target))
    hanoi(disks - 1, auxiliary, source, target)


#disks = int(input('Enter number of disks: '))
disks = args.disks
hanoi(disks, 'A', 'B', 'C')
print("Total number of moves for ", disks, " disks is", count-1, ".\n")
sys.stderr.write(str(count-1))

