import openbabel as obab

# Create module function that saves set containing residues with input pattern
def match_res_inf(file, pattern):
    # Converts any type of file to .smi format
    conv = obab.OBConversion()
    conv.SetOutFormat('smi')        # more readable

    # Reads input file and store the SMILES string in variable
    mol = obab.OBMol()
    conv.ReadFile(mol, file)

    # Creates set to store residues with rings
    residues = set()                # not only with rings anymore

    # Iterates through each atom in every peptide's residue, applying SMARTS-pattern to them
    for atom in obab.OBMolAtomIter(mol):
        if atom.MatchesSMARTS(pattern):
            residues.add(atom.GetResidue().GetName())
    return residues

# Create private function of root program script
def main():
    # Creates input pattern for script
    input_pat = input('input_file SMARTS_pattern output_file\n').split()
    file, pattern = input_pat[0], input_pat[1]

    # Now able to find rings with function (if pattern = '[r5,r6]')
    residueswrings = match_res_inf(file, pattern)

    # Manages our output
    if len(input_pat) == 3:
        with open(input_pat[2], 'w') as out: out.writelines(' '.join(residueswrings))
    else: print(*residueswrings)

# Code performes only if root program is executed
if __name__ == '__main__':
    main()