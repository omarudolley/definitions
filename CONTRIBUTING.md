# Contributing to Data Product Definitions

A big welcome and thank you for considering contributing to this project!

Reading and following these guidelines will help us make the contribution process easy
and effective for everyone involved. It also communicates that you agree to respect the
time of the developers managing and developing these open source projects. In return, we
will reciprocate that respect by addressing your issue, assessing changes, and helping
you finalize your pull requests.

## Quicklinks

- [Contributing to Data Product Definitions](#contributing-to-data-product-definitions)
  - [Quicklinks](#quicklinks)
  - [Getting Started](#getting-started)
  - [Definitions format](#definitions-format)
  - [Adding new Data Product Definition](#adding-new-data-product-definition)
    - [Raw OpenApi spec](#raw-openapi-spec)
    - [Definition as a Python file](#definition-as-a-python-file)
    - [Test version of definitions](#test-version-of-definitions)
  - [Pull Requests](#pull-requests)
  - [License](#license)

## Getting Started

New definitions should be submitted as a pull request to this repository. We try our
best to provide an automated validation of the most common mistakes in the definitions
format, but it's still better to go through the definition guidelines.

## Definitions format

The most complete set of rules with examples can be found in the
[DataProducts](./DataProducts/README.md) directory. Except of that, please make sure to
meet the following criterias:

1. Use American English for describing data
2. Each definition file must define only one POST endpoint
3. Each definition file must include a schema for a successful response
4. Each definition file must include a schema for the request body
5. Each definition file must not define any severs or security sections

## Adding new Data Product Definition

There are two ways of contribution:

### Raw OpenApi spec

For example, to add a definition for `Foo/Bar`:

- create `DataProducts/<version>/Foo/Bar.json`
- make sure you follow the data product definition
  [guidelines](./DataProducts/README.md)

### Definition as a Python file

If you're familiar with Python and [pydantic](https://github.com/samuelcolvin/pydantic)
library, you may find it easier to create the definition as a set of pydantic models.

For example, to add a definition for `Foo/Bar`:

- create `src/<version>/Foo/Bar.py`

You have 2 options to use the converter:

1. By running `pre-commit install` after cloning the repo. Then definitions will be
   converted automatically before each commit.
2. By creating a PR to the `main` branch. CI workflow will run the automation and push
   updated/generated files if needed.

### Test version of definitions

Everyone can submit to this repo whatever definitions they seem appropriate. It will
allow to create data products using these definitions in a dataspace and experiment with
the system. In order to do this:

1. Fork this repository
2. Create your definitions under `src/test/<your_github_username>/` if you're familiar
   with Python approach, or directly under `DataProducts/test/<your_github_username>` if
   you know what you're doing
3. Submit a PR and wait for CI Workflow to run and validate the changes
4. Once PR is merged, it's possible to use the definitions in the dataspace

## Pull Requests

In general, we follow the ["fork-and-pull" Git workflow](https://github.com/susam/gitpr)

1. Fork the repository to your own Github account
2. Clone the project to your machine
3. Create a branch locally with a succinct but descriptive name
4. Commit changes to the branch
5. Following any formatting and testing guidelines specific to this repo Push changes to
   your fork
6. Open a PR in our repository

## License

By contributing, you agree that your contributions will be licensed under its
[MIT License](./LICENSE).
