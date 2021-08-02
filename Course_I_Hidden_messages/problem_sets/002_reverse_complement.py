# inverse maker

def make_complement(input_string):
    reverse_complement = []
    for l in input_string:
        if l == "A":
            O = "T"
        elif l == "T":
            O = "A"
        elif l == "C":
            O = "G"
        elif l == "G":
            O = "C"
        reverse_complement.append(O)
    reverse_comp = ''.join(reverse_complement)[::-1]
    
    return reverse_comp

test_string = "CGTTATGAACTATAGAGTTTCCTGAATCTTCGTTGAAGATCCGGAAGACCGAGGTCATCCGTAAGCCTTGCTCTCTGGGTGCATCCAGACGAATTTCTCATTCGTTGGAAGGCTAGCGGAACCGACCCACTATTTTTCAAACCTCGACCGCACCACCCCGGCGCGCGGCCCTTCCTTGATGTGTTAAGACGGTATATAGGTCTACGAGAAGGATCTCCCTTCAAAGCCCCGTATAATCCGCGCGAAATGGCTTGAGCCAATAGTTCTGTACCAACATTCACTGCATTCTTCAGATTCTAAAGTCTGTAAATCCTGCGAGCGAGCGTGGGTCTCTAGCTTGTCAGTGAGAAGCACCTCTGGTCTCAATTTGAATCGAATCCGGTGATTTGTGAAACAGTGCGATTCGTAACACAATGGCATTGCTCAAGTGAATTATCTGGCGTACCCAGCCTTCTGTTTTTGAATGTTGCCCAAATGCAACCAATCAATCGGCCTCCGAAACCAACCTGCAGCAATACAGTTTATCCGCTACATCCATTCGCCACCAGTCATTTTATCTGACGCAATTTATCAACAATGTGGTGGCATACTCTACACGCTAATCTCTGGGTGGGGCAAAAGGGTGAGTGTTATCCCAGTATCCAAAACAACACCCTGGTTAACCACCTAGGGACGATGGCTGTATGCAGTCGAAGGACTGCGCCTTTGTTCGTCAGCCTATCAGCTCCAGGCATCAATACTAAGGTGGGCTCACTTTTGGCTCTGGCGTGCCCGCCGTTACTACAGGTTTGTGTATGTTGGCCCGGATTGATCAAGGGACGTCTGACTGTGTAATGACTATATGGTGGGGGGTTTGTGGCTAGCTGGGTTGGCGTCTAATTCTCGCAGCCCCCCGCGTACCTATGATCGCGCAGGTCGCGCCGTGGAAGCATCACTGTGGGAAATGTAGTCATATCGCCCAATTGGGAGGGGGCGCGGTAAGTATGTATTTGGGGCAGACACCCACCTCGCTAAGCTGCCTGCTTCCGAGGAGTGTCGTACTGGCTAGCTGGCGTAGCCTTAGGATTCTTGCGCTTCGTGAGGTGAATCTGAAGTGTAGTTTGGACTATAGAAAACGAGGAGCCACTACATCGATCAGAATAGCTTCGACTATTCCCACCAGTGAAAAGCAGCCACATAGCTTTTAAATTGCTATGGTTTGGCTGGAAATGATGTTGGGAGATATGATTTCAACGTGCCGTACGCTCTGCTGTTTGTGAGCAATGACATTGGCACGTCGTTATAGCCGTCGCGTTTATGTTGTACAAACTCTGCGAGTTTCTCCAGACTATATTCCCCCAAGAGCAAATGGCACCCCTTGCTCGTCACGTCTTAGTACCAGCTTCTTCGTAGTGCACACCAACTACTCAGTATTGACTCAGTATCAGTACCAGAATGTTTATGTCGGGCGAGTCTCATTAACGTTTTACATGAGTAAACGACGGTTTCTGAATGACGTGGTTGCCTAATGTAGCGATCTTGACCTATTTTAGCGGCTGTGGAAAATTCAATTGATGTGCGTCAAACATAGCTTGGTCAGAGCAATTGCAGCTTAATGACCAGAATACTCTTCTCCGCGGTATCCCATCGGCTATAACTGTGAGGCCACATGCTCGCTGCCATACCGAAAGGGGGTGAAATCGAAATTCACACCCGGCGGGAATCCTTTTATCTGATTTCAATGGTGCGGGCGGCAGGGTCGTAGTCAGAATACCAACAATACTTTAGACACACGATTTTTCGGTGAGCCGTAGCATTTTGGTTACTAACTAGCCCCGCTATACAAACTCGTTCAGTGCGTTAAATAGGGAACATAACTGACCAAGACTGAGCCGTGCACTGAAATTTGAAATACCGCCCCAAGCAGAAATCAAGTGGTAAACTAATCAAAAGTCATATTATCTCGTTAGAGGCGAGGAAAATGTTCTGGCCCAGCACTAGAGAAGGCTACCACTACTCGGATCCGTTCTTTCCACGCGACGCAATAATTCCGGTCCGAACAACGTCTTAAGGATATCTACGAGCTGGGAGCGGGGTCCTTTCGTACGCTGTTCCCGAAACCTGCGCGTGGAAAAAAGATGGATTCTGGTCGTGCTAATAGAGGCTCATATTTACCAGTAGTCTTACTTGAGCGTAAGATAGGTCGTCAACGGCGTTTCATTCCCTGGAAAAAGCGACTTGCTACGGTGCGGGCTTTTTCTCATGGAGTTGCTGGAGGACATTATCACGCATGTAAGACAAGATGCCGAGAGTGTATGTAGCGGGAAATGTGACGAGCCAGTAAAAACATGCGTCAGGATTTCGCGCGTGCATATACCCCCGGATCTTAAATGACCCCACGCTACTGAGTACGTTCGCGAACATCTCCCCTAGCAACTACCGTGTAAGAGAGCGACGTGGGAACAGAGTCTCGAATTAAATTAATAGCATGATCATTTCCTTTGGACAAAAACGTCGGCCTACAAATACAATAATGAAATGTAGGAAGTCAGCAACAAGTGGGGGCGTCCAGCGCGCCTTAGACAGTTATGACAAGGAATGCCAAGCGTCCCGCATCGTCTCAGCTCTCTTGTTTGACTCATACTTGTGGGCAATATTCGGGCGGCCAAGAAATTTGTCCGTAGTTTCAATATTAATTTATACAAGTCAGGTTGCGCCGTGCCCTAAAGCACTATTCCCAACCCCGCCTCAAACCGGCCACATAGTTGCAAGCTGTTCTCTGCACTTCTCGTAGCTAGAGCAAGACGACGCTCGGACCTACTTTCGGCCGCGTCATCGATATGGTCTCAAGGCTTAAGGAATTAGGCCAAGCAGTTCATTGTCCCAGCAAGATTTCAGGCGTTCTTATTTGCTGTCTTTCACGAGCCGGAGATCAAGATATTAGCCGAGATGCCCGTCTGGTGCCCTGAGTTACATCGCGACTTATAGCAACCTCTGCTCCCTTTGAACCGACCACAACATAACTAAGCGGGCTTATGCCGTAGCAGTCGGGCAACGCTTACGCGGAACTTGATGGCGGTCTAACTTTAGCGCAATATAGCCTCAGGGCCAAGAAGGATCCTTCGATTGGAAATCTGAAGGATCCCTCCGCGAATTTGCAGCACTCCTGATCAGGCACCGTGTACATACGGTTAAACGAGAATCCTCAACGCAAGCCAAGCAAGCGTGGTCGTCCTGAGGTCGTATCTTTAATAATGTTTCTCATTAGTTGGTACTTCCCCTCTCCTGTCTACGATCCGTACTGCCGGTCAACCTCCAAAACTGCGGGCGCGTCGCTCATGCCCTGAGAGACTATCCTGTATGTCATAGAACCTCACTTGTTCACGAATTGTTGTTTCACGTTAGCGACAAGCTCACTCGAGTAAAAAAACTTAGGGAGTACTTCGTCGGAGTAAGATACCACAAGTGTCAGTCCAAGCACCCGATCCTCCCACCCAGAGCCCTGATAATTCTGGGTGCACGTATGCCAATTGATGTCCCGCCAATCATTGCGGCTAACCGGTCTCTGATTCCAATAGTGGGCGCATTGTCAGTGTCCACCATGGTACTAACGGTATCCAGGAACTGCAGATGGTACCTATATTTCTAGTTTTCTCACTACCTAATGTAACATCTGCAACCCCGTACAATTGGGCCTGAGTTTCAGCAAGTGTGAATATAGTGGCTCAGGAATGCGGAGGGTAATTGGGCGACTCCCCTAGCGCGATAGCGGGAGAGAACTGTGAGACCCGAGTAAGCATTGTAGCGTGGATGAAGAATGCAGTTCGGTTCGTTGTCTTACTGTTAGACGTAATTTTTCACACTTCACATTATCACCAGCGGCCGGAATGTTCACTTGAATATTGTTAGAATTCGCCCTAGGATTGTGCTAACTCAGGTTACGTGTAGGGGTTCATCTTTCGGTCGCAGGGGGATAGGACCCCGTGTTTAGGTCTTTACAGAGAATCCTTGGGGTCGAGGCGGGAGCTCGGAAAGCAGCGGCACACAACGAATTTTAGGATCCCAAGCAACGTCATGCACTTAATCGAGCAACCTTTGACCATAATGGATGATCCTGCCGATGAGGTTTAGTCCGGTAGGCGCCCCGAACCATGTTCATGTAATGAGGCGAAAGGGTACCTTTAGAATTCCACATAGGTCAAATGGTCGTGCAAGTAGCAGGGGCCTTTTAGCAAGATCGCCAAAGTACGTCAAGCGAATAAATCGAAAGTTGTAACAACAGAAATGGATTGTAAGGTGGGCAAACTTTGGAGAAAGTTCCGGAAAAAAATAGCCGGATGCTGCATTGCATTAACGGCAAATAATTGCCCCGCCTTATCCATAAGCGTACCCCTCGTTTTCAGTAAACGAGGTTCCAACGTAAGTTTGACCTATCCCACCGGCGGACTGAAGTTCGTATTGTTCAATGATCCATCAGTCCTACCGAAAACTGACATACCCAGGTTACGTGGCTCTGGCCTCTCCATCGCAATGAGGATGACTCGTACTGTTGTCCCCACCGACAGAATATCGTCTTCCGCCCTCAGGCCATAGGGCGAGCTCCCCGTACCACGTACTTCTTGACCCGTTCTGAATCTGAGGGTTAGCTGTTCAGGTCTAGTTCCACCTATCATGATTACTACAATCATGTAATCTATAAGTCCAGACCACCGCTGCGCTGCGCGCAGGTGTAAACAAAAAGACCTTATTGTGACGCGCTGGACTCACATTTCTACCCAGTGACCCTCCACGGACCCTAGGAGGACGAACCTTCTGGCCCCTCCGGTGATTCCAACCATAATTACGGCGAAGACCCTCTGACCGACTAAAAGAACTCAGATAAGTGTTAAGGTAAGCTTGACAAATAAATCTTCGCCAGGTCACATACGAGAATACATTGTACTGGCTGTATAAATGCATAATTCATTCTACTTCTGGTGGAGACCGCCTGGAACTCACGGATCCCGTCCATCCGACGGAAATATAGTGGAACTAAAAGCGGGTCTAGACGCATTATAGCGCCACTATTTCGCACACATTCTGTTCCCCATCCCGCTAATACTCAGCAGAGTCAGAGCAGGAGGACGGGGTCATTTTGAGCTCTAAGAATCTAGCCGATGGAATGCTAACAGCCGCACCTGGAGGTTCCTCTCTGCCGGCGGCCACGCCAGAAAATATGTTCCAAAGGCTCTCAGTCAACCAGGAGTTCGAACTAGCCTCTACGGGCACACTAACTCAATCAGTGCTTAAATGACGCATCGTAGATTCTCTAACGAGTCACACGACGACCCAACCTAGTGCCTCCCAAGAAAGTACTCTTGCTATTAGATCAGGGGCAAGTACTTGAGACGACATACCCGCCTCTGGCCGTCGATATCATTGAGGTCTCATTGAGCTAAGATTCCCATCTATGGTCCCTGATCTAAGCCATATATTCGTACTGTTCGACCAGCCCCGATATGTTGAACCCGTTGCCATCAGTAGAATCATGTCGCGCGAAAAGAGTCAAGTGGGGAATCCACTTTTCTCTTATACGGAATAGCTTCTGGAATCAAGTTCGATCCGGGACCCCTCTAATCGTATTGAATAGGAGATCTTGCTATCTTGCCTGACACATCTAATGCTCTAAGTTGGATGGCTACCCGGCGCACAGGAAGGAACAGATACCAAATTAGTATACTACTTCCCATTTCATCCTATAGGATCGCACATTGTATAGCCTACAGGCAATGTTGATCATCTATCATTGTTGAGGGCATGTGCAGCGCAAAACTTTAGCGGGTTGGGAAATAACCTTGTTCTTCATGACCTAAGTTTGGAGCTCATCGCTGGGATGACGTTCAGCACCCGATAGCAAGCGAGCCTTCCGCGAACGTAAGCCACTCACCAGGCCCTTTTGGCGGCTTCGACGAACTCTACGAGACACTGTTCTAGCTCGCTGAACACGCCGGTGCGACCTCTGTCAGATCGTAATCTAAACCTTGGTGGGTAAAATCTCACGGATTCATTACGCAACAAGACGCATCCTCGCATTTGCTGCGAGGCACGGATCCCTTTATCTTGGGCCCCCCCGCCCGTAAAAATCATTAGTGGGGAGAGCGCGCTGGATCGTCGCTTAAAGTACTTAACCGCATCTGACCGATCGCTTACTTGGAGCCCGTGAGGACGCCAACACCCCCACAATATGTACATCGCCGCTCGTTGAAGCTGTTCTATGACATACTACTTTGTTGGTATACGTGGGGCGTTCAAGGCGGAGAATACTAGCGACTCGGCCAGGCACCGAACACGAGGGACGAAGATCCGCGCCTTTAGTACCACTCTTCGGATTGGATTGGTGCGGTCTTTGAGAGCGCAAACCTAGCAACCACATCTACTAGAATAGCGTTGATACCGGGCAGCTAGTGCACTGCCTTCGGATGAATAGAGTACTTGTAACGACTCGGGCTTGAGCTTTGCTCATCAGTTGTCCCCGTCGAGATTATTCACTATGGGTTTAGGAGATAAAGTCAATCCGAATAGGTCGATTAGGAAGGACGCTATCCGAAGGCCGCCATGAGACGCTTTATAATTAACCCCAACGACTCTGCAGCCCATCTACCGGACACACCTAAAGGATGCATCTATTCGTCAGTAAAGAGTAAGGTCTAACAACCGGATCGTAGGTAATCAAAATGCCGCCTCTTAGCGGCGGTACTCCCGCCTCGTGTCTTCGGGCGATATACCCCTTGACTGAGCGTACGTCTACTTCACGGGGTCGCATGACCGTCTCTTGCCTGAAAGGATCCGCCTTGCGGGACGTTAAATTTAGTAGATGCAGTGATCTAGAGCACTATTATGATGTTGTCGCCTGCACTCGGGGATGGATGGACAGCCTTATGATGACAATCCAACAAACAACTGCGCAGTAATATGGAACGAAGCTAGAGGGCCTTAGTCGAGGGTAGTGGGCACACCGGGCCCGCCTCTTCCCACGGTTGGCACTCGTGTTCGTCGCGACCTGGTGCCCCGTGTGACCTACCACGAATATAACACCTGGAAATTATGTATCGTGCGATGGATCGGCTTTCGCCTGTGATAAGCGGCGGACACCCACCTTGACCCTGAGAAGATGACAGACGAGACCAGCGCAGTCGAAACGTTAGTTGGAAGCATGCTTATAGAATAGTCCGGGAGCAGAGGCGTGATATGAAACTTCGCCCGTTTTCAATGCGCCAAACAGCTTCCAAATCGCCGGGTGTAGAAATTTATAAAGGTCTCCCTCACATAACCAATACACGCTCATCCGCGAACGATTCGTAATAGGGTATATATGGGGATCCGCGGGATATTGGGTGACTCGAAGATCCGTTTCCTAATTGTCCGTGTCTTTGACTCTGAATTGACCCACAACCAGATTATAGGCTGCATTTGTTCTTAATACGCACCAACCGGGTGGTTACAACTCGTGGTCGGTTCCCGGAATGAAATGTGATGTGGAAAGTCACCCCTTAAGACATGTGAGGTGAGTCGCTAGTCGGCAAATTACTAGAATACATTGCTGGAGAGCAGGGCCTAACACACCTAGTCGAGGAATCGCTCGGACTCTGTCAGCGCTGCACGGGTACACTCGAGGTAGTGATATATTGTCGATCGCCCGGCGGAGTCCGCAGCAGATCAGGAGGAGTCGTAAACGATAAGTAGCCCAATACATTATCCAGTAGCAACCGCCCTCATGGTACTCTTCGCAAGGCATATTCAACCGCTGAGGCTCCGGATGATTAATATCTCACAGAACTTGATAGCCTTTTGTATTTCGGTTGCAGTATAGTATCCTAGGGTGACTCAGATAAAATCACGGATTCCTTTTAAATCCCTTACATCACTTGATCGCAGTCGGCGGGTTCCCGCATACGCGGGTCCAGTCTTAGAACGTGTCAATGGCGTACTTAGGACCAATAGATGGAGGGAGTTACGGGTAGAAAAAGCCTTCCGCGTCCCCTTGCCGCCCCCGACTTCCCGGAAAGCGCCAGAGCGCAGCTCCAAACCACGGGTGTTTCTGGCCAACCTTCAGGTAGGATCCCAATCGCTATGACTGCGACTGGTATATCCGTGCGGCGACCGTTTGACGGATCTTCAAGCCTATAACGGAGGTCTATTCAAAGGCGAAATAAATTAACACCAGGAGAAACACGCGCGCAAGGACCGCTGGGGGCAACTTGTCTCCAGGTCGCACGTGTGGAGGGCCTCATGATCCAGACGGTCGAGAAGGGGACATATTTGCTTTCCAATTTCACCTACTGATCCTGGATATCAAGCGAAGCCTGTATTTATCCTTTTGACGCTCGCGCCGGATGCGAGACTCGTCAGGTACATAGTTTAGTGAGACCTTCAAGTAACTACCGTGAGGAGACGTTCCTGCTTACCTACTCGGTTGTGCTATCGGTCAGCTTCGCTTTGTTTTTTTTTGTCCAAGGGGTTCAGCGATGAGCAATCGAAACCAGCATCGCTAAACGAATTCCGTGGAAGCTTTGGCTTAGCTTCGCAAAAAGTATATGATCAGAGGCAAGCGTTTATCTGCCATTAGATCTGATCCCCTTATGTCCGGAAAGGGGTGATCTGTGGAGGTATTTTCGCATGTGAAGTAAAGTACTATCTAAAGGAGCTCGCTTTATCATTACGGGCCCAACTTTAATACCAATGGGATATACCGTGACCCTTAGAGGCCCCAAGCGATTAGTGGAGCGGTGGGCCGGCATGATGGCATGTGGGGGTTCGCACATTCCACGAGCCAAGTCTACTCTATACGATCGAACTACAGCGACGAACAACATGGCGAGAGTTGGCCGCACTCGTAAATGCAGCGCGAGAAAAGGTGACCATAGATTAGTATCCACAACACACCAACTTAACTCGATGTATGGTTCTAGCACGGGATCGTCTGATGGTTCGTATTGCGCGGTCTAACCAAACTCAAAGTGCTCGCAGGACACGAATTAATATTGTTCGTCAGCTGAGCGAAACCACCGGTTTCATAAGCAGGCTACCAAAGAAGTCCTACAACTGTAGTTTCGGGGGGCAACGACTGCATACGCGTGATATTACACCA"
make_complement(test_string)