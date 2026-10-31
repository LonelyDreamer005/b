terraform {
  required_providers {
    local = {
      source  = "hashicorp/local"
      version = "~> 2.5"
    }
  }
}

provider "local" {}

resource "local_file" "example" {
  filename = "hello.txt"
  content  = "Hello! Terraform is working successfully."
}