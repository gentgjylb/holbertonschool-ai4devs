# Systematic AI-Assisted Bug Hunting Methodology

This document outlines a standardized, reusable framework for integrating Artificial Intelligence into modern debugging workflows. It synthesizes practical learnings from resolving cross-language defects and establishes actionable methods to streamline debugging while ensuring high code quality.

---

## 1. Step-by-Step Process for AI-Assisted Bug Hunting

1. **Isolation & Contextualization**: Gather verbatim logs, stack traces, and isolate the exact file or function causing the issue. Strip away irrelevant project architecture to prevent the AI from overcomplicating the context.
2. **Initial AI Diagnostic Pass**: Feed the minimal, reproducible snippet to the AI. Ask for an explanation of the root cause before asking for the explicit fix. This prevents the AI from blindly rewriting code without understanding the architectural failure.
3. **Hypothesis Validation (Human-in-the-Loop)**: Critically evaluate the AI's explanation. Does it align with domain logic? AI easily identifies syntax anomalies (like `var` scoping natively in JavaScript) but relies on humans to validate business intent.
4. **Resolution Generation**: Prompt the AI for robust fixes taking into account architectural stability. 
5. **Testing & Integration**: Validate the proposed fix with isolated unit tests. Verify that no architectural regressions were introduced before committing the code.

---

## 2. AI Prompting Guide & Templates

Tailoring the prompt to the specific category of the bug yields more accurate diagnostics from the AI. 

### For Syntax / Runtime Errors
> "I am encountering a `{Error_Type}` in the following `{Language}` code. The error occurs around line `{Line_Number}`. Can you explain the structural root cause and provide a corrected version?"

### For Logical / State Bugs
> "This `{Language}` function is supposed to `{Intended_Behavior}`. However, when given the input `{Input_Example}`, it evaluates to `{Actual_Output}` instead of `{Expected_Output}`. What is causing this logical discrepancy? Please provide a semantic fix."

### For Architecture / Concept Errors
> "I am trying to accomplish `{Goal}` in `{Language}`. The following code attempts to do this, but I suspect I am using an anti-pattern. Can you point out any conceptual flaws (e.g., memory references vs value comparisons) and optimize it?"

---

## 3. Bug Prioritization Framework

| Priority | Category / Description | Real-World Example from Sprint |
| :--- | :--- | :--- |
| **P0 (Critical)** | System crashes, data corruption, runtime iterator exceptions. Needs immediate fix. | Python: `RuntimeError` due to mutating live dictionary sizes during `.items()` iteration (`bug4.py`). |
| **P1 (High)** | Core functionality broken across a broad scope, structural anti-patterns. | JavaScript: Loop state closures breaking variable binding due to `var` instead of `let` (`bug2.js`). |
| **P2 (Medium)** | Specific feature failure or evaluation inconsistencies. Workarounds might exist. | Java: Fails string evaluation because `==` measures memory reference identity rather than `.equals()` content (`bug3.java`). |
| **P3 (Low)** | Minor boundary faults or edge case anomalies. | Python: Off-by-one slicing list error returning the full array when `0` index slices are evaluated (`bug1.py`). |

---

## 4. Practical Tools and Checklists

### Bug Analysis Checklist
- [ ] Has the bug been isolated to a specific module or component?
- [ ] Is there a predictable sequence of steps to reproduce the exact issue?
- [ ] Have standard language traps been evaluated (e.g., pointers, object references, specific variable scoping)?
- [ ] Has the "intended behavior" been explicitly defined to measure the AI's output against?

### Testing Strategy Template
1. **Unit Testing**: Create targeted tests for the exact function modified. Validate standard execution and isolated edge cases (e.g., exclusively passing `0` or negative constraints).
2. **Integration Verification**: Ensure the updated component flawlessly interacts with upstream providers and semantic downstream consumers.
3. **Regression Safety**: Execute your suite to confirm the mechanical bug fix did not disturb tightly coupled global states.

---

## 5. Quality Criteria for Evaluating Fixes

Before merging an AI-proposed fix, ensure it passes these human-verified criteria:
1. **Accuracy Requirements**: Does the update resolve the problem without introducing unexpected side effects?
2. **Idiomatic Cleanliness**: Does the syntax adhere to modern project standards? (e.g., actively utilizing native array operations or optimized standard library methods).
3. **Variable Security**: Is the proposed scope correctly bound? (e.g., block-scoped `let` versus function-scoped `var`).
4. **Performance Consistency**: Did the AI introduce unoptimized recursive looping that will degrade complexity at scale?

---

## 6. Team Collaboration and Knowledge Sharing

- **Post-Mortem Logs**: Record critical debugging insights in a centralized environment (similar to the local `ai_debug_log.md` standard) so teams recognize recurring language-specific anti-patterns.
- **Shared Prompt Repositories**: Maintain an internal wiki of highly effective AI prompts customized to your team's specific stack, frameworks, and deployment idiosyncrasies.
- **Mandatory Peer Verification**: Mandate that all AI-generated code undergoes standard human peer review. The AI serves as an accelerator, but the human engineers hold absolute architectural responsibility.
