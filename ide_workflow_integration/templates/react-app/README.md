# React Template with AI Support

## Projects
This repository contains two distinct templates:
1. React Frontend Template (this document)
2. Node Backend Template (located in the `../node-backend` directory)

## Features
- Pre-configured Copilot settings natively attached.
- ESLint + Prettier auto-formatting bounds.
- AI doc generation workflow pre-installed.

## AI Configuration Setup
A concrete configuration file for AI is presented entirely inside the companion `ai-config.json` package. It explicitly maps the following internal IDE parameters:
```json
{
  "github.copilot.enable": {"*": true, "javascriptreact": true},
  "github.copilot.advanced": {"inlineSuggestEnable": true}
}
```
