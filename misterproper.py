import os

path = "datasets"


for item in [item for item in os.listdir(path) if item.startswith("tmp")]:
    os.remove(os.path.join(path, item))
