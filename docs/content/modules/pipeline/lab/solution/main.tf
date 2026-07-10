# Arquivo: main.tf
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = "us-east-1"
}

# Um recurso de rede simples apenas para teste
resource "aws_vpc" "rede_principal" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_hostnames = true

  tags = {
    Name        = "VPC-Desafio-Pipeline"
    Environment = "Desenvolvimento"
  }
}
