import openbabel as obab

# Converts any type of file to .smi format
conv = obab.OBConversion()
conv.SetOutFormat('smi')

# Reads input file and store the SMILES string in variable
mol = obab.OBMol()
conv.ReadFile(mol, input())  
smi_str = conv.WriteString(mol)

residueswrings = set()

# Finds atoms located in rings and writes names of their residues in the set
for atom in obab.OBMolAtomIter(mol):
        if atom.IsInRing():
            name = atom.GetResidue().GetName().strip()
            if name not in residueswrings:              # Redundant condition because of sets' properties
                residueswrings.add(name)                # but why not

print(*residueswrings)