#!/bin/bash

# experiments and datasets meta
KITTI_RAW_HOME="/disk_hdd/kitti_full/"
EXPERIMENTS_HOME="/disk_ssd/Self_Mono_Experiments/"

# model
MODEL=MonoSF_Full

# save path
CHECKPOINT=None

# Loss and Augmentation
Train_Dataset=KITTI_Raw_Depth_KittiSplit_Train_mnsf
Train_Augmentation=Augmentation_SceneFlow_Depth_Sup
Train_Loss_Function=Loss_SceneFlow_Depth_Sup

Valid_Dataset=KITTI_Raw_Depth_KittiSplit_Valid_mnsf
Valid_Augmentation=Augmentation_Resize_Only
Valid_Loss_Function=Loss_SceneFlow_Depth_Sup

ALIAS="-kitti-dep-"
TIME=$(date +"%Y%m%d-%H%M%S")
SAVE_PATH="$EXPERIMENTS_HOME/$MODEL$ALIAS$TIME/$Train_Dataset/$Train_Loss_Function/$Train_Augmentation"

# training configuration
python ../main.py \
--batch_size=4 \
--batch_size_val=1 \
--checkpoint=$CHECKPOINT \
--lr_scheduler=MultiStepLR \
--lr_scheduler_gamma=0.5 \
--lr_scheduler_milestones="[23, 39, 47, 54]" \
--model=$MODEL \
--num_workers=10 \
--optimizer=Adam \
--optimizer_lr=2e-4 \
--save=$SAVE_PATH \
--total_epochs=62 \
--training_augmentation=$Train_Augmentation \
--training_augmentation_photometric=True \
--training_dataset=$Train_Dataset \
--training_dataset_root=$KITTI_RAW_HOME \
--training_dataset_flip_augmentations=True \
--training_dataset_preprocessing_crop=True \
--training_dataset_num_examples=-1 \
--training_key=total_loss \
--training_loss=$Train_Loss_Function \
--validation_augmentation=$Valid_Augmentation \
--validation_dataset=$Valid_Dataset \
--validation_dataset_root=$KITTI_RAW_HOME \
--validation_dataset_preprocessing_crop=False \
--validation_key=total_loss \
--validation_loss=$Valid_Loss_Function \