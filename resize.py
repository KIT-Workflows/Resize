import os
import yaml

from ase.io import read
from pwtools import io


os.environ['ESPRESSO_PSEUDO'] = os.getenv('PSEUDOPOTENTIALS_PATH', os.getcwd())


def create_optimized_structure():
    """
    Create an optimized crystal structure from a 'relax.pwo' file.

    This function reads the last structure from the 'relax.pwo' file,
    which is an output of a quantum espresso relaxation calculation.
    It then converts this structure into an ASE atoms object and
    writes it to a trajectory file named 'optimized_structure.traj'.
    """

    structure_opt = io.read_pw_md('output.pwo')[-1].get_ase_atoms()
    structure_opt.write('optimized_structure.traj')


def apply_strain_and_write(input_yaml, input_traj, output_yaml):
    """
    Applies strain to a crystal structure and writes the strained structure to a file.

    Parameters:
    input_yaml (str): Path to the YAML file containing the strain value.
    input_traj (str): Path to the input trajectory file ('optimized_structure.traj').
    output_yaml (str): Path to the output YAML file ('output_dict.yml').
    """

    # Read values from YAML file
    with open(input_yaml, 'r') as file:
        wano_data = yaml.safe_load(file)
        strain = float(wano_data['Strain value'])

    # Read optimized structure
    structure_opt = read(input_traj)

    # Apply strain to the structure
    structure_strain = structure_opt.copy()
    structure_strain.set_cell(structure_strain.cell * strain ** (1 / 3), scale_atoms=True)
    file_name = 'structure_strain.traj'
    structure_strain.write(file_name)

    # Create output dictionary
    output_dict = {
        "iter": [file_name],
        "struct_len": 1
    }

    # Write the dictionary to a YAML file
    with open(output_yaml, 'w') as file:
        yaml.dump(output_dict, file, default_flow_style=False)

    return output_dict


if __name__ == '__main__':
    create_optimized_structure()

    apply_strain_and_write(
        input_yaml='rendered_wano.yml',
        input_traj='optimized_structure.traj',
        output_yaml='output_dict.yml'
    )
