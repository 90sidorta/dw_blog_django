{
    "editor.formatOnSave": true,
    "python.formatting.provider": "black",
    "python.formatting.blackArgs": [
        "--line-length",
        "100"
    ],
    "python.linting.enabled": true,
    "python.linting.lintOnSave": true,
    "python.linting.flake8Enabled": true,
    "python.linting.flake8Args": [
        "--max-line-length=100"
    ],
    "[python]": {
        "editor.codeActionsOnSave": {
            "source.organizeImports": true,
        }
    }
}