.PHONY: clean lint create_environment bind_kernel 

#################################################################################
# GLOBALS                                                                       #
#################################################################################

PROJECT_NAME := $(shell pwd | rev | cut -f1 -d'/' - | rev)
PYTHON_INTERPRETER = "python3"

#################################################################################
# COMMANDS                                                                      #
#################################################################################

## Delete all compiled Python files
clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete

## Lint using flake8
lint:
	flake8 src

## Set up python virtual environment
create_environment:
	@echo ">>> Install Pipenv if not already installed"
	pipenv install --dev --skip-lock
	@echo ">>> Installing project dependencies"
	@echo ">>> New pipenv env create. Activate with: pipenv shell"

## Bind ipython kernel to env: only run after "pipenv shell"
bind_kernel:
	ipython kernel install --user --name=$(PROJECT_NAME)
	@echo ">>> Installing ipython kernel and associating with pipenv for jupyterlab"

test_print:
	echo $(PROJECT_NAME)
