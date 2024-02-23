#!/bin/bash

#SBATCH -N 1
#SBATCH -n 1
#SBATCH -p volta-gpu
#SBATCH --mem=16g
#SBATCH -t 1:00:00
#SBATCH --qos gpu_access
#SBATCH --gres=gpu:1
#SBATCH --mail-type=ALL
#SBATCH --mail-user=tianyin4@email.unc.edu

source activate mistral
cd LING427_project
CUDA_VISIBLE_DEVICES=0 python evaluate_model.py
