# Structure Sampling using ColabFold MSA Subsampling

This simple script enables conformational sampling of protein structures using ColabFold by systematically varying the Multiple Sequence Alignment (MSA) depth (check the script for customisation options). The approach leverages the observation that adjusting MSA parameters and using different random seeds and dropout can help explore alternative conformational states of proteins [1]. 

## Key Features

- Systematic MSA depth sampling (10-100 sequences when --use-max-msa is enabled)
- Multiple random seed sampling for each MSA depth
- Configurable number of prediction cycles
- Uses dropout for increased conformational diversity
- Generates 5 models per run using all AlphaFold2 model weights

## References

[1] [Customising AlphaFold2 structure predictions](https://www.ebi.ac.uk/training/online/courses/alphafold/advanced-modeling-and-applications-of-predicted-protein-structures/customising-alphafold-structure-predictions/), EMBL-EBI Training


## Usage
```usage: struc_sampling_localcolabfold_msa_pair_2.py [-h] [--num-seeds NUM_SEEDS] [--input-file INPUT_FILE] [--output-dir OUTPUT_DIR] [--use-max-msa]

Run colabfold_batch with optional max-msa argument and seed number.

optional arguments:
  -h, --help            show this help message and exit
  --num-seeds NUM_SEEDS
                        Number of seeds to use for colabfold_batch
  --input-file INPUT_FILE
                        Input FASTA file for colabfold_batch
  --output-dir OUTPUT_DIR
                        Output directory for colabfold_batch results
  --use-max-msa         Use max-msa argument if flag is set
```