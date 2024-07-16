AWS Infrastructure Automation with Terraform and Ansible
Overview
This project sets up a basic web application infrastructure on AWS using Terraform and configures the web server using Ansible. The infrastructure includes a VPC, subnets, an Internet Gateway, a Load Balancer, an EC2 instance running Nginx, and an RDS instance running MySQL.

Part 1: Infrastructure Automation with Terraform
Infrastructure Components
VPC
Subnets
Public Subnets across two availability zones
Private Subnets across two availability zones
Internet Gateway
Route Tables
Public Route Table associated with Public Subnets
Security Groups
Web Security Group for EC2 instance
DB Security Group for RDS instance
EC2 Instance
Runs Nginx web server
RDS Instance
Runs MySQL database
Load Balancer
Public-facing Load Balancer
Target Group and Listener
Registers the EC2 instance to the Load Balancer
Setup Instructions
1. Clone the Repository.
   https://github.com/mohsinrao51/Ansiterra.git

2. Initialize Terraform
     => terraforn init
3. Plan Terraform Configuration
    => terraform plan
4. Apply Terraform Configuration
    => terrafrom apply

5. Access the Web Application
After the infrastructure is created, access the web application using the DNS name of the Load Balancer.
Assumptions
The AWS region is set to us-west-2.
An Ubuntu AMI ID (ami-0ee3d9a8776e8b99c) is used for the EC2 instance. Replace this with a valid Ubuntu AMI ID for your region if necessary.
The RDS instance uses the default MySQL 5.7 parameter group.
Security groups are configured to allow HTTP (port 80), HTTPS (port 443), and MySQL (port 3306) traffic as required.
Security Considerations
Ensure the security group rules are correctly set to allow necessary traffic and restrict access where appropriate.
Use strong passwords for the RDS instance.
Part 2: Web Server Configuration with Ansible
Ansible Playbook: setup-nginx.yml

Setup Instructions
1. Ensure Ansible is Installed
Make sure Ansible is installed on your local machine. You can install Ansible using pip:
=> pip install ansible
2. Run the Ansible Playbook
Update your Ansible inventory file (hosts) to include the EC2 instance: hosts.ini

**[web]
16.170.219.181 ansible_user=ubuntu ansible_ssh_private_key_file=/home/worker/Downloads/basemachine.pem**

Run the playbook:

=> ansible-playbook -i hosts setup-nginx.yml

Access the Web Server
After running the playbook, you can access the web server using the EC2 instance's public IP or the Load Balancer's DNS name.
Conclusion
This README provides an overview of setting up a basic web application infrastructure on AWS using Terraform and configuring the web server using Ansible. Follow the provided instructions to deploy and configure the infrastructure and web server.




-------------------------------------------------------------------------------------------------------------------------------------------------------------------Part 2:
Application Components
app.py: Contains the Flask application with endpoints to add and retrieve visitors.
db.py: Contains functions to establish a database connection and create the visitors table.
test.py: Contains unit tests for the Flask application.
Setup Instructions
Prerequisites
Python 3.x
pip (Python package installer)
MySQL database running on AWS RDS
1. Clone the Repository
https://github.com/mohsinrao51/Ansiterra.git

2. Create a Virtual Environment

=> python3 -m venv venv
=> source venv/bin/activate

3. Install Dependencies

4. Run the Applicatio

=> python app.py

The application will be accessible at http://0.0.0.0:5000.

API Endpoints
Add a Visitor
URL: /visitors
Method: POST
Request Payload: {"name": "Visitor Name"}
Response: {"message": "Visitor added"}
Get Visitors
URL: /visitors
Method: GET
Response: [{id: 1, name: "Visitor Name", visit_time: "2024-07-16T00:00:00"}]
Running the Tests

1. Install Testing Dependencies
Make sure pytest is installed:

=> pip install pytest

2. Run the Tests

=> pytest test.py


The tests will check the following:

Adding a visitor.
Retrieving the list of visitors.
Handling the case when no name is provided in the POST request.



