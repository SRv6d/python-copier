# Python Copier Template

[![GitHub](https://img.shields.io/github/v/tag/srv6d/python-copier?logo=github&sort=semver)](https://github.com/srv6d/python-copier)

An opinionated [copier] template for robust Python code that aims to reduce the overhead
of managing different linters, typecheckers and workflows for mulitple repositories.

## Feature Summary

- [ruff] linting, code & import formatting
- [mypy] type checking
- [PDM] packaging and dependency management
- [Nox] linting, testing and maintenance task automation

## Usage

After installing [copier], run the following and answer the questions.

```shell
copier copy gh:srv6d/python-copier /path/to/new/projet
```

[copier]: https://github.com/copier-org/copier/
[ruff]: https://github.com/astral-sh/ruff
[mypy]: https://github.com/python/mypy
[pdm]: https://github.com/pdm-project/pdm
[nox]: https://github.com/wntrblm/nox
