#!/usr/bin/env python3
"""Exercise 2: Combine device and lab environment data into YAML."""

import json

import yaml

try:
    with open("devices.yaml") as devices_file:
        devices = yaml.safe_load(devices_file)

    with open("lab_envs.json") as lab_envs_file:
        lab_envs = json.load(lab_envs_file)

    for device in devices.values():
        lab_env_name = device.get("lab_env")

        if lab_env_name is None:
            device["lab_env"] = None
        else:
            device["lab_env"] = lab_envs.get(lab_env_name)

    with open("combined_devices.yaml", "w") as output_file:
        yaml.safe_dump(devices, output_file, sort_keys=False)

except FileNotFoundError as error:
    print(f"File not found: {error}")

except (json.JSONDecodeError, yaml.YAMLError) as error:
    print(f"Failed to parse file: {error}")
