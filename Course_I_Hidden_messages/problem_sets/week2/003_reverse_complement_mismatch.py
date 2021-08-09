def reverse_complement(seq):
    tab = str.maketrans("ACTG", "TGAC")
    return seq.translate(tab)[::-1]

reverse_complement("AAGG")

def read_data(data_path):
    with open(data_path) as f:
        data = f.readlines()
        content = [x.strip() for x in data]
    return content

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


frequent_words_with_mismatch("ACGTTGCATGTCGCATGATGCATGAGAGCT", 4, 1)