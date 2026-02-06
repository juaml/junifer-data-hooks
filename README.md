# junifer-data-hooks

Git pre-commit hooks for `junifer-data`, to be used with either `pre-commit` or `prek`.

## Usage

`.pre-commit-config.yml`

```yml
repos:
  - repo: https://github.com/juaml/junifer-data-hooks
    rev: e53cfed516b4b1dc81b24bfb5fd90768714cd389
    hooks:
      - id: check-julich-brain-versions
```

With `pre-commit`

```console
pre-commit run --all-files
```

With `prek` (recommended)

```console
prek run --all-files
```

In case of failure, try installing `uv` and running again.

## Available hooks

`check-julich-brain-versions`

Checks for new versions of Julich-Brain via `siibra`.
