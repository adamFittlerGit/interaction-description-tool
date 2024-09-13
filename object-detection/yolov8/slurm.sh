#!/bin/bash 
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --job-name=yolo
#SBATCH --mail-type=All
#SBATCH --mail-user=a.fittler@uqconnect.edu.au
#SBATCH -o yolo_out.txt
#SBATCH -e yolo_err.txt
#SBATCH --gres=gpu:1

conda activate yolo8 #Make sure to create a conda env called yolo8 and install ultralytics on rangpour

python3 run.py