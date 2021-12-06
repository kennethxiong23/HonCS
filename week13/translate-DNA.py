""" This program translates genes to proteins. """

def translate(DNA_Sequence, codonTable):

    ### Find ATG codon before we start constructing the protein sequence
    START = False
    phrase = ""
    for i in range(0,len(DNA_Sequence), 3):
        codon = DNA_Sequence[i:i+3]
        print(codon)
        if START:
            if codonTable.get(codon) == "stop":
                return phrase
            phrase = phrase + codonTable.get(codon)
        if codon == "ATG":
            START = True
            

def readCodons(filename):
    """ Complete the readCodons() function to add entries to the dictionary.
        Each line of the file has one amino acid and then all of the codons
        that map to it. Each codon/amino-acid pair will need to be in the
        dictionary. Note: the three letter abbreviation of the amino acid
        appears first, followed by the one-letter abbreviation, followed by all
        of the codons that map to it.
    """
    infile = open(filename, 'r')
    codonTable = {}
    for line in infile:
        line = line.strip()
        line = line.split(",")
        amino = line[1]
        codons = line[2:]
        for codon in codons:
            # make codon, amino key-value pair and add key-value pair to list
            codonTable[codon] = amino
    return codonTable


def readDNAFile(filename):
    infile = open(filename, 'r')
    sequence = ""
    for line in infile:
        if line[0] != ">":
            sequence += line.strip()
    infile.close()
    return sequence


def main():

    filename = str(input("Enter filename: "))        # test.fasta

    DNA_Sequence = readDNAFile(filename)
    codonTable = readCodons("codon.txt")
    print(DNA_Sequence)

    translated_sequence = translate(DNA_Sequence, codonTable)
    print("Translated protein sequence:\n%s" % translated_sequence)


main()
