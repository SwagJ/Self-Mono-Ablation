from . import model_monosceneflow
from . import model_monosceneflow_ablation
from . import model_monosceneflow_ablation_decoder_split
from . import model_monodepth_ablation
from . import model_exp_depth_flow

##########################################################################################
## Monocular Scene Flow - The full model 
##########################################################################################

MonoSF_Full		=	model_monosceneflow.MonoSceneFlow
MonoSF_Disp_Exp		=	model_monosceneflow.MonoSF_Disp_Exp
MonoSF_Disp_Exp_Plus		=	model_monosceneflow.MonoSF_Disp_Exp_Plus
MonoSceneFlow_Disp_Res      =	model_monosceneflow.MonoSceneFlow_Disp_Res
MonoFlow_Disp 				=	model_monosceneflow.MonoFlow_Disp
Mono_Expansion				=   model_exp_depth_flow.Mono_Expansion
PWC_Disp					=   model_exp_depth_flow.PWC_Disp
PWC_Disp_Unfreeze			=	model_exp_depth_flow.PWC_Disp_Unfreeze
MonoDispExp 				=	model_exp_depth_flow.MonoDispExp
MonoDispExp_v2				=	model_exp_depth_flow.MonoDispExp_v2
MonoDispDispC 				=	model_exp_depth_flow.MonoDispDispC
MonoDispDispC_Large			=	model_exp_depth_flow.MonoDispDispC_Large
Joint_MonoDispExp			=	model_exp_depth_flow.Joint_MonoDispExp
MonoFlow_Disp_Seperate_NoWarp = model_monosceneflow.MonoFlow_Disp_Seperate_NoWarp
MonoFlow_Disp_Seperate_Warp_OG_Decoder = model_monosceneflow.MonoFlow_Disp_Seperate_Warp_OG_Decoder
MonoFlow_Disp_Seperate_Warp_OG_Decoder_No_Res = model_monosceneflow.MonoFlow_Disp_Seperate_Warp_OG_Decoder_No_Res
MonoFlow_Disp_Seperate_Warp_OG_Decoder_Feat_Norm = model_monosceneflow.MonoFlow_Disp_Seperate_Warp_OG_Decoder_Feat_Norm
MonoSceneFlow_PWC 			=	model_monosceneflow.MonoSceneFlow_PWC
MonoFlowExp_ppV1			=	model_monosceneflow.MonoFlowExp_ppV1
MonoFlowExp_ppV1_2			=	model_monosceneflow.MonoFlowExp_ppV1_2
MonoFlowExp_ppV1_3			=	model_monosceneflow.MonoFlowExp_ppV1_3
MonoFlow_DispC_v1_1			=	model_monosceneflow.MonoFlow_DispC_v1_1
MonoFlow_DispC_v1_2			=	model_monosceneflow.MonoFlow_DispC_v1_2
MonoFlow_DispC_v2_1			=	model_monosceneflow.MonoFlow_DispC_v2_1
MonoFlow_DispC_v2_2			=	model_monosceneflow.MonoFlow_DispC_v2_2
MonoFlow_DispC_v2_3			=	model_monosceneflow.MonoFlow_DispC_v2_3
MonoFlow_DispC_v2_4			=	model_monosceneflow.MonoFlow_DispC_v2_4
MonoSF_DispC				=	model_monosceneflow.MonoSF_DispC
MonoFlowDisp_DispC			=	model_monosceneflow.MonoFlowDisp_DispC
MonoFlowDisp_DispC_v2		=	model_monosceneflow.MonoFlowDisp_DispC_v2
MonoFlowDisp_DispC_v3		=	model_monosceneflow.MonoFlowDisp_DispC_v3
MonoFlowDisp_Exp			=	model_monosceneflow.MonoFlowDisp_Exp
MonoFlowDisp_Teacher_Student	=	model_monosceneflow.MonoFlowDisp_Teacher_Student
MonoFlowDisp_DispC_Joint	=	model_monosceneflow.MonoFlowDisp_DispC_Joint
MonoFlowDisp_DispC_Joint_v2	=	model_monosceneflow.MonoFlowDisp_DispC_Joint_v2

##########################################################################################
## Monocular Scene Flow - The models for the ablation studies
##########################################################################################

MonoSceneFlow_CamConv			=	model_monosceneflow_ablation.MonoSceneFlow_CamConv

MonoSceneFlow_FlowOnly			=	model_monosceneflow_ablation.MonoSceneFlow_OpticalFlowOnly
MonoSceneFlow_DispOnly			=	model_monosceneflow_ablation.MonoSceneFlow_DisparityOnly

MonoSceneFlow_Split_Cont		=	model_monosceneflow_ablation_decoder_split.SceneFlow_pwcnet_split_base
MonoSceneFlow_Split_Last1		=	model_monosceneflow_ablation_decoder_split.SceneFlow_pwcnet_split1
MonoSceneFlow_Split_Last2		=	model_monosceneflow_ablation_decoder_split.SceneFlow_pwcnet_split2
MonoSceneFlow_Split_Last3		=	model_monosceneflow_ablation_decoder_split.SceneFlow_pwcnet_split3
MonoSceneFlow_Split_Last4		=	model_monosceneflow_ablation_decoder_split.SceneFlow_pwcnet_split4
MonoSceneFlow_Split_Last5		=	model_monosceneflow_ablation_decoder_split.SceneFlow_pwcnet_split5

##########################################################################################
## Monocular Depth - The models for the ablation study in Table 1. 
##########################################################################################

MonoDepth_Baseline				= model_monodepth_ablation.MonoDepth_Baseline
MonoDepth_CamConv				= model_monodepth_ablation.MonoDepth_CamConv