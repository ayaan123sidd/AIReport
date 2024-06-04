import pandas as pd
import os

# List of CSV files to merge
csv_files = [
    'C:\\Users\\Admin\\Desktop\\AIReportAcademically\\ExcelMerge\\11thFebAMCPLAB_Report_2.csv',
    'C:\\Users\\Admin\\Desktop\\AIReportAcademically\\ExcelMerge\\3rdmarchOCANZWebinar_Report_march1.csv',
    'C:\\Users\\Admin\\Desktop\\AIReportAcademically\\ExcelMerge\\ADCMasterclass_Report_feb8.csv',
    'C:\\Users\\Admin\\Desktop\\AIReportAcademically\\ExcelMerge\\ADCMasterclass_Report_march8.csv',
    'C:\\Users\\Admin\\Desktop\\AIReportAcademically\\ExcelMerge\\ADCWebinar_Report_feb5.csv',
    'C:\\Users\\Admin\\Desktop\\AIReportAcademically\\ExcelMerge\\ADeepDiveintotheKAPSExamforPharmacistsinAustralia_Report_may5.csv',
    'C:\\Users\\Admin\\Desktop\\AIReportAcademically\\ExcelMerge\\APCWebinar_Report_feb3.csv',
    'C:\\Users\\Admin\\Desktop\\AIReportAcademically\\ExcelMerge\\APCWebinar1_Report_april1.csv',
    'C:\\Users\\Admin\\Desktop\\AIReportAcademically\\ExcelMerge\\APeekintotheAMCExamBecomingaRegisteredDoctorinAust_Report_aprl5.csv',
    'C:\\Users\\Admin\\Desktop\\AIReportAcademically\\ExcelMerge\\AWebinarExploringADCExamforDentalRegistrationinAus_Report_march5.csv',
    'C:\\Users\\Admin\\Desktop\\AIReportAcademically\\ExcelMerge\\EmpoweringGlobalNursesandLabTechniciansNavigatingt_Report_may3.csv',
    'C:\\Users\\Admin\\Desktop\\AIReportAcademically\\ExcelMerge\\EngagingDiscussionforGlobalDoctorsWillingtoMigrate_Report_march4.csv',
    'C:\\Users\\Admin\\Desktop\\AIReportAcademically\\ExcelMerge\\InsightsIntotheNCLEXforNursesandAIMSExamforLabTech_Report_march3.csv',
    'C:\\Users\\Admin\\Desktop\\AIReportAcademically\\ExcelMerge\\KAPSWebinaronthePharmacyRegistrationExamofAustrali_Report_march2.csv',
    'C:\\Users\\Admin\\Desktop\\AIReportAcademically\\ExcelMerge\\MasteringEnglishLanguageforOverseasMigrationwithPT_Report_feb6.csv',
    'C:\\Users\\Admin\\Desktop\\AIReportAcademically\\ExcelMerge\\MasteringEnglishLanguageforOverseasMigrationwithPT_Report_march6.csv',
    'C:\\Users\\Admin\\Desktop\\AIReportAcademically\\ExcelMerge\\MasteringtheNCLEXandAIMSExamsforNursingandLabTechn_Report_april4.csv',
    'C:\\Users\\Admin\\Desktop\\AIReportAcademically\\ExcelMerge\\MedicalCareerintheUSandtheUKRoadmaptoDoctorsLicens_Report_april8.csv',
    'C:\\Users\\Admin\\Desktop\\AIReportAcademically\\ExcelMerge\\OCANZCOEExamWebinar_Report_april3.csv',
    'C:\\Users\\Admin\\Desktop\\AIReportAcademically\\ExcelMerge\\PathwaytoOverseasDentistRegistrationinAustraliawit_Report_april7.csv',
    'C:\\Users\\Admin\\Desktop\\AIReportAcademically\\ExcelMerge\\PharmaKineticMasteryExploringDrugRelatedKnowledgeA_Report_april2.csv',
    'C:\\Users\\Admin\\Desktop\\AIReportAcademically\\ExcelMerge\\RoadmaptoBecomeaPharmacistinIrelandAWebinarAboutth_Report_may1.csv',
    'C:\\Users\\Admin\\Desktop\\AIReportAcademically\\ExcelMerge\\TheAMCRegistrationJourneytoBecomeaDoctorinAustrali_Report_may4.csv',
    'C:\\Users\\Admin\\Desktop\\AIReportAcademically\\ExcelMerge\\ThePathtoanOptometryCareerinAustraliaUnderstanding_Report_may2.csv',
    'C:\\Users\\Admin\\Desktop\\AIReportAcademically\\ExcelMerge\\UncoveringtheKAPSExamforPharmacistRegistrationinAu_Report_april6.csv',
    'C:\\Users\\Admin\\Desktop\\AIReportAcademically\\ExcelMerge\\USMLEMasterclass_Report_feb7.csv',
    'C:\\Users\\Admin\\Desktop\\AIReportAcademically\\ExcelMerge\\USMLEMasterclass_Report_march7.csv',
    'C:\\Users\\Admin\\Desktop\\AIReportAcademically\\ExcelMerge\\USMLEWebinar_Report_feb4.csv',
    'C:\\Users\\Admin\\Desktop\\AIReportAcademically\\ExcelMerge\\Webinar_Report_Feb1.csv',
]

dfs = []

for file in csv_files:
    if os.path.exists(file):
        try:
            df = pd.read_csv(file)
            dfs.append(df)
            print(f"Successfully loaded: {file}")
        except Exception as e:
            print(f"Error reading {file}: {e}")
    else:
        print(f"File not found: {file}")

if dfs:  # Check if dfs list is not empty
    merged_df = pd.concat(dfs, ignore_index=True)
    # Write the merged dataframe to a new Excel file
    merged_df.to_excel('zz1merged_output.xlsx', index=False)
    print("Merging completed. The merged file is saved as 'merged_output.xlsx'.")
else:
    print("No files were merged. Please check the file paths.")
