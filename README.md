# 🌍 Climate Analysis Dashboard

> A comprehensive web-based application for analyzing global temperature data and predicting future climate trends using Apache Spark and Machine Learning

[![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)](https://www.python.org/)
[![Spark](https://img.shields.io/badge/Apache%20Spark-4.0.0-orange.svg)](https://spark.apache.org/)
[![Gradio](https://img.shields.io/badge/Gradio-5.41.1-green.svg)](https://gradio.app/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 📊 Overview

The Climate Analysis Dashboard is a powerful, interactive web application that combines the efficiency of Apache Spark with modern machine learning capabilities to provide comprehensive insights into global climate patterns. Built with Python and featuring a user-friendly Gradio interface, this tool enables researchers, climate scientists, and data analysts to explore historical temperature data and make predictions about future climate trends.

## ✨ Key Features

### 🏃‍♂️ Country Analysis
- **Interactive Analysis**: Detailed climate analysis for 200+ countries
- **Multiple Analysis Types**: Overview, Monthly Patterns, Yearly Trends, Temperature Anomalies, Seasonal Analysis
- **Flexible Date Ranges**: Analyze data from 1750 to 2013
- **Statistical Insights**: Z-score based anomaly detection and pattern recognition

### 🔮 AI Temperature Predictions
- **Multiple ML Models**: Linear Regression, Random Forest, Gradient Boosting
- **Customizable Forecasts**: Predict 1-20 years into the future
- **Confidence Intervals**: Uncertainty quantification for predictions
- **Model Performance**: Real-time R², RMSE, and F1 score metrics

### 🌍 Global Comparisons
- **Multi-Country Analysis**: Compare climate metrics across multiple countries
- **Comparative Metrics**: Average Temperature, Temperature Range, Temperature Variability
- **Interactive Visualizations**: Dynamic charts and graphs

### ⚡ System Monitoring
- **Real-Time Performance**: Spark cluster monitoring and optimization
- **Resource Management**: Memory usage and caching status
- **Data Statistics**: Dataset overview and processing metrics

## 🛠️ Technology Stack

### Backend
- **Python 3.12**: Core programming language
- **Apache Spark 4.0.0**: Distributed data processing
- **PySpark**: Python API for Spark
- **Pandas & NumPy**: Data manipulation and analysis

### Frontend
- **Gradio 5.41.1**: Web interface framework
- **Plotly**: Interactive visualizations
- **HTML/CSS/JavaScript**: Custom styling and interactions

### Machine Learning
- **Scikit-learn**: ML model implementation
- **Custom Algorithms**: Temperature prediction models
- **Statistical Analysis**: Anomaly detection and pattern recognition

### Data Processing
- **Parquet Files**: Optimized data storage
- **Snappy Compression**: Efficient data compression
- **Adaptive Query Execution**: Dynamic query optimization

## 📁 Project Structure

```
areeba_project/
├── areeba_project.ipynb          # Main Jupyter notebook
├── main.py                       # Entry point for standalone execution
├── requirements.txt              # Python dependencies
├── generate_documentation.py     # Documentation generator
├── test_countries.py            # Country data validation
├── GlobalLandTemperaturesByCity.csv  # Primary dataset
├── output_folder/               # Processed Parquet files
├── artifacts/                   # Spark temporary files
├── spark-warehouse/            # Spark metadata
└── Documentation/              # Generated documentation
    ├── User_Documentation.docx
    ├── User_Documentation.pdf
    ├── Developer_Documentation.docx
    └── Developer_Documentation.pdf
```

## 🚀 Quick Start

### Prerequisites
- Python 3.12 or higher
- 8GB RAM minimum (16GB recommended)
- Apache Spark (included in requirements)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd areeba_project
   ```

2. **Create virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Launch the dashboard**
   ```bash
   # Open the Jupyter notebook
   jupyter notebook areeba_project.ipynb
   
   # Or run the Python script
   python main.py
   ```

### Using the Jupyter Notebook

1. **Run setup cells (1-9)** to initialize Spark and load data
2. **Execute the dashboard creation cell** to build the interface
3. **Launch the dashboard** using the provided launch function

```python
# In the notebook
launch_dashboard(share=True, port=7860)
```

## 📖 Documentation

Comprehensive documentation is available in multiple formats:

### 📚 User Documentation
- **Purpose**: End-user guides, tutorials, and FAQs
- **Contents**: Getting started, feature explanations, troubleshooting
- **Formats**: 
  - `User_Documentation.docx` (Microsoft Word)
  - `User_Documentation.pdf` (PDF)

### 🔧 Developer Documentation
- **Purpose**: Technical architecture, API references, development guides
- **Contents**: System design, data workflows, ML models, deployment
- **Formats**:
  - `Developer_Documentation.docx` (Microsoft Word)
  - `Developer_Documentation.pdf` (PDF)

### 📄 Generate Documentation
```bash
python generate_documentation.py
```

## 🔍 Usage Examples

### Country Analysis
```python
# Analyze Pakistan's climate patterns
dashboard.get_country_analysis("Pakistan", "Monthly Patterns", (2000, 2013))
```

### Temperature Predictions
```python
# Predict temperature for next 10 years using Random Forest
predictions = evaluator.predict_temperature("Pakistan", 10, "Random Forest")
```

### Global Comparisons
```python
# Compare average temperatures across countries
dashboard.get_global_comparison(["Pakistan", "India", "China"], "Average Temperature")
```

## ⚡ Performance Features

### Spark Optimizations
- **Adaptive Query Execution (AQE)**: Dynamic query optimization
- **Intelligent Caching**: DataFrame caching for repeated operations
- **Partition Optimization**: Optimal data partitioning by year
- **Memory Management**: Efficient memory usage and garbage collection

### Data Processing
- **Lazy Evaluation**: Efficient computation graph execution
- **Predicate Pushdown**: Early filtering for better performance
- **Column Pruning**: Minimize data transfer
- **Compression**: Snappy compression for Parquet files

## 🧪 Testing

### Run Tests
```bash
# Test country data availability
python test_countries.py

# Run unit tests (if available)
python -m pytest tests/
```

### Performance Testing
```python
# Check system health
check_spark_health()

# View performance metrics
quick_stats()
```

## 📊 Dataset Information

- **Source**: Global Land Temperatures by City
- **Time Period**: 1750 - 2013
- **Countries**: 200+ countries worldwide
- **Records**: ~8.6 million temperature measurements
- **Format**: CSV (original), Parquet (processed)
- **Size**: ~500MB (compressed)

## 🔧 Configuration

### Spark Configuration
```python
spark.conf.set("spark.sql.adaptive.enabled", "true")
spark.conf.set("spark.sql.adaptive.coalescePartitions.enabled", "true")
spark.conf.set("spark.serializer", "org.apache.spark.serializer.KryoSerializer")
```

### Dashboard Configuration
```python
# Launch options
launch_dashboard(
    share=False,    # Set to True for public sharing
    port=7860,      # Custom port
    server_name="0.0.0.0"  # Allow external connections
)
```

## 🤝 Contributing

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/amazing-feature`)
3. **Commit your changes** (`git commit -m 'Add amazing feature'`)
4. **Push to the branch** (`git push origin feature/amazing-feature`)
5. **Open a Pull Request**

### Development Guidelines
- Follow PEP 8 style guidelines
- Add docstrings for all functions
- Include unit tests for new features
- Update documentation as needed

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Apache Spark**: For powerful distributed computing capabilities
- **Gradio Team**: For the excellent web interface framework
- **Climate Data Contributors**: For providing comprehensive temperature datasets
- **Open Source Community**: For the amazing tools and libraries

## 📞 Support

- **Documentation**: Check the comprehensive user and developer guides
- **Issues**: Report bugs and feature requests in the GitHub issues
- **Community**: Join discussions and share experiences

## 🔄 Version History

### Version 1.0.0 (Current)
- ✅ Initial release with core functionality
- ✅ Country analysis and global comparisons
- ✅ AI temperature predictions (demo mode)
- ✅ Interactive Gradio dashboard
- ✅ Comprehensive documentation

### Future Enhancements
- 🔮 Real-time data streaming
- 🤖 Advanced ML models (LSTM, Prophet)
- 🌐 API endpoints
- 📱 Mobile-responsive design
- 🗺️ Geospatial visualizations

---

<div align="center">
  <strong>Built with ❤️ for climate research and data science</strong>
  <br>
  <sub>Powered by Apache Spark • Python • Gradio • Machine Learning</sub>
</div>
