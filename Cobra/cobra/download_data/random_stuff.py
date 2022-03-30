
#%%
import os
from pathlib import Path
from os.path import join
import pandas as pd 
import shutil

#from repository
script_dir = os.path.realpath(__file__)
base_dir = Path(script_dir).parents[1]  #cobra directory
table_dir = join(base_dir, 'tables')

#from hdd
disk_dir = "F:" #hdd
dst_data_dir = join(disk_dir,"CoBra","Data")
dcm_dst_data_dir = join(dst_data_dir,"dcm")
nii_excluded_dst_data_dir = join(dst_data_dir,"swi_nii")
nii_included_dst_data_dir =  join(nii_excluded_dst_data_dir,"cmb_study")
sif_dir = "Y:"


# #%% 

# patientsID = ['0272922a8e1331758757be7a7460571f',
# '03e55f79b47c1c1e420c86337069e7fc',
# '1fc17604991a94f0f22c5bb72430fe79']

# info_swi_all = pd.read_csv(join(table_dir,'swi_all.csv'))
# info_missing = info_swi_all[ info_swi_all['PatientID'].isin(patientsID)]
# series_directories_df = pd.read_csv(join(table_dir,'series_directories.csv'))

# info_missing = info_missing.merge(series_directories_df,how='inner',on='SeriesInstanceUID')

# for idx,row in info_missing.iterrows():
    
#     print(row['PatientID'])

#     #try to find them in GE folder
#     path_where = join(dst_data_dir,"GE",row['Directory'])
#     files = next(os.walk(dst_data_dir))[2]
#     print("GE files")
#     print(files)
    
#     if (len(files)>0):
#         "There is something in GE directory"
        
#     #get month folder
#     no_month_dir = row['Directory'][8:] if (row['Directory'].split('\\')[0]!='positive') else row['Directory'][9:]
    
#     folders_in_sif = next(os.walk(sif_dir))[1]
#     for folder in folders_in_sif:
#         where_path = join(sif_dir,folder,no_month_dir)
#         if os.path.exists(where_path):
            
#             if len(os.listdir(where_path))>0:
#                 files = next(os.walk(where_path))[2]
#                 print(files)
                
#                 if (len(files)>0):
#                     print(f"There is something in sif {folder}")
                    
#         where_path2 = join(dcm_dst_data_dir,folder,no_month_dir)
#         if os.path.exists(where_path2):
            
#             if len(os.listdir(where_path2))>0:
#                 files = next(os.walk(where_path2))[2]
#                 print(files)
                
#                 if (len(files)>0):
#                     print(f"There is something in sif {folder}")
# #%% rename converted wrong files and move to folder for mostafa to try to fix
# # list_seriesuid = [
# # '498f5653b3c7ca101edc39435fe20f2c', 
# # '96948c17b964fe9177e5a8f081b8fd7d', 
# # 'c8a411565f74abc9ce257d732fa751a3', 
# # '075784a75c16ebb42cabb6d54eeeed1b', 
# # ]

# # # find paths 
# # df_paths = pd.read_csv(join(table_dir, 'series_directories.csv'))
# # df_paths = df_paths[ df_paths['SeriesInstanceUID'].isin(list_seriesuid) ]

# # for idx,row in df_paths.iterrows():
# #     converted_path = join(nii_excluded_dst_data_dir,row['Directory'])
# #     conv_files = [x[2] for x in os.walk(converted_path)]
    
# #     print(row['SeriesInstanceUID'])
# #     print(row['Directory'])
# #     print(conv_files)

# folder1 = "2019_10/ce54bbd4e10b772f5f368d39dcafeadc/d643b7c193fdc0163a042e9298e87df7/MR/498f5653b3c7ca101edc39435fe20f2c"
# im1 = "2019_10/ce54bbd4e10b772f5f368d39dcafeadc/d643b7c193fdc0163a042e9298e87df7/MR/498f5653b3c7ca101edc39435fe20f2c/498f5653b3c7ca101edc39435fe20f2c_Eq_1.nii.gz"
# im1_ph = "2019_10/ce54bbd4e10b772f5f368d39dcafeadc/d643b7c193fdc0163a042e9298e87df7/MR/498f5653b3c7ca101edc39435fe20f2c/498f5653b3c7ca101edc39435fe20f2c_pha_Eq_1.nii.gz"

