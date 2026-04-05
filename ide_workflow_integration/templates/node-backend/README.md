# Backend Express Template with AI Support

## Projects
This repository contains two distinct templates:
1. React Frontend Template (located in the `../react-app` directory)
2. Node Backend Template (this document)

## Features
- Pre-configured Copilot structural settings natively installed.
- Backend API parameter formatting limits.
- AI Code Review automation workflow strictly integrated.

## AI Configuration Setup
A concrete configuration file for AI is presented inside the companion `ai-config.json` file. It targets strict Express payload exclusion bounds protecting runtime loops:
```json
{
  "github.copilot.enable": {"*": true, "javascript": true},
  "files.exclude": {"node_modules/": true, "logs/": true}
}
```
