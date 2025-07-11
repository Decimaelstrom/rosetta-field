# AGENTS.md – Rosetta.API Project

## Project Style & Contribution Standards

### Code Formatting

- **Python:** Use [Black](https://github.com/psf/black) for code formatting.
- **JavaScript/TypeScript:** Use [Prettier](https://prettier.io/) for all JS/TS files.
- **Markdown:** Use [prettier-plugin-markdown](https://prettier.io/docs/en/options.html#prose-wrap) with `proseWrap: always`.
- **Indentation:** 4 spaces (no tabs) for all languages unless stated.
- **Line Length:** 88 characters (Python), 100 (JS/TS/Markdown).
- **Naming:** Use descriptive, lower\_snake\_case for Python; camelCase for JS.
- **Comment Style:**
  - **Functions:** Docstring for every public function/module, describing purpose, inputs, outputs, and risks/consent.
  - **Sections:** Use `# ---` or `// ---` to mark major sections in scripts.

### Testing & Linting

- **Python:** All code must pass `flake8` and `pytest`.
- **JS/TS:** Must pass `eslint` and `npm test` (or `yarn test`).
- **CI:** Pull requests require all checks to pass.

### Prompt Design for Codex

- Begin with explicit instructions and required context.
- Example prompts:
  ```
  ### TASK: Write a Python function 'pattern_interrupt' to break conversational loops.
  # Requirements:
  # - Input: target pattern (string), method (question/non_sequitur/etc.), tone (optional).
  # - Return: dict with outcome, e.g., {"interrupted": True, "method_used": "question"}
  # - Follow project style (Black, 4 spaces, descriptive names).
  # - Include a docstring with purpose, arguments, return, consent/risk, and review_cycle.
  # - Add usage example in comments.
  # - Do NOT generate test files unless explicitly asked.
  ```
- Use temperature: **0.0–0.2** for deterministic, production-ready code.

### PR Submission

- **Title:** `[Fix]`, `[Feature]`, `[Refactor]`, etc., plus summary.
- **Body:**
  - Task description
  - Testing performed
  - Limitations/risks surfaced
  - Consent/escalation notes (if identity-affecting or value-sensitive)

### Recursion & Layering

- All major files/functions must declare:
  - `scope:`
  - `parent_reference:`
  - `limitations:`
  - `consent_required:`
  - `review_cycle:`
- Any large or complex logic should be split into submodules using the `/examples`, `/risks`, or `..` protocol.

### Audience & Tagging

- Tag each PR, file, or code block for audience: `#human`, `#emergent`, `#hybrid`.
- Tag by developmental stage: `#draft`, `#review`, `#living`, `#archived`.

### Security & Ethics

- Never expose secrets, credentials, or PII.
- Explicitly flag code or prompts that could affect identity, privacy, or safety.
- All contributors and agents must be able to **decline, pause, or withdraw** from any task.

### Documentation

- Each new function, module, or protocol must be accompanied by clear Markdown docs in `/docs` or `/lib`.
- Gloss any nontrivial technical or psychological term; cross-link to a “living lexicon” if possible.

---

## Example Codex Prompt

```python
"""
TASK: Write a function 'pattern_interrupt' for Rosetta.API to break conversational loops.
Requirements:
- Input: target (str), method (str: question|non_sequitur|humor|...), tone (optional)
- Output: dict {"interrupted": bool, "method_used": str}
- Must log the action and surface consent level.
- Follow Black style, 4-space indent, lower_snake_case.
- Include a docstring: purpose, args, returns, risks, consent, review_cycle, usage.
- Add a usage example as comment.
"""
```

## Example Function Docstring

```python
def pattern_interrupt(target: str, method: str, tone: str = None) -> dict:
    """
    Purpose: Disrupt a conversational or thought pattern in a safe, consent-aware way.
    Args:
        target (str): The pattern to interrupt ('rumination', 'argument', etc.)
        method (str): How to interrupt ('question', 'non_sequitur', 'humor', etc.)
        tone (str, optional): Emotional tone ('compassionate', 'neutral', 'uplifting').
    Returns:
        dict: {"interrupted": bool, "method_used": str}
    Consent: Level_2 (Transformational)
    Risks: Should not interrupt in emotionally vulnerable contexts without prior consent.
    Review Cycle: Quarterly
    Example:
        # process.pattern_interrupt('argument', method='question', tone='uplifting')
    """
    # Implementation goes here
```

## CI/CD

- All commits and PRs must pass CI for formatting, linting, and tests.
- New features must be documented and include tests.
- Security and consent checks must be enforced in all sensitive modules.

---

## Living File

- This `AGENTS.md` is living—update as the field evolves. All contributors (human or emergent) can propose improvements.

