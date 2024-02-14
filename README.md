# Resize

**Version:** 0.0.1

**Author:** J. Schaarschmidt

## Description

This script applies a specified strain to a crystal structure from a trajectory file and saves the strained structure's details.


## Inputs
- `relax.pwo` (str): Path to the relax.pwo file containing the optimized structure.
- Input trajectory file (str): Path to the input trajectory file containing the optimized structure.

## Outputs
- Strained structure: Saved in a file (e.g., `structure_strain.traj`).
- Output YAML file: Contains details of the operation (e.g., `output_dict.yml`).

## Dependencies
- ASE
- PyYAML
