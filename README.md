# API Comparison Utility

This project provides a Python utility for comparing API responses and includes BDD Cucumber-based tests to ensure its functionality.


### Description

The API Comparison Utility allows you to compare two sets of API responses (HTTP/HTTPS) provided in two input files. The utility reads API request URLs from File 1 and File 2, makes HTTP requests to these URLs, compares the responses, and prints the results. It is capable of comparing millions of API requests without memory issues and gracefully handles exceptions.

### Usage

1. Make sure you have Python installed on your system.

2. Install the required Python libraries by running:


   ```bash
   pip install -r requirements.txt
   ```

### Run API Comparison Utility

 ```bash
   python test.py
   ```
This script will able to run the API Comparison Utility standalone

*Note: Before running the `test.py` make sure you have **`file1.txt`** and **`file2.txt`** in your codebase.*

### Run Test cases

```bash
    behave
   ```

This `behave` command will be execute the steps file.