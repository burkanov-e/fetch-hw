import requests
import yaml
import time
from collections import defaultdict


def check_health(endpoint):
    try:
        response = requests.request(
            method=endpoint.get("method", "GET"),
            url=endpoint["url"],
            headers=endpoint.get("headers", {}),
            data=endpoint.get("body", ""),
            timeout=5,  # Adjust timeout as needed
        )

        print(response.ok, response.elapsed.total_seconds())

        return response.ok and response.elapsed.total_seconds() < 0.5

    except requests.RequestException:
        return False


def api_availability(config_path):
    with open(config_path, "r") as file:
        endpoints = yaml.safe_load(file)  # save input as list of dictionaries

    domain_availability = defaultdict(lambda: {"total": 0, "up": 0})

    try:
        while True:
            for endpoint in endpoints:
                result = check_health(endpoint)
                domain = endpoint["url"].split("//")[1].split("/")[0]

                domain_availability[domain]["total"] += 1
                domain_availability[domain]["up"] += result

            for domain, data in domain_availability.items():
                availability_percentage = (
                    (data["up"] / data["total"]) * 100 if data["total"] > 0 else 0
                )
                print(
                    f"{domain} has {int(availability_percentage)}% availability percentage"
                )

            time.sleep(15)

    except KeyboardInterrupt:
        print("Program exiting.")


config_path = "input.yaml"  # Replace with the actual file path
api_availability(config_path)
