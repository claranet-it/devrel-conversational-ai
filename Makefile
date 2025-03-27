.PHONY: help install test fixtures terraform-init terraform-plan terraform-apply terraform-destroy

default: help

TF_BASE_DIR = infra
LAMBDA_BASE_DIR = code/lambda_chatbot
SCRIPT_BASE_DIR = code/scripts

help: # Show help for each of the Makefile recipes.
	@grep -E '^[a-zA-Z0-9 -]+:.*#'  Makefile | sort | while read -r l; do printf "\033[1;32m$$(echo $$l | cut -f 1 -d':')\033[00m:$$(echo $$l | cut -f 2- -d'#')\n"; done

install: # Install dev dependencies
	pip install -r requirements_dev.txt

test: # Launch tests
	cd $(LAMBDA_BASE_DIR) && pytest -vv

fixtures: # Load fixtures
	cd $(SCRIPT_BASE_DIR) && python populate_warehouse.py

terraform-init: # Initialize terraform
	cd $(TF_BASE_DIR) && terraform init

terraform-plan: # Apply terraform
	cd $(TF_BASE_DIR) && terraform plan

terraform-apply: # Apply terraform
	cd $(TF_BASE_DIR) && terraform apply -auto-approve

terraform-destroy: # Destroy terraform
	cd $(TF_BASE_DIR) && terraform destroy -auto-approve