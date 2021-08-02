

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

import re

def find_clumps(text, kmer, L, t):
    '''
    This function takes an input sequence text
    k is a kmer length that you want to find
    L is the length of the region you want to find
    t is the number of times the kmer is supposed to present
    '''
    patterns = []
    n = len(text)
    for i in range(0, n-L):
        window = text[i:i+L]
        freq_map = frequency_table(window, kmer)
        for k in freq_map.keys():
            if freq_map[k] >= t:
                patterns.append(k)
                
        
        unique_patterns = list(set(patterns))
    return unique_patterns
            


# FindClumps(Text, k, L, t)
#     Patterns ← an array of strings of length 0
#     n ← |Text|
#     for every integer i between 0 and n − L
#         Window ← Text(i, L)
#         freqMap ← FrequencyTable(Window, k)
#         for every key s in freqMap
#             if freqMap[s] ≥ t
#                 append s to Patterns
#     remove duplicates from Patterns
#     return Patterns

s_text = "CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA"
k = 5 
L = 50
t = 4


with open("..\Data\E_coli.txt") as f:
    s_try = f.read()


a = frequency_table(s_try, 9)


find_clumps(s_try, 9, 500, 3)


## more efficient

def find_clump_new(text, kmer, L, t):
    patterns = []
    list_all_kmer = frequency_table(text, kmer)
    list_all_kmer = [k for k in list_all_kmer.keys()]
    
    for i in range(0, len(text)-L, L):
        window = text[i : i+L]
        print(window)
        print(list_all_kmer)
        for k in list_all_kmer:
            num_times = len(re.findall(f'(?={k})', window))
            if num_times >= t:
                patterns.append(k)
    
    return patterns


find_clump_new(s_text, k, L, 3)



find_clump_new(s_try, 9, 500, 3)