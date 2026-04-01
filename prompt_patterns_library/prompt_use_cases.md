# Prompt Use Cases

## Code Quality
- **Refactoring**
  - **Goal**: Improve readability and performance  
  - **Input**: Source function in [LANGUAGE]  
  - **Output**: Optimized code + explanation  

- **Style Enforcement**
  - **Goal**: Enforce consistent naming and formatting  
  - **Input**: Code block  
  - **Output**: Rewritten code with consistent style  

## Debugging
- **Error Explanation**
  - **Goal**: Understand cryptic error messages
  - **Input**: Error snippet or compiler output
  - **Output**: Plain English explanation of the error and potential causes

- **Bug Fixing**
  - **Goal**: Resolve logical or syntax errors in code
  - **Input**: Problematic code snippet and the observed incorrect behavior
  - **Output**: Corrected code with an explanation of what was fixed

- **Stack Trace Analysis**
  - **Goal**: Pinpoint the origin of an exception in a deep stack trace
  - **Input**: Full stack trace and the corresponding log entries
  - **Output**: Identification of the exact file and line causing the issue, with a suggested fix

## Documentation
- **Inline Commenting**
  - **Goal**: Add descriptive comments to complex logic
  - **Input**: Undocumented complex function
  - **Output**: Function with standard inline comments explaining the logic step-by-step

- **README Generation**
  - **Goal**: Create comprehensive project setup and usage documentation
  - **Input**: Project structure summary and list of key features
  - **Output**: Well-structured `README.md` file contents

- **API Documentation**
  - **Goal**: Generate precise documentation for API endpoints
  - **Input**: API route definitions and expected payload structures
  - **Output**: Documentation detailing endpoints, methods, inputs, and expected responses

## Testing
- **Unit Test Generation**
  - **Goal**: Automatically create unit tests for a given piece of code
  - **Input**: Target function and its expected behavior
  - **Output**: A suite of unit tests covering main execution paths in [FRAMEWORK]

- **Edge Case Identification**
  - **Goal**: Find unusual scenarios that could break the application
  - **Input**: Function description and constraints
  - **Output**: A list of edge cases and corresponding test scenarios
