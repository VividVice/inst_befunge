from kubernetes import client, config
import os

def get_kubeconfig():
    home = os.path.expanduser("~")
    return os.path.join(home, ".kube", "config")

def get_clientset(kubeconfig):
    try:
        config.load_kube_config(config_file=kubeconfig)
    except Exception as e:
        raise RuntimeError(f"Error loading kubeconfig: {str(e)}")

    return client.CoreV1Api()

# Example usage:
# kubeconfig_path = get_kubeconfig()
# clientset = get_clientset(kubeconfig_path)
