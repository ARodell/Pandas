
# Dependencies and Setup
import pandas as pd
import numpy as np

# File to Load 
school_data_to_load = "../Desktop/Pandas/Resources/schools_complete.csv"
student_data_to_load = "../Desktop/Pandas/Resources/students_complete.csv"

# Read School and Student Data File and store into Pandas Data Frames
school_data = pd.read_csv(school_data_to_load)
student_data = pd.read_csv(student_data_to_load)

# Combine the data into a single dataset
schooldata_merged = pd.merge(student_data, school_data, how="left", on=["school_name", "school_name"])
schooldata_merged

# Rename header row
schooldata_renameheader = schooldata_merged.rename(columns={"student_name":"Student Name", "gender" : "Gender", "grade":"Grade", "school_name":"School Name", "reading_score": "Reading Score", "math_score": "Math Score", "type":"School Type", "size" : "Number of Students", "budget" :"School Budget"})
schooldata_renameheader.head()

#Remove duplicates
district_deduped = schooldata_renameheader.drop_duplicates("School Name")

#Calculate total number of schools
total_schools = district_deduped["School Name"].count()
total_schools

#Calculate the total number of students
total_students = district_deduped["Number of Students"].sum()
total_students

#Calculate the total budget
total_budget = district_deduped["School Budget"].sum()
total_budget

#Calculate the average math score 
avg_math = schooldata_renameheader["Math Score"].mean()
avg_math

#Calculate the average reading score
avg_reading = schooldata_renameheader["Reading Score"].mean()
avg_reading

#Calculate the overall passing rate (overall average score), i.e. (avg. math score + avg. reading score)/2
passing_rate = (avg_math + avg_reading)/2
passing_rate

#Dataframe to locate math scores greater than or equal to 70
passing_math = schooldata_renameheader.loc[schooldata_renameheader["Math Score"] >= 70]
passing_math

#Calculate the percentage of students with a passing math score (70 or greater)
passing_mathcount = passing_math["Math Score"].count
passing_mathpercent = passing_math["Math Score"].sum()/passing_mathcount()
passing_mathpercent

#Dataframe to locate reading scores greater than or equal to 70
passing_reading = schooldata_renameheader.loc[schooldata_renameheader["Reading Score"] >= 70]
passing_reading

#Calculate the percentage of students with a passing reading score (70 or greater)
passing_readingcount = passing_reading["Reading Score"].count
passing_readingpercent = passing_reading["Reading Score"].sum()/passing_readingcount()
passing_readingpercent

#Create a dataframe to hold the above results
district_results = {"Total Schools": [total_schools] , "Total Students": [total_students], "Total Budget": [total_budget],"Average Math Score": [avg_math], "Average Reading Score": [avg_reading], "% Passing Reading": [passing_readingpercent], "% Passing Math": [passing_mathpercent], "% Overall Passing Rate": [passing_rate]}
district_results_df = pd.DataFrame(district_results)
district_results_df

#Calculate the per student budget
perstudent_budget = schooldata_renameheader.loc[schooldata_renameheader[(total_budget) / (total_students)]]
perstudent_budget

# Build summary table with school name as index
school_summary = {"Total Schools": [total_schools] , "Total Students": [total_students], "Total Budget": [total_budget], "Per Student Budget" : [perstudent_budget],"Average Math Score": [avg_math], "Average Reading Score": [avg_reading], "% Passing Reading": [passing_readingpercent], "% Passing Math": [passing_mathpercent], "% Overall Passing Rate": [passing_rate]}
school_summary_df = pd.DataFrame(school_summary)

# Set the index of this new dataframe to be the school name
schoolname_index = school_summary_df.set_index("School Name")
schoolname_index


# Description of at least two observable trends based on the data.
# From these school data, it is observed that the district wide percentage of students passing math is 84.5% with a score of 70 or higher. Similarly, the percentage of students passing reading is 84.5% with a score of 70 or higher. 

