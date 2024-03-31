import openbabel as obab

# Creates input pattern for script
input = input('input_file SMARTS_pattern output_file\n').split()
file, pattern = input[0], input[1]

# Converts any type of file to .smi format
conv = obab.OBConversion()
conv.SetOutFormat('smi')        # more readable

# Reads input file and store the SMILES string in variable
mol = obab.OBMol()
conv.ReadFile(mol, file)

# Creates set to store residues with rings
residueswrings = set()

# Iterates through each atom in every peptide's residue, applying SMARTS-pattern to them
for atom in obab.OBMolAtomIter(mol):
    if atom.MatchesSMARTS(pattern):
        residueswrings.add(atom.GetResidue().GetName())

# Manages our output
if len(input) == 3:
    with open(input[2], 'w') as out: out.writelines(' '.join(residueswrings))
else: print(*residueswrings)
