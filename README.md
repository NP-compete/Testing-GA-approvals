# Testing-GA-approvals


## Team Agreements

- Release Cycle: Bimonthly
- Branching Strategy: Git Flow
- Product Teams
    - FrontEnd
    - BackEnd
    - Mobile



## Environments

| Environment | Usage                                                                                                                            | Branches        | Deployment                   |
|-------------|----------------------------------------------------------------------------------------------------------------------------------|-----------------|------------------------------|
| Dev         | <ul><li>Unit Testing</li><li>Component Testing</li><li>Smoke Testing</li><li>Sanity Testing</li><li>Regression Testing</li></ul> | feature/develop | on commit to feature/develop |
| Test        | <ul><li>Integration Testing</li><li>API testing</li><li>UI testing</li><li>System testing</li></ul>                              | develop         | manually trigger approval    |
| Hotfix      | <ul><li>Integration Testing</li><li>API testing</li><li>UI testing</li><li>System testing</li></ul>                              | hotfix/release  | on commit to hotfix          |
| Pre-Prod    | <ul><li>QA Testing</ul>                                                                                                          | release         | manually trigger approval    |
| Prod        | Production Environment                                                                                                           | master/tag      | manually                     |

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
- Once the code is tested in `test` environment, it will be deployed to `Pre-Prod` environment for QA Testing after an approval process.
- If there is a bug in Pre-prod, the intended hotfix branch would be tested in the `hotfix` environment and merged back to develop and release branches.
- Once again QA tests the updated code and if it is successful, we get a DAG of IPC dependencies and deploy the code to `prod`.
