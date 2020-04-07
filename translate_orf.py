#! /usr/bin/env python3

#script to translate the first ORF found in a nucleotide sequence
def main():
    import sys
    import find_orf
    import translate
    import argparse
def main():
    import argparse

    # Create a command-line parser object
    parser = argparse.ArgumentParser(
            formatter_class = argparse.ArgumentDefaultsHelpFormatter)

<<<<<<< HEAD
    # Tell the parser what command-line arguments this script can receive
    parser.add_argument('sequence',
            metavar = 'SEQUENCE',
            type = str,
            help = ('The sequence to search for an open-reading frame. '
                    'If the path flag (\'-p\'/\'--path\') is specified, '
                    'then this should be a path to a file containing the '
                    'sequence to be searched.'))
    parser.add_argument('-p', '--path',
            action = 'store_true',
            help = ('The sequence argument should be treated as a path to a '
                    'containing the sequence to be searched.'))
    parser.add_argument('-s', '--start-codons',
            type = str,
            nargs = '+', # one or more arguments
            default = ['AUG'],
            help = ('One or more possible start codons.'))
    parser.add_argument('-x', '--stop-codons',
            type = str,
            nargs = '+', # one or more arguments
            default = ['UAA', 'UAG', 'UGA'],
            help = ('One or more possible stop codons.'))
=======
p = argparse.ArgumentParser(description=usage)
p.add_argument('Path'
        metavar='path',
        type=str
        help='the path to list'
>>>>>>> 61c7a46c812d3d652eb32691b2ef553477f8c7bc

    # Parse the command-line arguments into a 'dict'-like container
    args = parser.parse_args()

    # Check to see if the path option was set to True by the caller. If so, parse
    # the sequence from the path
    if args.path:
        sequence = parse_sequence_from_path(args.sequence)
    else:
        sequence = args.sequence

    orf = find_first_orf(sequence = sequence,
            start_codons = args.start_codons,
            stop_codons = args.stop_codons)
    sys.stdout.write('{}\n'.format(orf))


if __name__ == '__main__':
    main()
    p = argparse.ArgumentParser(descritption=usage)
    p.add_argument('Path'
            metavar='path',
            type=str
            help='the path to list'

    p.add_argument(

    p.add_argument(

    args = p.parse_args()

    print(args.input)

    genetic_code = {'GUC': 'V', 'ACC': 'T', 'GUA': 'V', 'GUG': 'V', 'ACU': 'T', 'AAC': 'N', 'CCU': 'P', 'UGG': 'W', 'AGC': 'S', 'AUC': 'I', 'CAU': 'H', 'AAU': 'N', 'AGU': 'S', 'GUU': 'V', 'CAC': 'H', 'ACG': 'T', 'CCG': 'P', 'CCA': 'P', 'ACA': 'T', 'CCC': 'P', 'UGU': 'C', 'GGU': 'G', 'UCU': 'S', 'GCG': 'A', 'UGC': 'C', 'CAG': 'Q', 'GAU': 'D', 'UAU': 'Y', 'CGG': 'R', 'UCG': 'S', 'AGG': 'R', 'GGG': 'G', 'UCC': 'S', 'UCA': 'S', 'UAA': '*', 'GGA': 'G', 'UAC': 'Y', 'GAC': 'D', 'UAG': '*', 'AUA': 'I', 'GCA': 'A', 'CUU': 'L', 'GGC': 'G', 'AUG': 'M', 'CUG': 'L', 'GAG': 'E', 'CUC': 'L', 'AGA': 'R', 'CUA': 'L', 'GCC': 'A', 'AAA': 'K', 'AAG': 'K', 'CAA': 'Q', 'UUU': 'F', 'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'GCU': 'A', 'GAA': 'E', 'AUU': 'I', 'UUG': 'L', 'UUA': 'L', 'UGA': '*', 'UUC': 'F'}
