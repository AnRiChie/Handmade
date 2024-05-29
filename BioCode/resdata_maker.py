import openbabel as obab
import sys

# Creates dictionary with lists of two lists
# containing strings with information
# about atoms and bonds in each residue
def res_inf(input_file):
    # Loads our input file
    conv = obab.OBConversion()
    conv.SetInFormat(conv.FormatFromExt(input_file))
    mol = obab.OBMol()
    conv.ReadFile(mol, input_file)

    residues = {}

    # Iterates through residues in molecule to write individual information unit for each residue
    for res in obab.OBResidueIter(mol):
        res_name = f'RES {res.GetName()}'
        if res_name not in residues:
            residues[res_name] = [[], []]

            # Builds up each unit adding atom data in first list
            for atom in obab.OBResidueAtomIter(res):
                atom_str = f'ATOM {atom.GetAtomicNum()} {atom.GetType()} {atom.GetHyb()}'
                residues[res_name][0].append(atom_str)
                
                # And then data of every bond of this atom in second list
                for bond in obab.OBAtomBondIter(atom):
                    bond_str = f'BOND {bond.GetBeginAtom().GetType()} {bond.GetEndAtom().GetType()} {bond.GetBondOrder()}'
                    residues[res_name][1].append(bond_str)

    return residues

def main():
    # Creates input pattern for script
    input_pat = sys.argv[1:]
    input_file, output_file = input_pat[0], input_pat[1]

    # Manages our output
    residues = res_inf(input_file)

    with open(output_file, 'w') as out: 
        for i in residues:
            out.writelines(i + '\n')
            for j in residues[i][0]:
                out.writelines(j + '\n')
            for k in residues[i][1]:
                out.writelines(k + '\n')
            out.writelines('END\n\n')

if __name__ == '__main__':
    main()