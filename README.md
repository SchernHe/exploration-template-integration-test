# Integration Test Instance
<p><small>Project based on <a target="_blank" href="https://resources.gitpages.aai.sh/mlops/exploration-template/docs/latest">Explora - The Machine Learning Exploration Template</a></small></p>

<!-- vscode-markdown-toc -->
* 1. [Developer Instructions](#DeveloperInstructions)
* 2. [Initial Setup](#InitialSetup)
* 3. [Development](#Development)
	* 3.1. [Activate environment](#Activateenvironment)
	* 3.2. [Pre-Commit](#Pre-Commit)
	* 3.3. [Execute Tests](#ExecuteTests)
* 4. [Update Documentation](#UpdateDocumentation)

<!-- vscode-markdown-toc-config
	numbering=true
	autoSave=true
	/vscode-markdown-toc-config -->
<!-- /vscode-markdown-toc -->

##  1. <a name='DeveloperInstructions'></a>Developer Instructions

- In case of problems, questions or feature requests, please reach out via Slack: [#AI-Alchemist](https://appliedaide.slack.com/archives/C0636ERJQ1W)
- For more information on how to use the template, see the [documentation](https://resources.gitpages.aai.sh/mlops/exploration-template/docs/latest).


##  2. <a name='InitialSetup'></a>Initial Setup

Congratulation, you just created your project using the explora template. Before you start, please
take a look at the following small steps for the initial setup.



**Initial Repository Setup:**
```console
# Install Repository
poetry install

# Initial commit and connect to the remote GitLab / GitHub repository
git add .
git remote add origin <REMOTE-URL>
git commit -m "Instantiated Explora Template"
git push -u origin main
```

**Activate GitHub Pages:**
The first documentation will be already created once you pushed the initial commit 'Instantiated Explora Template'
to the `main` branch. However, you still need to activate GitHub pages in the settings.

To do so, set the `Branch` in the pages settings to `gh-pages` and click on save:
`Settings > Pages > 'Branch' > 'gh-pages'`





Feel free to remove this chapter once you finalized the initial setup.

##  3. <a name='Development'></a>Development

The following code snippets are only important for developers **not** using the devcontainer.

###  3.1. <a name='Activateenvironment'></a>Activate environment

You can either activate the virtuale environment created by poetry ...

```console
poetry shell
```

or execute each command using `poetry run` as a prefix.

###  3.2. <a name='Pre-Commit'></a>Pre-Commit

```console
pre-commit install
```

###  3.3. <a name='ExecuteTests'></a>Execute Tests

```console
poetry run python3 -m pytest tests/
```
##  4. <a name='UpdateDocumentation'></a>Update Documentation

- The documentation will be updated automatically by GitHub Actions whenver a pull-requests gets merged
- The documentation version will be according to the current project version as defined in the [pyproject.toml](./pyproject.toml)


