# Technical Details

### Toolstack

- VSCode Devcontainer
- Git LFS for networked Data storage & versioning
- Pre-commit setup

### CI Setup

- In your project create a cleanup policy, 7 days should be enough
    - [docs](https://gitlab.aai.sh/help/user/packages/container_registry/reduce_container_registry_storage#create-a-cleanup-policy)
- Create an project access token and add the token to the GitLab CI variables
    - [docs](https://resources.gitpages.aai.sh/mlops/exploration-template/docs/latest/tutorials/first-steps/#configuring-ci-pipeline-to-execute-and-deploy-notebooks)

### Documentation

- Created with [mkdocs](https://github.com/mkdocs/mkdocs) and [mike](https://github.com/jimporter/mike).
- Uses [mkdocs-nav-weight](https://github.com/shu307/mkdocs-nav-weight) to order the documentation
