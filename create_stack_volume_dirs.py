import os
import yaml
import sys

def create_directories_from_volumes(yaml_file):
    try:
        # Read the YAML file
        with open(yaml_file, 'r') as file:
            data = yaml.safe_load(file)

        # Extract volumes
        volumes = data.get('volumes', {})

        if not volumes:
            print("No volumes found in the YAML file.")
            return

        # Create directories for each volume
        for volume in volumes:
            if not os.path.exists(volume):
                os.makedirs(volume)
                print(f"Directory created: {volume}")
            else:
                print(f"Directory already exists: {volume}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <path_to_yaml_file>")
        sys.exit(1)

    yaml_file_path = sys.argv[1]
    create_directories_from_volumes(yaml_file_path)
