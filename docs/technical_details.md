# Technical Details

## Toolstack

- VSCode Devcontainer
- Git LFS for networked Data storage & versioning
- Pre-commit setup
- mike-mkdocs

### CI Setup

- In your project create a cleanup policy, 7 days should be enough
    - [docs](https://gitlab.aai.sh/help/user/packages/container_registry/reduce_container_registry_storage#create-a-cleanup-policy)
- Follow step 1 & 2 from the instructions of `mike-mkdocs`: [docs](https://resources.gitpages.aai.sh/mlops/mike-mkdocs/docs/latest/#gitlab-ci)
