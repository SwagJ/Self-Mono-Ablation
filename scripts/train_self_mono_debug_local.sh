#!/bin/bash

# For SLURM cluster only
#SBATCH	--output=/scratch_net/phon/majing/src/log/%j.out
#SBATCH --gres=gpu:1
#SBATCH --mem=50G

#source /scratch_net/phon/majing/anaconda/bin/conda shell.bash hook
#conda activate self-mono


# experiments and datasets meta
#KITTI_RAW_HOME="/scratch_net/phon/majing/datasets/kitti_full/"
KITTI_RAW_HOME="/disk_hdd/kitti_raw/"
EXPERIMENTS_HOME="/disk_ssd/self-mono-debug"
KITTI_COMB_HOME="/disk_hdd/kitti_full"
SYNTH_DRIVING_HOME="/disk_ssd/driving"

# model
MODEL=Mono_Expansion

# save path
#CHECKPOINT="checkpoints/full_model_kitti/checkpoint_latest.ckpt"
CHECKPOINT=None

# Loss and Augmentation
Train_Dataset=Synth_Driving_Train
Train_Augmentation=Augmentation_Exp
Train_Loss_Function=Loss_Exp_Sup

Valid_Dataset=Synth_Driving_Val
Valid_Augmentation=Augmentation_Exp
Valid_Loss_Function=Loss_Exp_Sup
ALIAS="-kitti-raw-"
TIME=$(date +"%Y%m%d-%H%M%S")
SAVE_PATH="$EXPERIMENTS_HOME/debug"


# training configuration
python ../main.py \
--batch_size=4 \
--batch_size_val=1 \
--finetuning=False \
--checkpoint=$CHECKPOINT \
--lr_scheduler=MultiStepLR \
--lr_scheduler_gamma=0.5 \
--lr_scheduler_milestones="[23, 39, 47, 54]"  \
--model=$MODEL \
--num_workers=16 \
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