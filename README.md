# Devrel: Infusing Conversational AI in Your Business with Amazon Lex 

## Pre-requisites
- Python 3.12
- Terraform 1.11.x or later
- AWS Account with IAM permissions to create resources

Create virtual environment:

```bash
python3 -m venv .venv
```

Activate virtual environment:

```bash
source .venv/bin/activate
```

## Makefile commands

### Local development

Install dependencies:

```bash
make install
```

Launch all tests:

```bash
make test
```

### Setup Infrastructure with Terraform

Terraform Init:

```bash
make terraform-init
```

Terraform Plan:

```bash
make terraform-plan
```

Terraform Apply:

```bash
make terraform-apply
```

Terraform Destroy:

```bash
make terraform-apply
```

Load fixtures:

```bash
make fixtures:
```