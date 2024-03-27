import openbabel as obab

file = input()

# Converts any type of file to .smi format
conv = obab.OBConversion()
conv.SetInFormat(file[file.find('.') + 1:])

# Reads input file and store the SMILES string in variable
mol = obab.OBMol()
conv.ReadFile(mol, file)

# Make SMARTS-patterns for aromatic and heterocycles
arom_rings = "[#6]1:[#6]:[#6]:[#6]:[#6]:[#6]:1"
heterocyc = "[#6,#7]1~[#6,#7]~[#6,#7]~[#6,#7]~[#6,#7]~1"

# Creates set to store residues with rings
residueswrings = set()

# Iterates through each atom in every peptide's residue, applying SMARTS-pattern to them
for atom in obab.OBMolAtomIter(mol):
    if atom.MatchesSMARTS(arom_rings) or atom.MatchesSMARTS(heterocyc):
        residueswrings.add(atom.GetResidue().GetName())

print(*residueswrings)
