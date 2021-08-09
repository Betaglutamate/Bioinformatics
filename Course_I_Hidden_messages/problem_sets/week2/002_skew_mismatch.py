def read_data(data_path):
    with open(data_path) as f:
        data = f.readlines()
        content = [x.strip() for x in data]
    return content

df = read_data("dataset_9_3.txt")

def count_mismatch(str1, str2):
    mismatch_count = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            mismatch_count = mismatch_count +1
    
    return mismatch_count

def count_mismatch_pattern(pattern, text, mismatch_all):
    positions = []
    for i in range(len(text)-len(pattern)+1):
        mismatch_count = count_mismatch(text[i : i+len(pattern)], pattern)
        if mismatch_count <= mismatch_all:
            positions.append(i)
    
    return positions

# count of total matchs allowing for mismatch

data = read_data("dataset_9_6.txt")
len(count_mismatch_pattern(data[0], data[1], 2))



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
    for i in range(n-k+1):
        pattern = text[i:i+k]
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


frequent_words_with_mismatch("ACGTTGCATGTCGCATGATGCATGAGAGCT", 4, 1)


data = read_data("dataset_9_9.txt")

frequent_words_with_mismatch(data[0], 6, 2)

## answer to help debug my answer
# import itertools
# import time
# from collections import defaultdict

# def FrequentWordsWithMismatches(Genome, k, d):
#     start = time.process_time()
#     aprox_frq_words = []
#     frequencies = defaultdict(lambda: 0)
#     # all existent kmers with d mismatches of current kmer in genome
#     for index in range(len(Genome) - k + 1):
#         curr_kmer_and_neighbors = PermuteMotifDistanceTimes(Genome[index : index + k], d)
#         for kmer in curr_kmer_and_neighbors:
#             frequencies[kmer] += 1 

#     for kmer in frequencies:
#         if frequencies[kmer] == max(frequencies.values()):
#             aprox_frq_words.append(kmer)
#     end = time.process_time()
#     print("Time:", end - start)
#     return aprox_frq_words


# def PermuteMotifOnce(motif, alphabet={"A", "C", "G", "T"}):
#     """
#     Gets all strings within hamming distance 1 of motif and returns it as a
#     list.
#     """

#     return list(set(itertools.chain.from_iterable([[
#         motif[:pos] + nucleotide + motif[pos + 1:] for
#         nucleotide in alphabet] for
#         pos in range(len(motif))])))


# def PermuteMotifDistanceTimes(motif, d):
#     workingSet = {motif}
#     for _ in range(d):
#         workingSet = set(itertools.chain.from_iterable(map(PermuteMotifOnce, workingSet)))
#     return list(workingSet)