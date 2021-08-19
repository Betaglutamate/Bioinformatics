import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def find_skew_list(text):
    skew_list = []
    skew = 0

    for i in text:
        if i == "C":
            skew = skew - 1
        elif i == "G":
            skew = skew + 1
    
        skew_list.append(skew)

    return skew_list

with open("../../Data/Salmonella_enterica.txt") as f:
    genome = f.read()

d=open("../../Data/Salmonella_enterica.txt").readlines()


#Now because of the format the genome is in i need to remove header and shizz

split = genome.split("\n")
final_g = "".join(split[1:])



pd.DataFrame(skew_array).plot()

def find_min_skew(genome):
    skew_array = find_skew_list(genome)
    min_value = min(skew_array)

    min_index = np.where(np.array(skew_array) == min_value)[0]+1
    return min_index

min_skew = find_min_skew(final_g)[0]


Dna_window = final_g[min_skew-500: min_skew+500]

def reverse_complement(seq):
    tab = str.maketrans("ACTG", "TGAC")
    return seq.translate(tab)[::-1]

reverse_complement("AAGG")


def neighbours(pattern, d):
    """
    this function takes a kmer and generates all possible kmers
    with a hamming distance of 1
    """
    pattern_list = set()
    nucleotides = ['A', 'T', 'C', 'G']

    for i in range(len(pattern)):
        for nucleotide in nucleotides:
            new_pattern = list(pattern)
            new_pattern[i] =  nucleotide
            new_pattern = "".join(new_pattern)
            pattern_list.add(new_pattern)
    
    return list(pattern_list)




def frequent_words_with_mismatch(text, k, d):
    """
    Text in a DNA string, 
    k is the length of the kmer we are looking for,
    d is the number of tolerated mismatches
    """
    #I need to generate all kmers
    patterns = []
    freq_map = {}
    n = len(text)
    directions = [text, reverse_complement(text)]

    for direct in directions:

        for i in range(n-k+1):
            pattern = direct[i:i+k]
            neighborhood = neighbours(pattern, 1)

            for j in range(len(neighborhood)):
                neighbour = neighborhood[j]
                if not freq_map.get(neighbour):
                    freq_map[neighbour] = 1
                else:
                    freq_map[neighbour] = freq_map[neighbour] + 1


        max_value = max(freq_map.values())
        m = [k for k,v in freq_map.items() if v == max_value]

    return m


frequent_words_with_mismatch(Dna_window, 9, 1)

from itertools import chain, combinations, product

def hamming_circle(s, n, alphabet):
    """Generate strings over alphabet whose Hamming distance from s is
    exactly n.

    >>> sorted(hamming_circle('abc', 0, 'abc'))
    ['abc']
    >>> sorted(hamming_circle('abc', 1, 'abc'))
    ['aac', 'aba', 'abb', 'acc', 'bbc', 'cbc']
    >>> sorted(hamming_circle('aaa', 2, 'ab'))
    ['abb', 'bab', 'bba']

    """
    for positions in combinations(range(len(s)), n):
        for replacements in product(range(len(alphabet) - 1), repeat=n):
            cousin = list(s)
            for p, r in zip(positions, replacements):
                if cousin[p] == alphabet[r]:
                    cousin[p] = alphabet[-1]
                else:
                    cousin[p] = alphabet[r]
            yield ''.join(cousin)

from itertools import chain, combinations, product

def hamming_circle(s, n, alphabet):
    """Generate strings over alphabet whose Hamming distance from s is
    exactly n.

    >>> sorted(hamming_circle('abc', 0, 'abc'))
    ['abc']
    >>> sorted(hamming_circle('abc', 1, 'abc'))
    ['aac', 'aba', 'abb', 'acc', 'bbc', 'cbc']
    >>> sorted(hamming_circle('aaa', 2, 'ab'))
    ['abb', 'bab', 'bba']

    """
    for positions in combinations(range(len(s)), n):
        for replacements in product(range(len(alphabet) - 1), repeat=n):
            cousin = list(s)
            for p, r in zip(positions, replacements):
                if cousin[p] == alphabet[r]:
                    cousin[p] = alphabet[-1]
                else:
                    cousin[p] = alphabet[r]
            yield ''.join(cousin)

def hamming_ball(s, n, alphabet):
    """Generate strings over alphabet whose Hamming distance from s is
    less than or equal to n.

    >>> sorted(hamming_ball('abc', 0, 'abc'))
    ['abc']
    >>> sorted(hamming_ball('abc', 1, 'abc'))
    ['aac', 'aba', 'abb', 'abc', 'acc', 'bbc', 'cbc']
    >>> sorted(hamming_ball('aaa', 2, 'ab'))
    ['aaa', 'aab', 'aba', 'abb', 'baa', 'bab', 'bba']

    """
    return chain.from_iterable(hamming_circle(s, i, alphabet)
                               for i in range(n + 1))

res = "\n".join(list(hamming_ball("GTACTTGACCG", 2, "ATGC")))

f = open("test.txt", "a")
f.write(res)
f.close()
