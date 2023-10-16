**INF1002 G29 - Predictive Data Analysis on HDB Resale Prices**

This project focuses on predictive data analysis of HDB resale prices in Singapore. The goal is to uncover trends, patterns, and factors affecting HDB prices through comprehensive data analysis and visualization techniques.

**Group Members** 
* SAITO YUGO (2301793) 
* IMMANUEL LOH JUN KAI (2301796) 
* CHAI JUN YU (2301847)
* CHIA QI JUN (2301848)
* CHUA SHING YING (2301932)

**Table of Contents**
+ [Features](#features)
+ [Content](#contents)
+ [Installation](#installation)
+ [Usage](#usage)


# Features

These are the key features of the project:

- Web scraper to supplement open-source dataset (`/web_scraper`)
- Data Analysis techniques and Visualization tools (`/data_visualization/data_visualization.py`)
- Machine Learning (`/machine_learning/machine_learning.py`)
- Predictive Analysis with Hyperparameters Tuning (`/machine_learning/machine_learning.py` and `/machine_learning/tuning_hyperparam.py`)
- Graphical User Interface (`client/src/App.vue`)


# Contents

The contents within this zip file and repository are as follows:

* `amenities` folder - contains `get_amenities.py` file that accesses the respective column in `/csv_files/amenities.csv`. Given a postal code input, the function selects the corresponding row with that postal code and retrieves the value from the specified column.
* `client` folder - contains the source codes used to build our Graphical User Interface (GUI).
* `csv_files` folder - contains all the processed csv files used for this project.
* `data_visualization` folder - contains `data_visualization.py` file that has all the codes of basic charts we used to explore to gain deeper understanding of the data used.
* `machine_learning` folder - contains everything pertaining to our usage machine learning and hyperparameters tuning.
* `node_modules` folder - contains all CSS and Bootstrap files to style our GUI.
* `opensource_dataset` folder - contains all the raw open-sourced csv files we took from data.gov.sg, as well `dataset.py` that we used to preprocess the raw data.
* `templates` folder contains `heatmap_map.html` which is the folium heatmap generated to provide an effective visualization of the distribution, density and resale price of HDB across Singapore.
* `web_scraper` folder contains everything related to our web scrapped dataset used to complement the open-sourced dataset from data.gov.sg
* `app.py` is the main Flask application that houses this Project.


# Installation

# Getting Git Repository
git clone https://github.com/melwin911/INF1002

# Installing npm 
pip install node.js

cd client

npm install


# Usage 

# Run flask app
flask run app.py

# Run vue.js
cd client

npm run dev




