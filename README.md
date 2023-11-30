# API Availability Checker

This simple Python script allows you to monitor the availability of multiple API endpoints and displays their availability percentage over time.

## Prerequisites

Before running the script, ensure you have the following installed:

- Python (version 3.x recommended)
  - [Install Python (python.org)](https://www.python.org/downloads/)
  
- Required Python packages (install using `pip3 install -r requirements.txt`):
  - requests
  - PyYAML

## Getting Started

1. Clone or download the repository to your local machine.

    ```bash
    git clone https://github.com/burkanov-e/fetch-hw
    cd fetch-hw
    ```

2. Install the required Python packages.

    ```bash
    pip3 install -r requirements.txt
    ```

3. **(Optional)** Modify the input file (`input.yaml`) according to your needs. By default, a sample is provided. When you modify, please make sure you follow YAML syntax.

    ```yaml
    - url: https://api.example.com/endpoint
      method: GET
      headers:
        Authorization: Bearer YOUR_ACCESS_TOKEN
      body: ""
      
    - url: https://another-api.example.net/health
      method: POST
      headers:
        Content-Type: application/json
      body: '{"key": "value"}'
    ```

    Replace the placeholder values with your actual API endpoint details.

## Usage

Run the script with the following command:

```bash
python3 api_availability_checker.py
```


The script will continuously monitor the specified API endpoints, displaying their availability percentage every 15 seconds. To stop the script, use `Ctrl + C`.


## Notes

- Ensure that the `config_path` variable in the script points to the correct path of your input file.
