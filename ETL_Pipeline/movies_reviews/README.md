# Netflix Movies and TV Shows Pipeline Project

This project demonstrates the end-to-end process of building a data pipeline using **IBM StreamSets** to process and load Netflix Movies and TV Shows data into a **Snowflake** database. The pipeline focuses on data ingestion, cleaning, transformation, and loading, making the dataset ready for analytical and reporting use cases.


---


![Pipeline Flowchart](https://github.com/Dislevekanku/datascienceprojects/blob/master/ETL_Pipeline/movies_reviews/code/pipeline.png)

---
## Project Overview

The pipeline processes the Netflix Movies and TV Shows dataset. The main objective is to:
- Ingest the dataset into StreamSets.
- Perform data cleaning and transformations.
- Enrich the data with calculated fields.
- Load the cleaned and transformed data into a Snowflake target table.

---

## Features

1. **Data Preprocessing**:
   - Classification of movies into age categories based on `rating`.

2. **Transformations**:
   - New calculated column: `country_year` (concatenating `country` and `release_year`).

3. **Target Table**:
   - Cleaned and enriched data is stored in Snowflake for analytics.

4. **StreamSets Integration**:
   - Configured pipeline stages for reading, processing, and writing data.

---

## Dataset Description

**Source**: [Netflix Movies and TV Shows Dataset](https://www.kaggle.com/shivamb/netflix-shows)

The dataset contains the following fields:
- **show_id**: Unique identifier for the show.
- **type**: Indicates whether the entry is a Movie or TV Show.
- **title**: Name of the Movie/TV Show.
- **director**: Director of the Movie/TV Show.
- **cast**: Leading actors in the Movie/TV Show.
- **country**: Country where the show was produced.
- **date_added**: Date when the show was added to Netflix.
- **release_year**: Year of release.
- **rating**: Age rating of the show.
- **duration**: Duration of the show.
- **listed_in**: Genres of the show.
- **description**: Summary of the show.

---

## Prerequisites

1. **Tools and Technologies**:
   - IBM StreamSets (Data Collector or Transformer)
   - Snowflake database
   - Python (for data preprocessing if necessary)
   - Excel (for dataset cleanup)

2. **Environment Setup**:
   - Snowflake account and workspace
   - StreamSets account with a configured pipeline environment

3. **Libraries** (Optional for local preprocessing):
   ```bash
   pip install pandas
   pip install openpyxl


## Pipeline Configuration

The complete pipeline used for this project has been exported from StreamSets and is included in this repository.

### How to Import the Pipeline

1. Open **StreamSets Data Collector**.
2. Navigate to the **Pipeline** menu and select **Import Pipeline**.
3. Upload the exported pipeline file located in this repository.
4. Review the configurations and ensure the source file paths, Snowflake credentials, and transformations align with your environment.
5. Start the pipeline and monitor the progress in the dashboard.

### File Details

- **Pipeline Export File**: [`netflix_pipeline.json`](https://github.com/Dislevekanku/datascienceprojects/blob/master/ETL_Pipeline/movies_reviews/code/tya0bf5391-62ee-4348-be9e-5b6ec41b9e5e_9eb54357-ab74-11ef-a409-83d6150da07b.json)
  - Contains the fully configured pipeline, including:
    - **Data Origin**: CSV file reader.
    - **Transformations**: Field mapping, date formatting, and data enrichment.
    - **Destination**: Snowflake table mapping and credentials.

### Modifying the Pipeline

If you need to customize the pipeline:
1. Open the imported pipeline in StreamSets.
2. Modify the stages or configurations as per your requirements.
3. Save the pipeline with a new name for future reference.

