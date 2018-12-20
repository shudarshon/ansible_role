variable "aws_region" {}
variable "aws_profile" {}
variable "instance_type" {}
variable "instance_name" {}
variable "ami_id" {}
variable "ssh_user_name" {}
variable "ssh_key_name" {}
variable "ssh_key_path" {}
variable "security_groups" {
  type = "list"
}
variable "subnet_ids" {
  type = "list"
}
variable "instance_count" {}
variable "dev_host_label" {}
