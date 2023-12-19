import yaml
from typing import List, Optional

class WhanosResources:
    def __init__(self, limits=None, requests=None):
        self.limits = limits
        self.requests = requests

class WhanosDeployment:
    def __init__(self, replicas=None, resources=None, ports=None):
        self.replicas = replicas
        self.resources = resources
        self.ports = ports

class WhanosConfig:
    def __init__(self, deployment=None):
        self.deployment = deployment

def parse_config(config):
    try:
        cfg = yaml.safe_load(config)
        return WhanosConfig(**cfg)
    except Exception as e:
        raise RuntimeError(f"Error parsing configuration: {str(e)}")

# Example usage:
# config_str = """
# deployment:
#   replicas: 3
#   resources:
#     limits:
#       memory: "512Mi"
#       cpu: "500m"
#     requests:
#       memory: "256Mi"
#       cpu: "250m"
#   ports:
#     - 8080
#     - 9090
# """

# whanos_config = parse_config(config_str)
# print(whanos_config.deployment.replicas)  # Output: 3
