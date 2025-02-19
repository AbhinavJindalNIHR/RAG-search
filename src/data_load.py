#load dependencies
from sql_conn import connection #SQL connection details and variables
import pandas as pd


#set SQL query
s='''
        SELECT 
        StudyID
        ,[StudyTitle]
        ,[StudyShortName]
        ,StudyResearchSummary
        ,StudyInclusionCriteria
        ,StudyDesignType
        ,StudyPhases_Concatenated
        ,StudySettings_Concatenated
        ,StudyManagingSpecialty
        ,StudyManagingSpecialty_PrimarySubSpecialty
        ,Study_IsCommercial
        ,Study_IsDraft

        FROM [CPMS_BI].[dbo].[ODP_Study]

    '''

#Loading data
study_df = pd.read_sql(s, connection)
#pre-processing
data = study_df.fillna("not available")
#combine text data into one column
data['Text'] = data['StudyTitle'] + " " + data['StudyResearchSummary'] + " "+ data['StudyInclusionCriteria']