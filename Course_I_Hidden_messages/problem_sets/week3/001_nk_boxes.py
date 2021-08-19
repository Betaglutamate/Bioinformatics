"""
Exercise Break: What is the expected number of occurrences of a 9-mer in 500 random DNA strings, each of length 1000?
 Assume that the sequences are formed by selecting each nucleotide (A, C, G, T) with the same probability (0.25).
"""

#how many different 9mer are there?
ninemer = 4**9

#how many ninemers are there in a string of 1000

(992/ninemer)*500

import itertools, random
from cacheout import Cache
import time

all_c=set('AGCT')
get_other = lambda x : list(all_c.difference(x))

other={}
for c in all_c:
    other[c]=get_other(c) 


def get_changed(sub, i):
    return [sub[0:i]+c+sub[i+1:] for c in other[sub[i]]]

mmatchHash=Cache(maxsize=256*256, ttl=0, timer=time.time, default=None)

def get_mismatch(d, setOfMmatch):
    
    if d==0:
        
        return setOfMmatch
    
    newMmatches=[]
    for sub in setOfMmatch:
        newMmatches.extend(list(map(lambda x : ''.join(x), itertools.chain.from_iterable(([get_changed(sub, i)  for i, c in enumerate(sub)])))))
    
    setOfMmatch=setOfMmatch.union(newMmatches)
    
    if not mmatchHash.get((d-1, str(setOfMmatch)), 0):
        mmatchHash.set((d-1, str(setOfMmatch)), get_mismatch(d-1, setOfMmatch))
        
    return mmatchHash.get((d-1, str(setOfMmatch)))


length_of_DNA=1000
dna=''.join(random.choices('AGCT', k=length_of_DNA))
hamm_dist=4
length=9

len(list(itertools.chain.from_iterable([get_mismatch(hamm_dist, {dna[i:i+length]}) for i in range(len(dna)-length+1)])))
# set(itertools.chain.from_iterable([get_mismatch(hamm_dist, {dna[i:i+length]}) for i in range(len(dna)-length+1)]))


def nk_box(dna, k, d):
    patterns = set()
    for k in dna:
        for 

MotifEnumeration(Dna, k, d)
        Patterns ← an empty set
        for each k-mer Pattern in the first string in Dna
            for each k-mer Pattern’ differing from Pattern by at most d mismatches
                if Pattern' appears in each string from Dna with at most d mismatches
                    add Pattern' to Patterns
        remove duplicates from Patterns
        return Patterns