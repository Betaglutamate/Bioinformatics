# Here I will attempt to count the occurences of a kmer in a patter

def count_kmer(kmer, pattern):
    num_matches = 0
    for num, _ in enumerate(kmer):
        window = kmer[num: (num+len(pattern))]
        if window == pattern:
            num_matches = num_matches + 1

    return num_matches
            
count_kmer("ACAACTATGCATACTATCGGGAACTATCCT", "ACTAT") #3

#problem set
kmer_to_match = "GGAGGATTCTCCTGAAAAGGATTCAAGCGAGGATTCAAGATATCGCCGTACAGTAGGATTCTAACAGGATTCAGGATTCCTAGACCAAAAGGATTCGACTAGGATTCAGGATTCAGCAAGGATTCAGGATTCAGGATTCTTAGGATTCTGCAGGATTCAGGATTCGAGGATTCTGAGGATTCGCAAGCTCTAGGATTCAGGATTCTTAGGATTCAGGATTCAGAGGATTCAGGATTCAGGATTCGTATGAAAGGATTCCGGAGGATTCCGGGTAGGATTCAGGATTCAAGGATTCAAGGATTCAGGATTCAGGATTCCGAGGATTCAGGATTCGGAGGATTCTTAGGATTCCCAGGATTCACGGGCAGACCTAGGATTCAGGATTCGAAAGGATTCTTGAGGATTCAGGATTCAAAGGATTCCGAGGATTCTAGGATTCGAAGTACCGAGGATTCCCCAGGATTCATGTAGGATTCAGGATTCTAGGATTCGTACGAGGATTCAGGATTCCGTTCTAGGATTCCTTAGGATTCCAGGATTCAGGATTCGGAGGATTCAGAAGGATTCCAGGATTCCTCACAAAATAGGATTCGAGGATTCTAGAGGATTCGCAGGATTCTAAGGATTCATTGTCCAGGATTCTTAAGGATTCAGGATTCAGGATTCAGCCTAGGATTCAGGATTCGGAGGATTCATTCAGGATTCGATCGTGACAGAGGATTCACCAGGATTCTCAGGATTCTAGGATTCAGGATTCGAGGATTCTAGGATTCAAGGATTCAGGATTCGTTATTCACTGGGCAGGATTCAAGGATTCATAGGATTCAGACGCAGGATTCAGGATTCAGGATTCCAGGATTCTGTGAGGATTCATCGAAGGATTCATCCAATAGGATTCCTTTGAGGATTCTAGGATTCGGGCGACTTTAGCAGGATTCGGCCGAAGGATTCAGGATTCATGTTGGTCGCAGGATTCCGCATTTAGTATAGGATTCAGGATTCAGGATTCCGCAAGTTCTGAGGATTCGAGGATTCAGGATTC"
pattern = "AGGATTCAG"

count_kmer(kmer_to_match, pattern)

#OK now I want to find the most frequent Kmer in the dataset

def list_of_all_kmer_in_string(input_string, kmer_length):
    all_kmer = []
    
    for num in range(0, len(input_string) - kmer_length):
        window = input_string[num: (num+kmer_length)]
        all_kmer.append(window)
    
    kmers_unique = list(set(all_kmer)) #this gives you unique kmers

    return kmers_unique


test_new = list_of_all_kmer_in_string(kmer_to_match, 5)


high_match = 0
for kmer in test_new:
    num_matches = count_kmer(kmer_to_match, kmer)
    if num_matches > high_match:
        freq_kmer = kmer
        high_match = num_matches

# note that this is not efficient O^2
# instead it is better to use a frequency table.
# so each KMER gets its own dictionary entry

text = "GGAGGATTCTCCTGAAAAGGATTCAAGCGAGGATTCAAGATATCGCCGTACAGTAGGATTCTAACAGGATTCAGGATTCCTAGACCAAAAGGATTCGACTAGGATTCAGGATTCAGCAAGGATTCAGGATTCAGGATTCTTAGGATTCTGCAGGATTCAGGATTCGAGGATTCTGAGGATTCGCAAGCTCTAGGATTCAGGATTCTTAGGATTCAGGATTCAGAGGATTCAGGATTCAGGATTCGTATGAAAGGATTCCGGAGGATTCCGGGTAGGATTCAGGATTCAAGGATTCAAGGATTCAGGATTCAGGATTCCGAGGATTCAGGATTCGGAGGATTCTTAGGATTCCCAGGATTCACGGGCAGACCTAGGATTCAGGATTCGAAAGGATTCTTGAGGATTCAGGATTCAAAGGATTCCGAGGATTCTAGGATTCGAAGTACCGAGGATTCCCCAGGATTCATGTAGGATTCAGGATTCTAGGATTCGTACGAGGATTCAGGATTCCGTTCTAGGATTCCTTAGGATTCCAGGATTCAGGATTCGGAGGATTCAGAAGGATTCCAGGATTCCTCACAAAATAGGATTCGAGGATTCTAGAGGATTCGCAGGATTCTAAGGATTCATTGTCCAGGATTCTTAAGGATTCAGGATTCAGGATTCAGCCTAGGATTCAGGATTCGGAGGATTCATTCAGGATTCGATCGTGACAGAGGATTCACCAGGATTCTCAGGATTCTAGGATTCAGGATTCGAGGATTCTAGGATTCAAGGATTCAGGATTCGTTATTCACTGGGCAGGATTCAAGGATTCATAGGATTCAGACGCAGGATTCAGGATTCAGGATTCCAGGATTCTGTGAGGATTCATCGAAGGATTCATCCAATAGGATTCCTTTGAGGATTCTAGGATTCGGGCGACTTTAGCAGGATTCGGCCGAAGGATTCAGGATTCATGTTGGTCGCAGGATTCCGCATTTAGTATAGGATTCAGGATTCAGGATTCCGCAAGTTCTGAGGATTCGAGGATTCAGGATTC"


