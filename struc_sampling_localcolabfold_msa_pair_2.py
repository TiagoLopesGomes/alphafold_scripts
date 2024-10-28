import os
import subprocess
import random
import argparse

def run_colabfold(num_seeds, use_max_msa, input_file, output_dir):
    for msa_value in [10, 20, 30, 40, 50, 60, 70, 80, 90, 100] if use_max_msa else [None]:
        random_seed = random.randint(0, 1000000)
        msa_pair = f"{int(msa_value/2)}:{int(msa_value)}" if use_max_msa else None
        msa_dir = os.path.join(output_dir, msa_pair.replace(':', '_')) if use_max_msa else output_dir
        
        if use_max_msa:
            os.makedirs(msa_dir, exist_ok=True)

        cmd = [
            'colabfold_batch',
            '--num-recycle', '3',
            '--num-models', '5',
            '--model-order', '1,2,3,4,5',
            #'--model-type', 'alphafold2_ptm',
            '--use-dropout',
            #'--amber',
            #'--use-gpu-relax',
            #'--msa-only'
        ]
        if use_max_msa:
            cmd.extend(['--max-msa', msa_pair])
        cmd.extend([
            '--random-seed', str(random_seed),
            '--num-seeds', str(num_seeds),
            input_file,
            msa_dir
        ])
        subprocess.run(cmd)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run colabfold_batch with optional max-msa argument and seed number.')
    parser.add_argument('--num-seeds', type=int, default=1, help='Number of seeds to use for colabfold_batch')
    parser.add_argument('--input-file', type=str, help='Input FASTA file for colabfold_batch')
    parser.add_argument('--output-dir', type=str, help='Output directory for colabfold_batch results')
    parser.add_argument('--use-max-msa', action='store_true', help='Use max-msa argument if flag is set')
    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)
    run_colabfold(args.num_seeds, args.use_max_msa, args.input_file, args.output_dir)
