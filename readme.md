
# Code Quality Check Tool

This project provides a Python interface to check code quality, including software supply chain security, by analyzing a `requirements.txt` file. It leverages OpenAI's capabilities to perform detailed quality checks on dependencies, including prompt-based quality issue fixing.

## Table of Contents
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)

## Requirements

- Python 3.8+
- OpenAI API key
- `requirements.txt` file with dependency information in the format `package_name==version`

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/sjmsjmdsg/CodeQualityAgent.git
    cd code-quality-check-tool
    ```

2. Install necessary packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Ensure you have an OpenAI API key. 

## Usage

The program reads dependencies from a `requirements.txt` file, checks their code quality, and outputs a report as a JSON file.

1. **Prepare Your Requirements File**: Prepare a `requirements.txt` file with the necessary dependencies.
   
2. **Run the Program**: Use `check_code_quality()` in `main.py` as the enter API to execute the code quality check.
   
   Example:
   ```python
   def example():
       with open(f'{root}/../ini_file/OpenAI/openaikey.txt', 'r') as file_r:
           # prepare input path
           key = file_r.readline()
           requirement_file = f'{root}/data_process/input/requirement.txt'
           verbose = False

           # check requirement.txt
           check_code_quality(requirement_path=requirement_file, openai_key=key, verbose=verbose,
                              output_path=f'{root}/data_process/output/result.json')
   ```

3. **View the Results**: The JSON output file `result.json` will contain the quality analysis results. 

### Parameters

- `openai_key`: The OpenAI API key for accessing the service.
- `requirement_path`: Path to the `requirements.txt` file.
- `output_path`: Path to save the resulting JSON report.
- `verbose`: Optional boolean. If set to `True`, prints intermediate details.