def frequency_table(text, kmer_len):
    freq_map = {}
    nt = len(text)
    nk = kmer_len
    
    for i in range(0, nt-nk):
        pattern = text[i : i+nk]
        if not freq_map.get(pattern):
            freq_map[pattern] = 1
        else:
            freq_map[pattern] = freq_map[pattern] + 1
        
    return freq_map

freq_map = frequency_table(text, 5)

max(freq_map, key=freq_map.get) # this is the easy way to get the highest freq one

test_pattern = "TATGCTAGGTCCAAGTCCAATATATGCTAGCTCTACGTCCAATATATGCTAGTCCAATAGTCTTCTTCCAATAGTCCAAGGTCTTCTCTCTACGGTCTTCTTATGCTAGCTCTACGCTCTACGTATGCTAGTCCAATACTCTACGTATGCTAGGTCCAAGGTCTTCTTATGCTAGGTCTTCTCTCTACGCTCTACGTATGCTAGTATGCTAGCTCTACGGTCCAAGCTCTACGTCCAATACTCTACGTATGCTAGGTCCAAGGTCTTCTGTCTTCTTCCAATATCCAATAGTCCAAGTATGCTAGGTCCAAGGTCTTCTGTCTTCTGTCCAAGGTCCAAGGTCCAAGCTCTACGGTCTTCTTATGCTAGCTCTACGTATGCTAGGTCCAAGTCCAATATCCAATATATGCTAGTCCAATATCCAATAGTCTTCTGTCTTCTCTCTACGCTCTACGGTCCAAGGTCCAAGTCCAATATATGCTAGGTCCAAGGTCTTCTTATGCTAGGTCTTCTTCCAATAGTCTTCTGTCCAAGTCCAATAGTCCAAGGTCTTCTGTCTTCTTATGCTAGTATGCTAGGTCTTCTTCCAATATCCAATATCCAATATCCAATAGTCCAAGCTCTACGTCCAATATATGCTAGTATGCTAGCTCTACGGTCCAAGTATGCTAGCTCTACGTCCAATAGTCTTCTTCCAATATATGCTAGCTCTACGGTCCAAGCTCTACGTCCAATAGTCTTCTTATGCTAGCTCTACGGTCCAAGGTCCAAGTATGCTAGGTCTTCTGTCCAAGTCCAATACTCTACGTATGCTAGGTCTTCTTATGCTAGGTCTTCTGTCTTCTCTCTACGGTCTTCTCTCTACGGTCTTCTCTCTACG"
test_pattern_1 = "CTTCCCAAAGACTTCTCTGATGTAGCAAAGACTTCTCTCGCTTTGCCGGTCTCGAGGATGTAGCAAAGACTTCTCTAGACTTCTCTAGACTTCTCTCTTCCCAACTTCCCAAGTCTCGAGGATGTAGCAAGATGTAGCAACGCTTTGCCGCTTCCCAAGTCTCGAGAGACTTCTCTGTCTCGAGCTTCCCAACGCTTTGCCGGTCTCGAGGTCTCGAGCTTCCCAAGTCTCGAGCTTCCCAACGCTTTGCCGCTTCCCAAGTCTCGAGCTTCCCAACTTCCCAAGTCTCGAGGTCTCGAGCTTCCCAAAGACTTCTCTGTCTCGAGCTTCCCAAAGACTTCTCTCTTCCCAACGCTTTGCCGCTTCCCAACGCTTTGCCGGATGTAGCAAAGACTTCTCTCGCTTTGCCGCGCTTTGCCGGATGTAGCAAAGACTTCTCTAGACTTCTCTCTTCCCAACGCTTTGCCGAGACTTCTCTCTTCCCAAGATGTAGCAACGCTTTGCCGGTCTCGAGCGCTTTGCCGGATGTAGCAAGTCTCGAGCTTCCCAAGATGTAGCAAGTCTCGAGCGCTTTGCCGGATGTAGCAAAGACTTCTCTCTTCCCAAGTCTCGAGCTTCCCAAAGACTTCTCTAGACTTCTCTGTCTCGAGGATGTAGCAAGTCTCGAGCTTCCCAAAGACTTCTCTAGACTTCTCTAGACTTCTCTCTTCCCAACTTCCCAAGTCTCGAGGTCTCGAGGTCTCGAGGTCTCGAGGTCTCGAGGATGTAGCAACTTCCCAACTTCCCAAAGACTTCTCTAGACTTCTCTGATGTAGCAACTTCCCAACGCTTTGCCGGTCTCGAGAGACTTCTCTGATGTAGCAACTTCCCAAGATGTAGCAAGTCTCGAGGTCTCGAGCGCTTTGCCGGATGTAGCAAAGACTTCTCTAGACTTCTCTGATGTAGCAAGTCTCGAGGATGTAGCAAAGACTTCTCT"
test_length = 11

freq_map = frequency_table(test_pattern_1, test_length)

max_value = max(freq_map.values())

[k for k,v in freq_map.items() if v == max_value]