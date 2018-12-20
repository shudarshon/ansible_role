init:
	cd ./terraform && /usr/local/bin/terraform init

plan:
	cd ./terraform && /usr/local/bin/terraform plan

apply:
	cd ./terraform && /usr/local/bin/terraform apply -auto-approve

destroy:
	cd ./terraform && /usr/local/bin/terraform destroy -auto-approve

