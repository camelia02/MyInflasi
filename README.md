# Grocery Price Visualization and Analysis Project 🛒📊

Welcome to the Grocery Price Visualization and Analysis project! This repository showcases my exploration into the daily average prices of grocery items in Malaysia, aiming to uncover trends, patterns, and insights within the consumer market.

## Project Highlights

- 📈 **Visualizing Trends**: Explore interactive visualizations that reveal the daily price trends for different categories of grocery items over time.

- 📅 **Temporal Analysis**: Uncover seasonal variations and long-term fluctuations in grocery prices to gain insights into consumer behavior and market dynamics.

- 📊 **Correlation Studies**: Investigate potential correlations between price changes and external factors such as economic indicators and supply chain disruptions.

## Data Sources

The analysis is based on meticulously curated data from reliable sources, ensuring accuracy and relevance in our findings.

## Directory Structure

Here's a quick overview of the project structure:

├── data/ # MyInflasi/pricecathcer

├── notebooks/ # analyser.ipynb

├── visualizations/ # Visualizations generated during the analysis

└── README.md # Project overview and documentation. This is the current file that you are in!

# Getting Started

To explore the project, follow these steps:

1. Clone this repository: `git clone https://github.com/camelia02/MyInflasi.git`
2. Navigate to the project directory: `cd MyInflasi`
3. **Data**: Explore the `data/` directory to find both raw and processed data files used in the analysis. The raw data have been obtained through web scraping of grocery price websites. To get the newest data, navigate to the spider directory, 'cd pricecatcher/pricecatcher/spiders' then run the spider 'scrapy crawl pricespider -o 'file.json'. If the extraction is successful you can import the json file into the jupyter notebook.
4. **Analysis**: Check out the Jupyter notebooks in the `notebooks/` directory for a detailed breakdown of the data analysis process.
5. **Visualizations**: Visit the `visualizations/` directory to view the charts and graphs created during the analysis.

For more comprehensive insights, a report will be available.

## Connect with Me

I'm excited to share this project with you! Let's connect and discuss:

- LinkedIn:[(https://www.linkedin.com/in/camelia-ariana/)](https://www.linkedin.com/in/camelia-ariana/)]

Your feedback and collaboration are greatly appreciated!


## REQUIRED DEPENDENCIES
- pandas
- numpy
- matplotlib
- pyarroq
- fastparquet
- dask
- fuzzywuzzy
- ipywidgets
- ipython
- jupyter_contrib_nbextensions
- requests
- aiohttp

For the spider environment install scrappy

use pip install in terminal

---
**Note**: This project was conducted as a personal exploration into data analysis and visualization. The findings presented here are not intended for commercial use.
