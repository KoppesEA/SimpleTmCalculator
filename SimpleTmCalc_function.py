#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 20:19:21 2022

@author: erikkoppes
"""

##Simple Tm Calculator Function
##input should be in the form of string with quotations e.g "CGACTCTTAGCGGTGGATCA"
def SimpleTmCalc(primer):
    #Define input DNA sequence
    DNA_input = primer

    #define nucleotide length
    DNAlen = len(DNA_input)

    #Define GC count
    DNAgc = DNA_input.count('G') + DNA_input.count('C')

    #Define GC percent
    DNAgcp = round((DNAgc / DNAlen) * 100, 2)

    #Define final 5 nucleotides
    DNAfin = DNA_input[(DNAlen-5):]

    #Define GC count final 5
    DNAgcf = (DNAfin.count('G')) + (DNAfin.count('C'))

    #Tm calculation 
    DNAtm = (DNAgc * 4) + ((DNAlen - DNAgc) * 2)
    
    ##reverse seq
    DNAr = DNA_input[::-1]
    
    ##reverse complement seq
    DNArc = ""
    for letter in DNAr:
        if letter == "A":
            DNArc = DNArc + "T"
        elif letter == "C":
            DNArc = DNArc + "G"
        elif letter == "G":
            DNArc = DNArc + "C"
        elif letter == "T":
           DNArc = DNArc + "A"
            

    #Print results
    print("Primer DNA Sequence (5' to 3'): " + DNA_input)
    print('\tPrimer Length (nt): ' + str(DNAlen))
    print('\tPrimer GC Count (nt): ' + str(DNAgc))
    print('\tPrimer GC Percent (%): ' + str(DNAgcp))
    print('\tPrimer Simple Tm (C): '  + str(DNAtm))
    print('\tPrimer Last 5nt: ' + DNAfin)
    print('\tPrimer GC Count Last 5nt: ' +str(DNAgcf))
    print('\tPrimer Reverse Complement is: ' + DNArc)
