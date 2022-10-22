# {{ cookiecutter.project_name }}

---

---

## Very first steps (DELETE THIS AFTER COMPLETING!)

### Initialize your code

1. Initialize `git` inside your repo:

```bash
cd {{ cookiecutter.project_name }} && git init
```

2. If you don't have `Poetry` installed run:

```bash
make poetry-download
```

3. Initialize poetry and install `pre-commit` hooks:

```bash
make install
make pre-commit-install
```

4. Run the codestyle:

```bash
make codestyle
```

5. Upload initial code to GitHub:

```bash
git add .
git commit -m ":tada: Initial commit"
git branch -M main
git remote add origin https://github.com/{{ cookiecutter.github_name }}/{{ cookiecutter.project_name }}.git
git push -u origin main
```

Read more on the DEV_README.md file.

---

---

<div align="center">

[![Build status](https://github.com/{{ cookiecutter.github_name }}/{{ cookiecutter.project_name }}/workflows/build/badge.svg?branch=master&event=push)](https://github.com/{{ cookiecutter.github_name }}/{{ cookiecutter.project_name }}/actions?query=workflow%3Abuild)
[![Python Version](https://img.shields.io/pypi/pyversions/{{ cookiecutter.project_name }}.svg)](https://pypi.org/project/{{ cookiecutter.project_name }}/)
[![Dependencies Status](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)](https://github.com/{{ cookiecutter.github_name }}/{{ cookiecutter.project_name }}/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot)

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Security: bandit](https://img.shields.io/badge/security-bandit-green.svg)](https://github.com/PyCQA/bandit)
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/{{ cookiecutter.github_name }}/{{ cookiecutter.project_name }}/blob/master/.pre-commit-config.yaml)
[![Semantic Versions](https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--versions-e10079.svg)](https://github.com/{{ cookiecutter.github_name }}/{{ cookiecutter.project_name }}/releases)
[![License](https://img.shields.io/github/license/{{ cookiecutter.github_name }}/{{ cookiecutter.project_name }})](https://github.com/{{ cookiecutter.github_name }}/{{ cookiecutter.project_name }}/blob/master/LICENSE)
![Coverage Report](assets/images/coverage.svg)

{{ cookiecutter.project_description }}

</div>

---

## Features

## Installation

```bash
pip install -U {{ cookiecutter.project_name }}
```

or install with `Poetry`

```bash
poetry add {{ cookiecutter.project_name }}
```

{% if cookiecutter.create_example_template == 'cli' -%}Then you can run

```bash
{{ cookiecutter.project_name }} --help
```

or with `Poetry`:

```bash
poetry run {{ cookiecutter.project_name }} --help
```

{%- endif %}

## 📈 Releases

You can see the list of available releases on the [GitHub Releases](https://github.com/{{ cookiecutter.github_name }}/{{ cookiecutter.project_name }}/releases) page.

## 🛡 License

[![License](https://img.shields.io/github/license/{{ cookiecutter.github_name }}/{{ cookiecutter.project_name }})](https://github.com/{{ cookiecutter.github_name }}/{{ cookiecutter.project_name }}/blob/master/LICENSE)

This project is licensed under the terms of the `{{ cookiecutter.license }}` license. See [LICENSE](https://github.com/{{ cookiecutter.github_name }}/{{ cookiecutter.project_name }}/blob/master/LICENSE) for more details.
