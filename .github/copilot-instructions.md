# Copilot Instructions

## Project Overview
This is a centralized repository for security guardrails, onboarding scripts, and AI policies for all team.blue brands. It serves as the source of truth for security standards and automation scripts used across the team.blue ecosystem.

## Tech Stack and Tools
- Python for automation scripts
- Markdown for documentation and policies
- Git for version control

## Purpose and Structure
- `policies/security-standards.md`: Defines security requirements for all brand repositories
- `policies/scripts/`: Contains automation scripts for brand onboarding and management

## Coding Standards
- Python scripts should follow PEP 8 style guide
- Use meaningful function and variable names
- Add docstrings to all functions explaining their purpose and parameters
- Use type hints where applicable to improve code clarity

## Security Requirements
- All brand repositories must have dependency scanning enabled
- Follow security standards defined in `policies/security-standards.md`
- Never commit secrets, API keys, or credentials to this repository
- All scripts that interact with external systems must validate inputs

## Documentation
- Keep README.md up to date with any new tools or policies
- Document all scripts with clear usage instructions
- Security standards should be written clearly and be actionable

## Best Practices
- Make minimal changes to achieve the goal
- Test scripts before committing
- Keep policies concise and focused
- Ensure all documentation is clear and accessible to all team.blue brands
