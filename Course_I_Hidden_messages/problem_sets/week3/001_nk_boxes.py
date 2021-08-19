"""
Exercise Break: What is the expected number of occurrences of a 9-mer in 500 random DNA strings, each of length 1000?
 Assume that the sequences are formed by selecting each nucleotide (A, C, G, T) with the same probability (0.25).
"""

#how many different 9mer are there?
ninemer = 4**9

#how many ninemers are there in a string of 1000

(992/ninemer)*500