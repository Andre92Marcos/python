1st) Download and Install Anaconda

2nd) Go to anaconda\Scripts folder and create a conda env

	conda create --name test_env python=3

3rd) Activate the env

	activate test_env

4th) Install jupyter for you conda env

	conda install jupyter

5th) Create ipykernel server for your conda env

	python -m ipykernel install --user --name test_env --display-name “Python (test_env)

6th) Start jupyter notebook

	jupyter notebook

7th) Create a new notebook with your env
