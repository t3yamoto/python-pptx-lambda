# python-pptx-lambda

A sample project that runs [python-pptx](https://python-pptx.readthedocs.io/en/latest/index.html) on AWS Lambda.

## Prerequisites

- Python 3.8+
- Pipenv
- Node.js 14+
- Docker
- AWS Profile

## Deployment

```sh
npm install
pipenv install
npx sls deploy
```

## Invoke function

```sh
# Invoke function that create pptx from scratch.
# see [Getting Started — python-pptx 0.6.19 documentation](https://python-pptx.readthedocs.io/en/latest/user/quickstart.html#hello-world-example)
npx sls invoke --function Scratch
```

You can download the pptx file from the output URL.
