from setuptools import setup, find_packages

setup(
    name="vendas-cli",
    version="1.0.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    entry_points={
        "console_scripts": [
            "vendas-cli=vendas_cli.cli:main",
        ],
    },
    install_requires=[],
    python_requires=">=3.8",
)
