PROJECT_NAME := "tropo-mods"

example_simple_ec2: ## Print the ec2_basic.py example to CF template file
	python3 examples/ec2_basic.py > examples/cf_ec2_basic.yml

example_ec2_sg: ## Print the ec2_sg.py example to CF template file
	    python3 examples/ec2_sg.py > examples/cf_ec2_sg.yml

dep: ## Install the dependencies
	pip install -r requirements.txt

help: ## Display this help screen
	@grep -h -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
