MS_Zoning = {'A':1, 'C':2, 'FV':3, 'I': 4, 'RH':5, 'RL':6, 'RP':7, 'RM':8}
Street = {'Grvl':1, 'Pave':2}
Alley  = {'Grvl':1, 'Pave':2, 'NA':0}
Lot_Shape = {'Reg':1, 'IR1':2, 'IR2':3, 'IR3':4}
Land_Contour = {'Lvl':1, 'Bnk':2, 'HLS':3, 'Low':4}
Utilitie = {'AllPub':1, 'NoSewr':2, 'NoSeWa':3, 'ELO':4}
Lot_Config = {'Inside':1, 'Corner':2, 'CulDSac':3, 'FR2':4, 'FR3':5}
Land_Slope = {'Gtl':1, 'Mod':2, 'Sev':3}
Neighborhood = {'Blmngtn':1, 'Blueste':2, 'BrDale':3, 'BrkSide':4, 'ClearCr':5,
                'CollgCr':6, 'Crawfor':7, 'Edwards':8, 'Gilbert':9, 'Greens':10,
                'GrnHill':11, 'IDOTRR':12, 'Landmrk':13, 'MeadowV':14, 'Mitchel':15,
                'Names':16, 'NoRidge':17, 'NPkVill':18, 'NridgHt':19, 'NWAmes':20,
                'OldTown':21, 'SWISU':22, 'Sawyer':23, 'SawyerW':24, 'Somerst':25,
                'StoneBr':26, 'Timber':27, 'Veenker':28}
Condition_1 = {'Artery':1, 'Feedr':2, 'Norm':3, 'RRNn':4, 'RRAn':5, 'PosN':6,
               'PosA':7, 'RRNe':8, 'RRAe':9}
Condition_2 = {'Artery':1, 'Feedr':2, 'Norm':3, 'RRNn':4, 'RRAn':5, 'PosN':6,
               'PosA':7, 'RRNe':8, 'RRAe':9}
Bldg_Type   = {'1Fam':1, '2FmCon':2, 'Duplx':3, 'TwnhsE':4, 'TwnhsI':5}
House_Style = {'1Story':1, '1.5Fin':2, '1.5Unf':3, '2Story':4, '2.5Fin':5, "2.5Unf":6,
               'SFoyer':7, 'SLvl':8}
Overall_Qual = {'Very Excellent':10, 'Excellent':9, 'Very Good':8, 'Good':7,
                'Above Average':6, 'Average':5, 'Below Average':4, 'Fair':3,
                'Poor':2, 'Very Poor':1}
Overall_Cond = {'Very Excellent':10, 'Excellent':9, 'Very Good':8, 'Good':7,
                'Above Average':6, 'Average':5, 'Below Average':4, 'Fair':3,
                'Poor':2, 'Very Poor':1}
Roof_Style = {'Flat':1, 'Gable':2, 'Gambrel':3, 'Hip':4, 'Mansard':5, 'Shed':6}
Roof_Matl  = {'ClyTile':1, 'CompShg':2, 'Membran':3, 'Metal':4, 'Roll':5, 'Tar&Grv':6,
              'Tar&Grv':7, 'WdShake':8, 'WdShngl':9}
Exterior_1 = {'AsbShng':1, 'AsphShn':2, 'BrkComm':3, 'BrkFace':4, 'CBlock':5,
              'CemntBd':6, 'HdBoard':7, 'ImStucc':8, 'MetalSd':9, 'Other':10,
              'Plywood':11, 'PreCast':12, 'Stone':13, 'Stucco':14, 'VinylSd':15,
              'Wd Sdng':16, 'WdShing':17}
Exterior_2 = {'AsbShng':1, 'AsphShn':2, 'BrkComm':3, 'BrkFace':4, 'CBlock':5,
              'CemntBd':6, 'HdBoard':7, 'ImStucc':8, 'MetalSd':9, 'Other':10,
              'Plywood':11, 'PreCast':12, 'Stone':13, 'Stucco':14, 'VinylSd':15,
              'Wd Sdng':16, 'WdShing':17}
Mas_Vnr_Type = {'BrkCmn':1, 'BrkFace':2, 'CBlock':3, 'None':4, 'Stone':5}
Exter_Qual = {'Ex':1, 'Gd':2, 'TA':3, 'Fa':4, 'Po':5}
Exter_Cond = {'Ex':1, 'Gd':2, 'TA':3, 'Fa':4, 'Po':5}
Foundation = {'BrkTil':1, 'CBlock':2, 'PConc':3, 'Slab':4, 'Stone':5, 'Wood':6}
Bsmt_Qual = {'Ex':1, 'Gd':2, 'TA':3, 'Fa':4, 'Po':5, 'NA':0}
Bsmt_Cond = {'Ex':1, 'Gd':2, 'TA':3, 'Fa':4, 'Po':5, 'NA':0}
Bsmt_Exposure = {'Gd':1, 'Av':2, 'Mn':3, 'No':4, 'NA':0}
BsmtFin_Type_1 = {'GLQ':1, 'ALQ':2, 'BLQ':3, 'Rec':4, 'LwQ':5, 'Unf':6, 'NA':0}
BsmtFin_Type_2 = {'GLQ':1, 'ALQ':2, 'BLQ':3, 'Rec':4, 'LwQ':5, 'Unf':6, 'NA':0}
Heating   = {'Floor':1, 'GasA':2, 'GasW':3, 'Grav':4, 'OthW':5, 'Wall':6}
HeatingQC = {'Ex':1, 'Gd':2, 'TA':3, 'Fa':4, 'Po':5}
Central_Air = {'N':1, 'Y':2}
Electrical  = {'SBrkr':1, 'FuseA':2, 'FuseF':3, 'FuseP':4, 'Mix':5}
KitchenQual = {'Ex':1, 'Gd':2, 'TA':3, 'Fa':4, 'Po':5}
Functional = {'Typ':1, 'Min1':2, 'Min2':3, 'Mod':4, 'Maj1':5, 'Maj2':6, 'Sev':7,
              'Sal':8}
FireplaceQu = {'Ex':1, 'Gd':2, 'TA':3, 'Fa':4, 'Po':5, 'NA':0}
Garage_Type = {'2Types':1, 'Attchd':2, 'Basment':3, 'BuiltIn':4, 'CarPort':5,
               'Detchd':6, 'NA':0}
Garage_Finish = {'Fin':1, 'RFn':2, 'Unf':3, 'NA':0}
Garage_Qual = {'Ex':1, 'Gd':2, 'TA':3, 'Fa':4, 'Po':5, 'NA':0}
Garage_Cond = {'Ex':1, 'Gd':2, 'TA':3, 'Fa':4, 'Po':5, 'NA':0}
Paved_Drive = {'Y':1, 'P':2, 'N':3}
Pool_QC = {'Ex':1, 'Gd':2, 'TA':3, 'Fa':4, 'NA':0}
Fence = {'GdPrv':1, 'MnPrv':2, 'GdWo':3, 'MnWw':4, 'NA':0}
Misc_Feature = {'Elev':1, 'Gar2':2, 'Othr':3, 'Shed':4, 'TenC':5, 'NA':0}
Sale_Type = {'WD':1, 'CWD':2, 'VWD':3, 'New':4, 'COD':5, 'Con':6, 'ConLw':7,
             'ConLI':8, 'ConLD':9, 'Oth':10}
Sale_Condition = {'Normal':1}
