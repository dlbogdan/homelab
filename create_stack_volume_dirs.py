import os
import yaml
import sys

# Configuration for the device prefix
DEVICE_PREFIX = "/mnt/cephfs/volumes"

def create_directories_and_modify_yaml(yaml_file):
    try:
        # Read the YAML file
        with open(yaml_file, 'r') as file:
            data = yaml.safe_load(file)

        # Extract and process volumes
        volumes = data.get('volumes', {})
        if not volumes:
            print("Error: No volumes found in the YAML file.", file=sys.stderr)
            sys.exit(1)

        for volume_name in volumes.keys():
            # Ensure directory exists
            volume_path = os.path.join(DEVICE_PREFIX, volume_name)
            os.makedirs(volume_path, exist_ok=True)

            # Update the volume definition
            volumes[volume_name] = {
                "driver": "local",
                "driver_opts": {
                    "type": "none",
                    "device": volume_path,
                    "o": "bind"
                }
            }

        # Output the modified YAML to stdout
        print(yaml.dump(data, default_flow_style=False))

    except FileNotFoundError:
        print(f"Error: File not found: {yaml_file}", file=sys.stderr)
        sys.exit(1)
    except yaml.YAMLError as e:
        print(f"Error: Failed to parse YAML: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <path_to_yaml_file>", file=sys.stderr)
        sys.exit(1)

    yaml_file_path = sys.argv[1]
    create_directories_and_modify_yaml(yaml_file_path)
