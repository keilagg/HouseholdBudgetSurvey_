# HouseholdBudgetSurvey_
Insights on mobility from Household Budget Surveys (HBS) around the world.

### Table of Contents

1. [Installation](#installation)
2. [Project Motivation](#motivation)
3. [File Descriptions](#files)

## Installation <a name="installation"></a>
This code was run using the environment set up in parent folder. The required libraries should be in requirements.txt.


## Objectives <a name="motivation"></a>
These files are intended to take hourly lectures of pollutants and return:
- Wrangling and preparation of datasets (from long format to wide, handling of missing values, etc.)
- Yearly statistics.
- Interpolation over territory using kriging.

## File Descriptions <a name="files"></a>
- The documentation.md file has the notation used to produce yearly pollutant estimator values.  
- The notebooks have wrangling and verification files.  
- Folders contain the historic data for: stations-location, stations measurements and the correlation matrices of these territories.
  - Madrid_data_preparation.ipynb  
      - First parts show objectives and description of Madrid's pollution measurement files.  
      - A dataframe with all hourly lectures for a whole year is created;  
      - A visual statistical inspection is carried out;   
      - Central tendency measurements are obtained yearly for each pollutant.  
  - Pollutant_data_preparation.ipynb  
      - Generalization of the previous notebook for data obtained with European format.
- Helper files hold functions used in the notebooks.  
  - Helper.py  
      - obtains yearly central tendency measurements for given pollutants for valid values (used in notebooks).     
  - Pollutant.py    
      - Another way of obtaining yearly central tendency measurements (using groupby). Not reliable.    
  - Helper_AQ_Verification.py  
      - Functions used to carry out the statistic assessment of the hexagon kpi -air quality relationship.  
