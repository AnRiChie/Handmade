import sys
import openbabel as obab

# Create module function that saves set containing residues with input pattern
def match_res_inf(input_file, pattern, rest_inf=True):                  # if rest_inf=False writes only
    # Sets object for input file                                          indeces of suitable residues
    conv = obab.OBConversion()
    conv.SetInFormat(conv.FormatFromExt(input_file))                    # set up object storing input file

    # Reads input file and store the SMILES string in variable
    mol = obab.OBMol()
    conv.ReadFile(mol, input_file)

    # Creates list to store information about suitable to pattern residues
    residues = []

    # Iterates through each atom in every peptide's residue, applying SMARTS-pattern to them
    for atom in obab.OBMolAtomIter(mol):
        res = atom.GetResidue()
        if (len(residues) != 0) and (residues[-1][0] == res.GetIdx()):  # checks uniqueness of atom (similar to set)
            continue
        if atom.MatchesSMARTS(pattern):
            residues.append([res.GetIdx()])                             # writes indeces of residues to list
            if rest_inf:
                residues[-1].append(res.GetName())                      # writes the rest of information of
                chain = res.GetChain()                                  # residue if rest_inf=True
                if (chain != 'A' and chain != None):
                    residues[-1].append(chain)
    return residues

# Create private function of root program script
def main():
    # Creates input pattern for script
    input_pat = sys.argv[1:]                                            # remade input to set arguments directly
    input_file, pattern = input_pat[0], input_pat[1]

    # Now able to find rings with function (if pattern = '[r5,r6]')
    residueswrings = match_res_inf(input_file, pattern)

    # Manages our output
    for i in range(len(residueswrings)): 
        residueswrings[i][0] = str(residueswrings[i][0])
        residueswrings[i] = '\t'.join(residueswrings[i])
    residueswrings = '\n'.join(residueswrings)

    if len(input_pat) == 3:
        with open(input_pat[2], 'w') as out:
                out.writelines(residueswrings)
    else: print(residueswrings)

# Code performes only if root program is executed
if __name__ == '__main__':
    main()
