#!/bin/bash

# For SLURM cluster only
#SBATCH	--output=/scratch_net/phon/majing/src/log/%j.out
#SBATCH --gres=gpu:1
#SBATCH --mem=50G
#SBATCH --mail-type=ALL
#SBATCH --constraint='turing|titan_xp'

SYNTH_DRIVING_HOME="/disk_ssd/driving"
EXPERIMENTS_HOME="/disk_ssd/Self_Mono_Experiments"

# model
MODEL=Mono_Expansion

# save path
#CHECKPOINT="checkpoints/full_model_kitti/checkpoint_latest.ckpt"
CHECKPOINT=None

# Loss and Augmentation
Train_Dataset=Synth_Driving_Full
Train_Augmentation=Augmentation_Exp_Driving
Train_Loss_Function=Loss_Exp_Sup

Valid_Dataset=Synth_Driving_Val
Valid_Augmentation=Augmentation_Exp_Driving
Valid_Loss_Function=Loss_Exp_Sup

ALIAS="-monoexpansion-driving-rescale-"
SAVE_PATH="$EXPERIMENTS_HOME/$ALIAS/"

#CHECKPOINT="$EXPERIMENTS_HOME/$ALIAS/checkpoint_latest.ckpt"

# training configuration
python ../main.py \
--batch_size=2 \
--batch_size_val=1 \
--finetuning=False \
--checkpoint=$CHECKPOINT \
--lr_scheduler=MultiStepLR \
--lr_scheduler_gamma=0.5 \
--lr_scheduler_milestones="[14, 39, 47, 54]"  \
--model=$MODEL \
--num_workers=12 \
--optimizer=Adam \
--optimizer_lr=1e-3 \
--save=$SAVE_PATH \
--total_epochs=20 \
--sf_sup=True \
--training_augmentation=$Train_Augmentation \
--training_augmentation_photometric=True \
--training_dataset=$Train_Dataset \
--training_dataset_root=$SYNTH_DRIVING_HOME \
--training_loss=$Train_Loss_Function \
--training_key=total_loss \
--validation_augmentation=$Valid_Augmentation \
--validation_dataset=$Valid_Dataset \
--validation_dataset_root=$SYNTH_DRIVING_HOME \
--validation_key=total_loss \
--validation_loss=$Valid_Loss_Function \