# folder2 = "2019_10/daba936bc5339f21756ab4c3d06537b3/9e808c88a4ca487d8deec11ae7114321/MR/96948c17b964fe9177e5a8f081b8fd7d"
# im2 = "2019_10/daba936bc5339f21756ab4c3d06537b3/9e808c88a4ca487d8deec11ae7114321/MR/96948c17b964fe9177e5a8f081b8fd7d/96948c17b964fe9177e5a8f081b8fd7d_Eq_1.nii.gz"

# folder3 = "2019_10/ebbd29d2f12ea769f3735e246ee0184d/c6b1c88402506b7f635f1d7c628bcbca/MR/c8a411565f74abc9ce257d732fa751a3"
# im3 = "2019_10/ebbd29d2f12ea769f3735e246ee0184d/c6b1c88402506b7f635f1d7c628bcbca/MR/c8a411565f74abc9ce257d732fa751a3/c8a411565f74abc9ce257d732fa751a3_Eq_1.nii.gz"
# im3_ph = "2019_10/ebbd29d2f12ea769f3735e246ee0184d/c6b1c88402506b7f635f1d7c628bcbca/MR/c8a411565f74abc9ce257d732fa751a3/c8a411565f74abc9ce257d732fa751a3_pha_Eq_1.nii.gz"

# folder4 = "2019_10/f958247b37653f8e02f7d07f02de94c3/f911d01e7c88771428b4bce39b218709/MR/075784a75c16ebb42cabb6d54eeeed1b"
# im4 = "2019_10/f958247b37653f8e02f7d07f02de94c3/f911d01e7c88771428b4bce39b218709/MR/075784a75c16ebb42cabb6d54eeeed1b/075784a75c16ebb42cabb6d54eeeed1b_Eq_1.nii.gz"

# dst_path = join(nii_excluded_dst_data_dir,"cmb_study","nii_new")
# shutil.copy(join(nii_excluded_dst_data_dir,im1),join(dst_path,'100027.nii.gz'))
# shutil.copy(join(nii_excluded_dst_data_dir,im1_ph),join(dst_path,'phases','100027_ph.nii.gz'))
# shutil.copytree(join(dcm_dst_data_dir,folder1),join(nii_excluded_dst_data_dir,"cmb_study","dcm_from_nii_new","100027"))

# shutil.copy(join(nii_excluded_dst_data_dir,im2),join(dst_path,'100028.nii.gz'))
# shutil.copytree(join(dcm_dst_data_dir,folder2),join(nii_excluded_dst_data_dir,"cmb_study","dcm_from_nii_new","100028"))

# shutil.copy(join(nii_excluded_dst_data_dir,im3),join(dst_path,'100029.nii.gz'))
# shutil.copy(join(nii_excluded_dst_data_dir,im3_ph),join(dst_path,'phases','100029_ph.nii.gz'))
# shutil.copytree(join(dcm_dst_data_dir,folder3),join(nii_excluded_dst_data_dir,"cmb_study","dcm_from_nii_new","100029"))

# shutil.copy(join(nii_excluded_dst_data_dir,im4),join(dst_path,'100030.nii.gz'))
# shutil.copytree(join(dcm_dst_data_dir,folder4),join(nii_excluded_dst_data_dir,"cmb_study","dcm_from_nii_new","100030"))

# # list_seriesuid = ['9d4e01787bbfe1da2056efa2fbd5b3c5',
# # '203eb99be47a32c361481136896303c9',
# # '168091681c46aeb8d2dafc42a30e6d65',
# # '0569d2217d7ba26e9801f8bf78eb76e8',
# # '119c20c821c973ecc4abfdde00a41fdd',
# # '498f5653b3c7ca101edc39435fe20f2c',
# # '96948c17b964fe9177e5a8f081b8fd7d',
# # 'c8a411565f74abc9ce257d732fa751a3',
# # '075784a75c16ebb42cabb6d54eeeed1b',
# # 'ac11f79a7709a623309beba66656e537']

# # # find paths 
# # df_paths = pd.read_csv(join(table_dir, 'series_directories.csv'))
# # df_paths = df_paths[ df_paths['SeriesInstanceUID'].isin(list_seriesuid) ]

# # for idx,row in df_paths.iterrows():
# #     sif_path = join(sif_dir,row['Directory'])
# #     hdd_path = join(dcm_dst_data_dir,row['Directory'])
    
# #     sif_files = [x[2] for x in os.walk(sif_path)]
# #     hdd_files = [x[2] for x in os.walk(hdd_path)]
    
# #     print(row['SeriesInstanceUID'])
# #     print(row['Directory'])
# #     print('SIF')
# #     print(sif_files)
# #     print('HDD')
# #     print(hdd_files)

