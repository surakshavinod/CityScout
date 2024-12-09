# CityScout: Identifying Safe Cities Based on Crime Statistics

CityScout is a tool designed to help users identify safe cities based on specific demographic factors and crime statistics. Whether you're planning a vacation or considering a move, CityScout provides tailored safety information to meet your unique needs.

Group members: Abhay Sastry, Jessica Eggers, Kunal Mohindra, Rameen Gauher, Sai Karyekar, Suraksha Vinod

Contribution: 
- Abhay and Suraksha: Data Processing
- Kunal and Rameen: Machine Learning
- Jessica and Sai: Visualization

## Introduction

Safety is a top priority when choosing a place to live or visit. While general crime statistics are widely available, they often fail to address specific demographic concerns. CityScout bridges this gap by providing tailored safety information based on user-selected criteria, such as crime rates against women, children, or tourists.

## Dashboard

Explore our interactive dashboard here: [CityScout Dashboard](https://public.tableau.com/app/profile/sai.paresh.karyekar/viz/CityScout_17316885780750/Dashboard1#1)

### How to Use the Dashboard

1. Open the CityScout link provided above.
2. Select your demographic category of interest (e.g., women traveling solo, children, tourists).
3. View the interactive choropleth map displaying a heat map representing the risk score for different states.
4. Adjust the population filter using the sliding bar to refine your results.
5. Explore the list of top 10 safe cities based on the calculated crime risk scores.
6. Switch to State view to narrow down your results to a particular state and view the county-wise choropleth map with cities reflecting the state filter.
7. Analyze the top crimes for the selected category or states to make an informed decision.

   
## Technology Stack

- Python
- Pandas
- PySpark
- Google Cloud Platform (GCP)
- Dolthub (for database management)
- Tableau

## Project Structure

The project consists of three main components:

1. **Data Processing:**
   - `dolt_test.py`: Queries the database hosted on DoltHub (for reference)
   - `doltSQLCommands.txt`: Consists of the commands used to extract relevant tables
   - `data_merge_and_clean.ipynb`: Cleans and merges the tables to get the final file
   - `merge.py`: Merges various datasets extracted for each year or feature (only if you stop with merging all the files using PySpark `final_all_df.write.csv('gs://6242filteringbucket/final_all.csv', header=True)` in the data_merge_and_clean.ipynb notebook; if you follow the notebook, this is not needed)

2. **Machine Learning:**
   - `Risk_Score_Calcuation.ipynb`: Script that uses the processed data calculates all of the risk scores for each person and each city based on a person's demographic attributes
   - `Offense_By_Categories.ipynb`: Script that uses the processed data to find the crimes most associated with victims that are of a specific demographic
3. **Tableau Dashboard:**
   - Interactive visualization of processed data

## Data Source

The final dataset (~2GB) used for analysis is available on Google Drive: [Merged Dataset Link](https://drive.google.com/file/d/1bwY2fyMjmfNOJpI-wdUImQXk9CvTFs9E/view)

## Development

Data processing operations were performed using Python's PySpark and Pandas on the Google Cloud Platform to handle the large dataset size and computational requirements. The original dataset can be found here [Dataset Link](https://www.dolthub.com/repositories/Liquidata/fbi-nibrs)

1.  Install Dolt by [building from source](https://docs.dolthub.com/introduction/installation/source).
2.  Clone the FBI NIBRS data repository hosted on Dolthub [here](https://www.dolthub.com/repositories/Liquidata/fbi-nibrs) using the command `dolt clone Liquidata/fbi-nibrs`. Please keep in mind that this is a 1.1TB database, so ensure you have sufficient storage space.
3.  Extract the relevant information for the tables using the commands present in the [doltSQLCommands.txt file](https://github.com/abhaysastry1/cityscout/blob/main/doltSQLCommands.txt).
4. Run the [data_merge_and_clean.ipynb](https://github.com/abhaysastry1/cityscout/blob/main/data_merge_and_clean.ipynb) script to get the necessary columns and merge the files to get the final output file for further analysis. The script uses PySpark. Ensure the file path is correct when running the script.
5. The final2017_2021_merged.csv file was used in further analyses.

Alternatively, please feel free to access the data used for our tool, which is linked under Data Source.

## Machine Learning and Regression Analysis
We employ TF-IDF and random forest to:
- Filter out relevant offenses for each demographic category using machine learning.
  To classify offenses into categories:
1. Download the [Merged Dataset Link](https://drive.google.com/file/d/1bwY2fyMjmfNOJpI-wdUImQXk9CvTFs9E/view) to your Google Drive
2. Run the [Offense By Categories.ipynb](https://github.com/abhaysastry1/cityscout/blob/main/Offense_By_Categories.ipynb) notebook to categorize  offenses into relevant categories.
3. Download the `offense_classifications_by_category.csv` file produced by the script

- Calculate risk scores based off of key features in the dataset(e.g. population, age_num, sex_code, race, resident_status_code, offense_name)
To calculate the risk scores for the dataset:
1. Download the [Merged Dataset Link](https://drive.google.com/file/d/1bwY2fyMjmfNOJpI-wdUImQXk9CvTFs9E/view) to your Google Drive
2. Run the [Risk_Score_Calculation.ipynb](https://github.com/abhaysastry1/cityscout/blob/main/Risk_Score_Calculation.ipynb) script to find the risk scores for each person in each city based on their demographic attributes
3. Download the `FinalCityDataRiskScores.csv` file produced by the script


## Limitations
- The current dataset is static and does not include real-time updates.
- Some states are not included in the dataset due to data availability constraints.
- The dashboard is currently available only as a Tableau visualization.

## Future Enhancements

- Incorporate real-time data updates
- Expand demographic categories
- Incorporate missing states
- Develop mobile applications for on-the-go access
