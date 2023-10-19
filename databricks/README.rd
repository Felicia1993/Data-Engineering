Introduction to Databricks

Databricks was launched as a Spark-based unified data analytics platform in the cloud.
Databricks provides a collaborative platform for data engineering and data science.
It has also revolutionized the existing data lakes by introducing the lakehouse architecture.

A one-stop solution for everything data

## Ingest data
download data files into the Databricks file system (DBFS)  
%sh
rm -r /dbfs/data     
mkdir /dbfs/data      
wget -O /dbfs/data/2019.csv https://raw.githubusercontent.com/MicrosoftLearning/dp-203-azure-data-engineer/master/Allfiles/labs/24/data/2019.csv     
wget -O /dbfs/data/2020.csv https://raw.githubusercontent.com/MicrosoftLearning/dp-203-azure-data-engineer/master/Allfiles/labs/24/data/2020.csv     
wget -O /dbfs/data/2021.csv https://raw.githubusercontent.com/MicrosoftLearning/dp-203-azure-data-engineer/master/Allfiles/labs/24/data/2021.csv    

 
