# 1. Installation Of Extensions And Python

- Install Python
    - Select all options, most importantly **Add python.exe to PATH**
- Install Python extension by Microsoft
- Install Jupyter extension by Microsoft
- Install Jupyter packages in cmd: `pip install jupyter ipykernel notebook`
- Choose kernel/env when creating a notebook:
    - Either: Use global Python (default)
    - Or: Create an isolated venv first (recommended for seperate projects)
        - venv = A folder with its own Python installation and packages 

# 2. Installation Of Libraries

Run in cmd `pip install -r requirments.txt`

The requirments.txt file includes all the necessary libraries used in the project along side it's specific version. It's syntax is ``` Libarary_name == version_number```



# 3. Import Needed Libraries After Installing them


```python
import numpy as np

print(np.array([1, 2, 3]))

```

    [1 2 3]



```python

```
