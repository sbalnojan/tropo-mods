PROJECT_NAME := "tropo-mods"

# .PHONY: example_simple_ec2
#
example_simple_ec2: ## Print the ec2_basic.py example to CF template file
	python3 examples/ec2_basic.py > examples/simple_ec2.yml

dep:
	pip install -r requirements.txt

help: ## Display this help screen
	@grep -h -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
