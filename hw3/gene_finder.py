# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 11:24:42 2014

@author: YOUR NAME HERE
"""

# you may find it useful to import these variables (although you are not required to use them)
from amino_acids import aa, codons
from random import shuffle
from load import load_seq
dna = load_seq("./data/X73525.fa")

def collapse(L):
    """ Converts a list of strings to a string by concatenating all elements of the list """
    output = ""
    for s in L:
        output = output + s
    return output


def coding_strand_to_AA(dna):
    """ Computes the Protein encoded by a sequence of DNA.  This function
        does not check for start and stop codons (it assumes that the input
        DNA sequence represents an protein coding region).
        
        dna: a DNA sequence represented as a string
        returns: a string containing the sequence of amino acids encoded by the
                 the input DNA fragment
    """
    code = ''
    for i in range(len(dna)/3):
        for j in range(len(codons)):
            for k in range(len(codons[j])):
                if dna[3*i:3*i+3] == codons[j][k]:
                    code += aa[j]
    return code

print coding_strand_to_AA("ATGCCCGCTTTT")

def coding_strand_to_AA_unit_tests():
    """ Unit tests for the coding_strand_to_AA function """
    print "input: " + "ATGCCCGCTTTT"
    print "expected output: " + "MPAF"
    print "actual output: " + coding_strand_to_AA("ATGCCCGCTTTT")
    
coding_strand_to_AA_unit_tests()

def get_reverse_complement(dna):
    """ Computes the reverse complementary sequence of DNA for the specfied DNA
        sequence
    
        dna: a DNA sequence represented as a string
        returns: the reverse complementary DNA sequence represented as a string
    """
    complement = ''
    for i in range(len(dna)):
        if dna[i]=='A':
            complement+= 'T'
        elif dna[i]=='T':
            complement+= 'A'
        elif dna[i]=='C':
            complement+= 'G'
        elif dna[i]=='G':
            complement+= 'C'
    
    return complement[::-1]
print get_reverse_complement("ATGCCCGCTTT")
    
def get_reverse_complement_unit_tests():
    """ Unit tests for the get_complement function """
    print "input: " + "ATGCCCGCTTAT"
    print "expected output: " + "ATAAGCGGGCAT"
    print "actual output: " + get_reverse_complement("ATGCCCGCTTAT")  
    
get_reverse_complement_unit_tests()

def rest_of_ORF(dna):
    """ Takes a DNA sequence that is assumed to begin with a start codon and returns
        the sequence up to but not including the first in frame stop codon.  If there
        is no in frame stop codon, returns the whole string.
        
        dna: a DNA sequence
        returns: the open reading frame represented as a string
    """
    codelove = ''
    for i in range(len(dna)/3): 
        if dna[3*i:3*i+3]=="TAA" or dna[3*i:3*i+3]=="TAG" or dna[3*i:3*i+3]=="TGA":
            break
        codelove+=dna[3*i:3*i+3]
    return codelove

print rest_of_ORF("ATGAGATAGG")

def rest_of_ORF_unit_tests():
    """ Unit tests for the rest_of_ORF function """
    print "input: " + "ATGAGATAGGG"
    print "expected output: " + "ATGAGA"
    print "actual output: " + rest_of_ORF("ATGAGATAGGG")  
    
rest_of_ORF_unit_tests()

def find_all_ORFs_oneframe(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence and returns
        them as a list.  This function should only find ORFs that are in the default
        frame of the sequence (i.e. they start on indices that are multiples of 3).
        By non-nested we mean that if an ORF occurs entirely within
        another ORF, it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
    codelove = []
    i=0
    while i < len(dna)/3:
        if dna[3*i:3*i+3]=="ATG":
            x=rest_of_ORF(dna[3*i:])
            codelove.append(x)
            i+=len(x)/3
        else:
            i+=1
    return codelove

print find_all_ORFs_oneframe("ATGCATGAATGTAGATAGATGTGCCC")

def find_all_ORFs_oneframe_unit_tests():
    """ Unit tests for the find_all_ORFs_oneframe function """

    print "input: " + "ATGCATGAATGTAGATAGATGTGCACC"
    print "expected output: " + "['ATGCATGAATGTAGA', 'ATGTGCACC']"
    print "actual output: " + str(find_all_ORFs_oneframe("ATGCATGAATGTAGATAGATGTGCACC"))

find_all_ORFs_oneframe_unit_tests()

def find_all_ORFs(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence in all 3
        possible frames and returns them as a list.  By non-nested we mean that if an
        ORF occurs entirely within another ORF and they are both in the same frame,
        it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
    new=[]
    for i in range(3):
        new.extend(find_all_ORFs_oneframe(dna[i:]))
    return new

print find_all_ORFs("ATGCATGAATGTAG")            

def find_all_ORFs_unit_tests():
    """ Unit tests for the find_all_ORFs function """
    print "input: " + "ATGCATGAATGTAGATAGATGTGCCC"
    print "expected output: " + "['ATGCATGAATGT', 'ATGAATGTA', 'ATG']"
    print "actual output: " + str(find_all_ORFs("ATGCATGAATGTAG"))

find_all_ORFs_unit_tests()

def find_all_ORFs_both_strands(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence on both
        strands.
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
    loco1=[]
    loco1.extend(find_all_ORFs(dna))
    loco1.extend(find_all_ORFs(get_reverse_complement(dna)))
    
    return loco1

print find_all_ORFs_both_strands("ATGCGAATGTAGCATCAAA")

def find_all_ORFs_both_strands_unit_tests():
    """ Unit tests for the find_all_ORFs_both_strands function """
    
    print "input: " + "ATGCGAATGTAGCATCAAAA"
    print "expected output: " + "['ATGCGAATG', 'ATGCTACATTCGCAT']"
    print "actual output: " + str(find_all_ORFs_both_strands("ATGCGAATGTAGCATCAAAA"))

find_all_ORFs_both_strands_unit_tests()

def longest_ORF(dna):
    """ Finds the longest ORF on both strands of the specified DNA and returns it
        as a string"""
    if find_all_ORFs_both_strands(dna)==[]:
        return ''
    else:
        a=max(find_all_ORFs_both_strands(dna),key=len)
        return a
    
print longest_ORF("ATGCGAATGTAGCATTCAAA")

def longest_ORF_unit_tests():
    """ Unit tests for the longest_ORF function """
    print "input: " + "ATGCGAATGTAGCATCAAA"
    print "expected output: " + "ATGCTACATTCGCAT"
    print "actual output: " + str(longest_ORF("ATGCGAATGTAGCATTCAAA"))

longest_ORF_unit_tests()

def longest_ORF_noncoding(dna, num_trials):
    """ Computes the maximum length of the longest ORF over num_trials shuffles
        of the specfied DNA sequence
        
        dna: a DNA sequence
        num_trials: the number of random shuffles
        returns: the maximum length longest ORF """
    lorg = ''
    d = list(dna)
    for i in range(num_trials):
        shuffle(d)
        f=longest_ORF(''.join(d))
        if len(f)>len(lorg):
            lorg = f                
    return len(lorg)

print longest_ORF_noncoding(dna,1500)
                
def gene_finder(dna, threshold):
    """ Returns the amino acid sequences coded by all genes that have an ORF
        larger than the specified threshold.
        
        dna: a DNA sequence
        threshold: the minimum length of the ORF for it to be considered a valid
                   gene.
        returns: a list of all amino acid sequences whose ORFs meet the minimum
                 length specified.
    """
    loco2 = find_all_ORFs_both_strands(dna)
    r=0
    p=[]
    while r<len(loco2):
            if len(loco2[r])>threshold:
                p.append(coding_strand_to_AA(loco2[r]))
                r+=1
            else:
                r+=1
    return p
    
print gene_finder(dna, 666)