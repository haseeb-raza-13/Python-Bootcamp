import os
from pathlib import Path

project_name="microinformatics"

list_of_files=[

    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/data_validation.py",
    f"{project_name}/components/data_transformation.py",
    f"{project_name}/components/model_trainer.py",




]
for path in list_of_files:
    filepath=Path(path)

    filedir,filename=os.path.split(path)
    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
   
