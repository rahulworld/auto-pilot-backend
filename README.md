# auto-pilot-backend

# auto-pilot-backend - Time Series Data Analysis with Flask

A Flask web application for performing time series data analysis, including data visualization, preprocessing.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Technologies](#technologies)
- [Contributing](#contributing)
- [License](#license)

## Overview

This project is a web application built with Flask that enables users to upload time series data, visualize it, and perform various analyses such as trend detection, seasonality, and forecasting. The application provides an intuitive interface for data scientists and analysts to quickly explore and analyze time series data.

## Features

- **Data Visualization**: Interactive charts to visualize time series data.
- **Preprocessing**: Data cleaning and transformation options (e.g., handling missing values, resampling) - Later using pandas.
- **Time Series Analysis**: Perform decomposition, trend analysis, and seasonality checks.
- **API Access**: RESTful API for integrating with other applications.

## Installation

To run this project locally, follow these steps:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/rahulworld/auto-pilot-backend
   cd auto-pilot-backend
   ```

2. **Create a virtual environment:**

   ```bash
   python3 -m venv venv
   ```

3. **Activate the virtual environment:**

   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```

4. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

5. **Run the application:**

   ```bash
   flask run
   ```

6. **Open your browser:**

   Navigate to [http://127.0.0.1:5000](http://127.0.0.1:5000) to view the application.

## API Endpoints

The application provides several API endpoints for accessing data and performing operations programmatically:

- **GET /api/defects?type=iphone&defectType=cracked&startDate=2024-06-01&endDate=2024-06-30**: Give Interactive charts and graphs data for selected filter date range, product category and defect type
- **GET /api/products?type=iphone&defectType=cracked&startDate=2024-06-01&endDate=2024-06-30**: Give summary for defect type for specific product type charts and graphs data for selected filter date range and defect type
- **GET /api/get_stats?type=iphone&defectType=cracked&startDate=2024-06-01&endDate=2024-06-30**: Give overview and statical parameter to measure the trends with optimisation for selected filter date range, product category and defect type

Refer to the [API Documentation](docs/API.md) for more details on how to use these endpoints.

## Technologies

- **[Flask](https://flask.palletsprojects.com/)** - A lightweight WSGI web application framework in Python.
- **[Pandas](https://pandas.pydata.org/)** - Data analysis and manipulation library.
- **[NumPy](https://numpy.org/)** - Fundamental package for scientific computing with Python.
- **[Matplotlib](https://matplotlib.org/)** and **[Seaborn](https://seaborn.pydata.org/)** - Libraries for creating static, animated, and interactive visualizations in Python.
- **[Prophet](https://facebook.github.io/prophet/)** - Forecasting tool for time series data.
- **[scikit-learn](https://scikit-learn.org/)** - Machine learning library in Python.
- **[statsmodels](https://www.statsmodels.org/)** - Statistical modeling and testing in Python.

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository
2. Create a new branch: `git checkout -b feature/your-feature-name`
3. Make your changes
4. Commit your changes: `git commit -m 'Add some feature'`
5. Push to the branch: `git push origin feature/your-feature-name`
6. Open a pull request

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Contact

For questions or support, please contact [your-email@example.com](mailto:your-email@example.com).
