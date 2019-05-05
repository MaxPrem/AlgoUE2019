#!/usr/bin/python3

"""
Needleman Wunsch Algorithm
Max Prem
./MaxPrem-NW.py < file.fasta

"""
from Bio import SeqIO
from argparse import ArgumentParser

parser = ArgumentParser(description="Needleman-Wunsch algorithm for global sequences alignment")
parser.add_argument("--match", type=int, default=1, help="enter a user defined value for match score, default = 1")
parser.add_argument("--mismatch", type=int, default=-1, help="Enter mismatching score for "
                                                             "sequence alignment, default = -1")
parser.add_argument("--gap", type=int, default=-2, help="Enter gap penalty, default = -2")
args = parser.parse_args()

### user defined values scoringFunction
match = args.match
mismatch = args.mismatch
gap = args.gap


def scoringFunction(pos1, pos2):
    """returns score value for given pair"""
    if pos1 == pos2:
        return match
    if pos1 == '-' or pos2 == '-':
        return gap
    return mismatch


def createMatrix(rows, columns):
    matrix = []
    for i in range(rows):
        matrix.append([])
        for j in range(columns):
            matrix[-1].append(0)
    return matrix

def createScoringMatrix(seq1, seq2):
    """creates Scoring Matrix with Needleman Wunsch algorithm"""
    m = len(seq1)
    n = len(seq2)

    # empty matrix
    scoringMatrix = createMatrix(m+1, n+1)

    # build scores, fill matrix
    for i in range(0, m + 1):
        scoringMatrix[i][0] = gap * i
    for j in range(0, n + 1):
        scoringMatrix[0][j] = gap * j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            match = scoringMatrix[i - 1][j - 1] + scoringFunction(seq1[i - 1], seq2[j - 1])
            delete = scoringMatrix[i - 1][j] + gap
            insert = scoringMatrix[i][j - 1] + gap
            scoringMatrix[i][j] = max(match, delete, insert)

    return scoringMatrix


def getAlignment(seq1, seq2, score):
    """takes two sequences and a scoring matrix and returns aligned sequences"""
    i = len(seq1)
    j = len(seq2)
    alignedseq1 = ""
    alignedseq2 = ""
    while True:

        if i == 0 and j == 0:
            break
        if j == 0:
            alignedseq1 += seq1[i - 1]
            alignedseq2 += '-'
            i -= 1
            continue
        if i == 0:
            alignedseq1 += '-'
            alignedseq2 += seq2[j - 1]
            j -= 1
            continue
        if score[i][j] == score[i-1][j] + gap:
            alignedseq1 += seq1[i - 1]
            alignedseq2 += '-'
            i -= 1
        elif score[i][j] == score[i][j-1] + gap:
            alignedseq1 += '-'
            alignedseq2 += seq2[j - 1]
            j -= 1
        elif score[i][j] == score[i-1][j-1] + scoringFunction(seq1[i - 1], seq2[j - 1]):
            alignedseq1 += seq1[i - 1]
            alignedseq2 += seq2[j - 1]
            i -= 1
            j -= 1

    return alignedseq1, alignedseq2


def compareAlignment(alignedseq1, alignedseq2):

    # reverse sequences
    alignedseq1 = alignedseq1[::-1]
    alignedseq2 = alignedseq2[::-1]

    # calculate similarity, score and aligned sequences
    score = 0
    sim = 0

    for i in range(0, len(alignedseq1)):
        # check match
        if alignedseq1[i] == alignedseq2[i]:
            sim += 1
            score += scoringFunction(alignedseq1[i], alignedseq2[i])
        #check gap
        elif alignedseq1[i] != alignedseq2[i] and alignedseq1[i] != '-' and alignedseq2[i] != '-':
            score += scoringFunction(alignedseq1[i], alignedseq2[i])
        # mismatch
        else:
            score += gap

    sim = float(sim) / len(alignedseq1) * 100

    return sim, score


def main():

### reading File
    idList = []
    seqList = []

    if sys.stdin.isatty():
        parser.print_help()
    for Sequence in SeqIO.parse(stdin, "fasta"):
        idList.append(str(Sequence.id))
        seqList.append(str(Sequence.seq).lower())

    seq1 = seqList[0]
    seq2 = seqList[1]
    seqID1 = idList[0]
    seqID2 = idList[1]

#   computing results

    scoringMatrix = createScoringMatrix(seq1, seq2)
    alignedseq1, alignedseq2 = getAlignment(seq1, seq2, scoringMatrix)
    signs = ""

    for i in range(0, len(alignedseq1)):
        if alignedseq1[i] is alignedseq2[i]:
            signs += "*"
        else:
            signs += " "
    path1 = alignedseq1[::-1]
    path2 = alignedseq2[::-1]
    signs = signs[::-1]
    rowClustal = len(seq1) / 60

    # printing results in CLUSTAL format
    print("CLUSTAL\n\n")
    for i in range(1, int(rowClustal) + 2):
        if i == int(rowClustal) + 2 and rowClustal > int(rowClustal):
            print(seqID1, path1[60 * (i - 1)::])
            print(seqID2, path2[60 * (i - 1)::])
            print("".ljust(len(seqID1)), signs[60 * (i - 1)::], "\n")
            break
        print(seqID1, path1[60 * (i - 1):60 * i])
        print(seqID2, path2[60 * (i - 1):60 * i])
        print("".ljust(len(seqID1)), signs[60 * (i - 1):60 * i], "\n")

    sim, score = compareAlignment(alignedseq1, alignedseq2)
    sys.stderr.write(str(sim))

    # printing results to stderr
    print("identity: %3.3f " % sim + "%", file=sys.stderr)
    print("score: ", score, file=sys.stderr)


if __name__ == "__main__":
    # read from stdin
    import sys
    from sys import stdin
    main()

