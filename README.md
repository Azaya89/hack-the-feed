# Hack The Feed Project

This repository serves as the home for the Hack The Feed project, a data analysis endeavor undertaken for the `Hack the feed` hackathon. Our goal in this project was to analyze and derive insights from data sourced from the hackathon page [here](https://portfolio.diceytech.co.uk/project-opportunity/1692893137471x831086163701530600). Below, you will find details on the project's structure, how to set it up locally, its usage, and licensing information.

A comprehensive report on the analyses can be found in the `docs/` directory named as [report.md](docs/report.md).

## Table of contents

- [Project structure](#project-structure)
- [Setup](#setup)
- [Usage](#usage)
- [License](#license)
- [Contributing](#Contributing)
- [Activating pre-commit hooks](#activating-pre-commit-hooks)
- [Reporting issues](#reporting-issues)

## Project structure

This repository is organized as follows:

```
HACK_THE_FEED/

    - data/
        - facebook.csv
        - instagram.csv
        - linkedin.csv
        - twitter.csv
    - docs/
        - [plot images]
        - report.md
    - notebooks/
        - init.py
        - facebook.ipynb
        - instagram.ipynb
        - linkedin.ipynb
        - twitter.ipynb
    - src/
        - init.py
        - clean_data.py
    - .gitignore
    - .pre-commmit-config.yaml
    - environment.yml
    - LICENSE
    - README.md
```

## Setup
To reproduce the notebooks on your local computer, follow these steps:

1. Clone this repository to your local computer using either the `https` or `SSH` link:

        git clone git@github.com:Azaya89/hack-the-feed.git

2. Navigate to the project's top directory on your computer using the terminal or command prompt.

3. Create a Conda environment using the `environment.yml` file provided in the repository:

         `conda env create -n <env_name> -f environment.yml`

    Replace `<env_name>` with the name you prefer for your environment. For example, you can name it `htf` as used in the `environment.yml` file.

    This command installs all the necessary dependencies required to get the repository to work exactly how it was used.

4. Activate the enviroment:

        conda activate htf

    Make sure to replace `htf` with the name you used in step 3.
## Usage

Navigate to the `notebooks` directory and run each notebook sequentially from the top down. Each notebook is self-contained and reproduces the analysis for the respective dataset.

## License
This repository is distributed under the terms of the [GPL-3.0 license](LICENSE) included in this repository.

## Contributing

We welcome contributions from the community to help improve the Hack The Feed project. If you'd like to contribute, follow these steps:

1. Fork this repository to your own GitHub account.
2. Clone the forked repository to your local machine.
3. Follow the [setup](#setup) instructions in the table of content.
4. Activate [pre-commit hooks](#activating-pre-commit-hooks)
5. Create a new branch for your contribution:

        git checkout -b your-feature

6. Make your changes or additions to the project.
7. Commit your changes and provide clear and concise commit messages.
8. Push your changes to your forked repository.
9. Create a pull request (PR) from your branch to the main repository.
10. We'll review your PR, provide feedback, and work together to merge it into the main project.

## Activating Pre-Commit Hooks

Before submitting your code changes, we recommend activating the pre-commit hooks to ensure code quality and consistency. To do this, follow these steps:

1. Install `pre-commit` if you haven't already:

        pip install pre-commit

2. Navigate to the project's root directory on your local machine.

3. Run the following command to set up the pre-commit hooks:

        pre-commit install  


    This command configures the pre-commit hooks in the `.pre-commit-config.yaml` file to run automatically before each commit.

By following these steps, you can ensure that your contributions adhere to our coding standards and best practices.

## Reporting Issues

If you encounter a bug,  or have a suggestion, please feel free to [open an issue](https://github.com/Azaya89/hack-the-feed/issues) in this repository. We value your feedback and will address the issue promptly.
