from . import kitti_2015_train
from . import kitti_2015_test

from . import kitti_raw_monosf
from . import kitti_raw_monodepth

from . import kitti_comb_mnsf
from . import kitti_eigen_test
from . import synth_driving

KITTI_2015_Train_Full_mnsf 				= kitti_2015_train.KITTI_2015_MonoSceneFlow_Full
KITTI_2015_Train_Full_monoexp_eval			= kitti_2015_train.KITTI_2015_MonoExp_Eval_Full
KITTI_2015_Train_Full_monodepth 		= kitti_2015_train.KITTI_2015_MonoDepth_Full
KITTI_2015_MonoExp_Train				= kitti_2015_train.KITTI_2015_MonoExp_Train
KITTI_2015_MonoExp_Val 					= kitti_2015_train.KITTI_2015_MonoExp_Val

KITTI_2015_Test 						= kitti_2015_test.KITTI_2015_Test
Audi_Test								= kitti_2015_test.Audi_Test
ETH3D_Test								= kitti_2015_test.ETH3D_Test

Synth_Driving_Train 					= synth_driving.Synth_Driving_Train
Synth_Driving_Val                      = synth_driving.Synth_Driving_Val
Synth_Driving_15mm_slow				   = synth_driving.Synth_Driving_15mm_slow
Synth_Driving_15mm_fast				   = synth_driving.Synth_Driving_15mm_fast
Synth_Driving_Full					   = synth_driving.Synth_Driving_Full


KITTI_Raw_KittiSplit_Train_mnsf 	= kitti_raw_monosf.KITTI_Raw_KittiSplit_Train
KITTI_Raw_KittiSplit_Valid_mnsf 	= kitti_raw_monosf.KITTI_Raw_KittiSplit_Valid
KITTI_Raw_KittiSplit_Full_mnsf 		= kitti_raw_monosf.KITTI_Raw_KittiSplit_Full

KITTI_Raw_EigenSplit_Train_mnsf 	= kitti_raw_monosf.KITTI_Raw_EigenSplit_Train
KITTI_Raw_EigenSplit_Valid_mnsf 	= kitti_raw_monosf.KITTI_Raw_EigenSplit_Valid
KITTI_Raw_EigenSplit_Full_mnsf 		= kitti_raw_monosf.KITTI_Raw_EigenSplit_Full

KITTI_Raw_Depth_KittiSplit_Train_mnsf 	= kitti_raw_monosf.KITTI_Raw_Depth_KittiSplit_Train
KITTI_Raw_Depth_KittiSplit_Valid_mnsf 	= kitti_raw_monosf.KITTI_Raw_Depth_KittiSplit_Valid
KITTI_Raw_Depth_KittiSplit_Full_mnsf	= kitti_raw_monosf.KITTI_Raw_Depth_KittiSplit_Full

KITTI_Complete_Depth_KittiSplit_Train_mnsf 	= kitti_raw_monosf.KITTI_Complete_Depth_KittiSplit_Train
KITTI_Complete_Depth_KittiSplit_Valid_mnsf 	= kitti_raw_monosf.KITTI_Complete_Depth_KittiSplit_Valid
KITTI_Complete_Depth_KittiSplit_Full_mnsf	= kitti_raw_monosf.KITTI_Complete_Depth_KittiSplit_Full

KITTI_Raw_Warpping_Sf_KittiSplit_Train_mnsf 	= kitti_raw_monosf.KITTI_Raw_Warpping_Sf_KittiSplit_Train
KITTI_Raw_Warpping_Sf_KittiSplit_Valid_mnsf 	= kitti_raw_monosf.KITTI_Raw_Warpping_Sf_KittiSplit_Valid
KITTI_Raw_Warpping_Sf_KittiSplit_Full_mnsf		= kitti_raw_monosf.KITTI_Raw_Warpping_Sf_KittiSplit_Full
KITTI_Raw_Warpping_Flow_KittiSplit_Train 		= kitti_raw_monosf.KITTI_Raw_Warpping_Flow_KittiSplit_Train
KITTI_Raw_Warpping_Flow_KittiSplit_Valid		= kitti_raw_monosf.KITTI_Raw_Warpping_Flow_KittiSplit_Valid
KITTI_Raw_Warpping_Flow_KittiSplit_Full			= kitti_raw_monosf.KITTI_Raw_Warpping_Flow_KittiSplit_Full
KITTI_Raw_Warpping_Test_Valid							= kitti_raw_monosf.KITTI_Raw_Warpping_Test_Valid

KITTI_Raw_KittiSplit_Train_monodepth	= kitti_raw_monodepth.KITTI_Raw_KittiSplit_Train
KITTI_Raw_KittiSplit_Valid_monodepth	= kitti_raw_monodepth.KITTI_Raw_KittiSplit_Valid

KITTI_Comb_Train		= kitti_comb_mnsf.KITTI_Comb_Train
KITTI_Comb_Train_Depth  = kitti_comb_mnsf.KITTI_Comb_Train_Depth
KITTI_Comb_Val_Depth    = kitti_comb_mnsf.KITTI_Comb_Val_Depth
KITTI_Comb_Val			= kitti_comb_mnsf.KITTI_Comb_Val
KITTI_Comb_Full			= kitti_comb_mnsf.KITTI_Comb_Full

KITTI_Eigen_Test 			= kitti_eigen_test.KITTI_Eigen_Test