# #%%
# # Taking first 5 with high prob of having CMB from excluded

# df_excl_probs = pd.read_csv(join(table_dir,"ids_swi_excluded_pcmb_v3.csv"))
# series_directories_df = pd.read_csv(join(table_dir,'series_directories.csv'))
# info_swi_all = pd.read_csv(join(table_dir,'swi_all.csv'))

# info_excluded = info_swi_all.merge(df_excl_probs,how='inner',on='PatientID',validate='one_to_one')
# info_excluded = info_excluded.merge(series_directories_df,how='inner',on='SeriesInstanceUID',validate='one_to_one')

# high_5 = info_excluded.head(5)
# low_5 = info_excluded.tail(5)

# for idx,row in high_5:
#     dir = info_excluded['Directory']
#     path = join(dst_data_dir,dir)
    
#     files_in_orig_path =  [f for f in os.listdir(path) if os.path.isfile(join(orig_path, f))]
    
#     shutil.copy(join(orig_path,files_in_orig_path[0]),dst_path)
    
# #%%

# log_file_path = join(nii_included_dst_data_dir,"log_renamed_swi.txt")
# old_path = join(table_dir,"ids_swi_included_old_only_v2.csv")

# df_names = pd.read_csv(log_file_path)
# df_old_ids = pd.read_csv(old_path)
# df_info_swi_all = pd.read_csv(join(table_dir,'swi_all.csv'))

# info_old = df_info_swi_all.merge(df_old_ids,on='PatientID',how='inner',validate='one_to_one')
# info_old = info_old.merge(df_names,on='SeriesInstanceUID',how='inner',validate='one_to_one')


# #%%
# # set new_names
# df_names = pd.read_csv(log_file_path)
# df_new_names = pd.read_csv(join(nii_included_dst_data_dir,"names_new_nii.csv"))

# path_niftis = join(nii_included_dst_data_dir,"nii")
# path_new_niftis = join(nii_included_dst_data_dir,"new_nii")

# filenames_niftis = next(os.walk(path_niftis))[2]
# filenames_new_niftis = next(os.walk(path_new_niftis))[2]
# filenames_niftis.append(filenames_new_niftis)

# df_v3 = pd.read_csv(join(table_dir,"ids_swi_included_v3.csv"))
# df_info_v3 = df_info_swi_all.merge(df_v3,on='PatientID',how='inner',validate='one_to_one')

# df_names_all = pd.concat((df_names,df_new_names))
# downloaded_series = df_names_all['SeriesInstanceUID']
# remaning_patients = df_info_v3[ ~df_info_v3['SeriesInstanceUID'].isin(downloaded_series)]

# # patients that are not included now 
# on_study_v3 = df_names[df_names['SeriesInstanceUID'].isin(df_info_v3['SeriesInstanceUID']) ]

# final_names_v3 = pd.read_csv(join(nii_included_dst_data_dir,"included_nii_v3_names.csv"))

#on_study_v3.to_csv(join(nii_included_dst_data_dir,"included_nii_v3_names.csv"),index=False)

#%%
# Find what exluded are converted already

ids_excl = pd.read_csv(join(table_dir,"ids_swi_excluded_v3.csv"))
info_swi_all = pd.read_csv(join(table_dir,'swi_all.csv'))
info_excluded = info_swi_all[ info_swi_all['PatientID'].isin(ids_excl['PatientID']) ]

series_directories_df = pd.read_csv(join(table_dir,'series_directories.csv'))
info_excluded = info_excluded.merge(series_directories_df,on='SeriesInstanceUID',how='inner',validate='one_to_one')

converted_path = nii_excluded_dst_data_dir

log_file_path = join(nii_excluded_dst_data_dir,"converted_excluded.csv")

if (os.path.exists(log_file_path)):
    log_file = open(log_file_path,'a')
else: 
    log_file = open(log_file_path,'w')
    log_file.write("PatientID,SeriesInstanceUID\n")
    
for idx,row in info_excluded.iterrows():
    
    nii_path = join(converted_path,row['Directory'])
    if (os.path.exists(nii_path)):
        files_inside_folder = next(os.walk(nii_path))[2]
        
        nii_files_inside_folder = filter(lambda file: (file.endswith('.nii.gz') or file.endswith('.nii') ), files_inside_folder)
        
        if (len(list(nii_files_inside_folder))>0):
            log_file.write(f"{row['PatientID']},{row['SeriesInstanceUID']}\n")
            
log_file.close()