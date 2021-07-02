import os

def ec2_va():
    os.system("terraform init")
    os.system("terraform apply -auto-approve")