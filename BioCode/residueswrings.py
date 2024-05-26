import openbabel as obab
import sys

# Create module function that saves list containing indeces of residues with input pattern
def match_res(input_file, pattern):
    # Sets object for input file
    conv = obab.OBConversion()
    conv.SetInFormat(conv.FormatFromExt(input_file))    # set up object storing input file

    # Reads input file and store the SMILES string in variable
    mol = obab.OBMol()
    conv.ReadFile(mol, input_file)

    # Picks from OBMol only atoms matching for pattern
    pat = obab.OBSmartsPattern()
    pat.Init(pattern)
    pat.Match(mol)

    # Creates set to store residues with rings
    residues = set()                # not only with rings anymore
    maplist = pat.GetMapList()

    # Iterates through each atom in every peptide's residue, applying SMARTS-pattern to them
    for atom in maplist:
        residues.add(mol.GetAtom(atom[0]).GetResidue().GetIdx())
    residues = sorted(list(residues))
    return residues

def res_inf(input_file, pattern):
    conv = obab.OBConversion()
    conv.SetInFormat(conv.FormatFromExt(input_file))

    mol = obab.OBMol()
    conv.ReadFile(mol, input_file)

    residues = []

    # Iterates through each atom in every peptide's residue, applying SMARTS-pattern to them
    for res in match_res(input_file, pattern):
        res = mol.GetResidue(res)
        residues.append([res.GetName()])                          # writes the rest of information of
        chain = res.GetChain()                                    # residue if rest_inf=True
        if (chain != 'A' and chain != None):
            residues[-1].append(chain)
    return residues

# Create private function of root program script
def main():
    # Creates input pattern for script
    input_pat = sys.argv[1:]                                      # remade input to set arguments directly
    input_file, pattern = input_pat[0], input_pat[1]

    # Now able to find rings with function (if pattern = '[r5,r6]')
    residueswrings = res_inf(input_file, pattern)

    # Convert our output into string content
    for i in range(len(residueswrings)): 
        if len(residueswrings[i]) == 1:
            residueswrings[i] = str(residueswrings[i][0])
        else:
            residueswrings[i][0] = str(residueswrings[i][0])
            residueswrings[i] = '\t'.join(residueswrings[i])
    residueswrings = '\n'.join(residueswrings)

    # Manages our output
    if len(input_pat) == 3:
        with open(input_pat[2], 'w') as out: out.writelines(residueswrings)
    else: print(residueswrings)

# Code performes only if root program is executed
if __name__ == '__main__':
    main()