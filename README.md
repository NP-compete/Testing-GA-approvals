# Deployment Process

## Team Agreements

- Release Cycle: Bimonthly
- Branching Strategy: Git Flow
- Product Teams
  - FrontEnd
  - BackEnd
  - Mobile

## Environments

| Environment | Usage                                                                                                                            | Branches        | Deployment                   | Notes                                                                     |
|-------------|----------------------------------------------------------------------------------------------------------------------------------|-----------------|------------------------------|---------------------------------------------------------------------------|
| Dev         | <ul><li>Unit Testing</li><li>Component Testing</li><li>Smoke Testing</li><li>Sanity Testing</li><li>Regression Testing</li></ul> | feature/develop |  | Might be down,<br>Stakeholders: developers                                |
| Stage        | <ul><li>Integration Testing</li><li>API testing</li><li>UI testing</li><li>System testing</li></ul>                              | develop         | manually trigger approval    | Might be down, but calculate downtime<br>Stakeholders: SRE and developers |
| Release     | <ul><li>Integration Testing</li><li>API testing</li><li>UI testing</li><li>System testing</li></ul>                              | hotfix/release  | on commit to hotfix/release (post code-freeze)          | Raise "Critical" ticket if down;<br>Stakeholders: SRE and developers      |
| QA          | <ul><li>QA Testing</ul>                                                                                                          | release         | manually trigger approval (post code-freeze)   | Raise "Critical" ticket if down;<br>Stakeholders: SRE, QA and developers  |
| Pre-Prod        | Pre-Production                                                                                                         | master/tag      | manually                     | Raise "Critical" ticket if down;<br>Stakeholders: SRE, QA and developers  |
| Prod        | Production Environment                                                                                                           | master/tag      | manually                     | Raise "Critical" ticket if down;<br>Stakeholders: SRE, QA and developers  |

## CI/CD

### Tools

- Github Actions
- AWS CodePipeline
- AWS CodeBuild
- AWS CodeDeploy

### Steps

- Deployment to `dev` will be on commit to `feature/develop` branch.
- When all testing is complete in dev, developers can trigger a manual approval process to deploy their code to test.
- Once the code is approved, it will be deployed to `test` environment.
- Once the code is tested in `test` environment, it will be deployed to `Release` environment for internal stakeholder demo.
- Once the code is approved in `Release`, it will be deployed to `Pre-Prod` environment.
- If there is a bug in Pre-prod, the intended hotfix branch would be tested in the `Release` environment and merged back to `develop` and `release` branches.
- Once again QA tests the updated code and if it is successful, we get a DAG of IPC dependencies and deploy the code to `prod`.


## Terraform

Amazon Elastic Compute Cloud	
AWS Marketplace	
AWS Data Transfer	
Amazon Simple Storage Service	
Amazon Relational Database Service	
Amazon Elastic File System	
Amazon OpenSearch Service	
Amazon ElastiCache	
Amazon Managed Streaming for Apache Kafka	
AWS Elemental MediaConvert	
Amazon CloudFront	
AWS Support (Developer)	
AmazonCloudWatch	
Elastic Load Balancing	
AWS Support (Business)	
AWS Lambda	
Amazon Simple Email Service	
Amazon WorkSpaces	
Amazon Virtual Private Cloud	
Amazon DynamoDB
Amazon Simple Queue Service	
Amazon Registrar	
Amazon API Gateway	
CodeBuild	
AWS Elemental MediaLive	
Amazon Route 53	
Amazon EC2 Container Registry (ECR)	
AWS WAF	
AWS Key Management Service