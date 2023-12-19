import base64
import subprocess
from typing import List
import yaml
from kube import get_kubeconfig, get_clientset
from whanos import WhanosResources, WhanosDeployment, WhanosConfig, parse_config

from kubernetes import client, config, watch
from kubernetes.client.rest import ApiException
from kubernetes.client import V1Container, V1ContainerPort, V1Deployment, V1PodTemplateSpec, V1LabelSelector, V1ObjectMeta, V1PodSpec

from flask import Flask, request, jsonify

app = Flask(__name__)

class CreateDeploymentDto:
    def __init__(self, image, config, name):
        self.image = image
        self.config = config
        self.name = name

class ServerConfig:
    def __init__(self, replicas=None, resources=None, ports=None):
        self.replicas = replicas
        self.resources = resources
        self.ports = ports

# def parse_config(config_str):
#     try:
#         cfg = yaml.safe_load(config_str)
#         return ServerConfig(**cfg.get("deployment", {}))
#     except Exception as e:
#         raise RuntimeError(f"Error parsing configuration: {str(e)}")

def main():
    kubeconfig_path = get_kubeconfig()
    clientset = get_clientset(kubeconfig_path)
    deployments_client = clientset.apps_v1.Deployment(api_version="apps/v1", kind="Deployment")

    @app.route('/deployments', methods=['POST'])
    def create_deployment():
        try:
            payload = request.get_json()
            deployment_dto = CreateDeploymentDto(**payload)

            config_str = base64.b64decode(deployment_dto.config).decode('utf-8')
            server_config = parse_config(config_str)

            ports = [V1ContainerPort(container_port=port) for port in server_config.ports]

            print("Starting to pull image", deployment_dto.image)
            subprocess.run(["minikube", "cache", "add", deployment_dto.image], check=True)
            print("Finished pulling", deployment_dto.image)

            deployment = V1Deployment(
                metadata=V1ObjectMeta(name=deployment_dto.name),
                spec=V1PodSpec(
                    replicas=server_config.replicas,
                    selector=V1LabelSelector(match_labels={"app": deployment_dto.name}),
                    template=V1PodTemplateSpec(
                        metadata=V1ObjectMeta(labels={"app": deployment_dto.name}),
                        spec=V1PodSpec(
                            containers=[
                                V1Container(
                                    name=deployment_dto.name,
                                    image=deployment_dto.image,
                                    ports=ports,
                                    resources=server_config.resources,
                                    image_pull_policy="IfNotPresent"
                                )
                            ]
                        )
                    )
                )
            )

            result = deployments_client.create_namespaced_deployment(
                body=deployment, namespace="default"
            )
            print(f"Created deployment {result.metadata.name}.")

            return jsonify({"status": "success"}), 200

        except ApiException as e:
            return jsonify({"error": "Kubernetes API error", "description": str(e)}), 500
        except Exception as e:
            return jsonify({"error": "Internal server error", "description": str(e)}), 500

    app.run(port=3030)

if __name__ == "__main__":
    main()
