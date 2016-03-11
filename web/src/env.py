import os

def getenv(key):
    if key == "CLUSTER_NAME":
        return os.environ.get("CLUSTER_NAME", "docklet-vc")
    elif key == "FS_PREFIX":
        return os.environ.get("FS_PREFIX", "/opt/docklet")
    elif key == "CLUSTER_SIZE":
        return os.environ.get("CLUSTER_SIZE", 1)
    elif key == "CLUSTER_NET":
        return os.environ.get("CLUSTER_NET", "172.16.0.1/16")
    elif key == "CONTAINER_CPU":
        return os.environ.get("CONTAINER_CPU", 100000)
    elif key == "CONTAINER_DISK":
        return os.environ.get("CONTAINER_DISK", 1000)
    elif key == "CONTAINER_MEMORY":
        return os.environ.get("CONTAINER_MEMORY", 1000)
    elif key == "DISKPOOL_SIZE":
        return os.environ.get("DISKPOOL_SIZE", 5000)
    elif key == "ETCD":
        return os.environ.get("ETCD", "localhost:2379")
    elif key == "NETWORK_DEVICE":
        return os.environ.get("NETWORK_DEVICE", "eth0")
    elif key == "MASTER_IP":
        return os.environ.get("MASTER_IP", "0.0.0.0")
    elif key == "MASTER_PORT":
        return os.environ.get("MASTER_PORT", 9000)
    elif key == "WORKER_PORT":
        return os.environ.get("WORKER_PORT", 9001)
    elif key == "PROXY_PORT":
        return os.environ.get("PROXY_PORT", 8000)
    elif key == "PROXY_API_PORT":
        return os.environ.get("PROXY_API_PORT", 8001)
    elif key == "WEB_PORT":
        return os.environ.get("WEB_PORT", 8888)
    elif key == "PORTAL_URL":
        return os.environ.get("PORTAL_URL",
            "http://"+getenv("MASTER_IP") + ":" + str(getenv("PROXY_PORT")))
    elif key == "LOG_LEVEL":
        return os.environ.get("LOG_LEVEL", "DEBUG")
    elif key == "LOG_LIFE":
        return os.environ.get("LOG_LIFE", 10)
    elif key == "STORAGE":
        return os.environ.get("STORAGE", "file")
    else:
        return os.environ[key]
