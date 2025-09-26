AfterQuery Bash/Linux Assessment – Software Engineer

This repository contains my solution submission for the AfterQuery Software Engineer – Bash/Linux Expert assessment.

Overview

This assessment tests the ability to create high-quality, self-contained Bash/Linux tasks that run in a Unix-like command-line environment. Each task includes:

Deterministic test suites

Containerized setup (Docker)

Clear documentation

The goal is to demonstrate correctness, clean execution, and understanding of terminal workflows (sysadmin, data engineering, networking, devops).

Task Structure
tasks/<task-id>/
├── Dockerfile          # Base image & environment setup
├── task.yaml           # Task description, metadata
├── solution.sh         # Reference solution (Bash)
├── run-tests.sh        # Test runner script
└── tests/
    └── test_outputs.py # Validation tests

Key Files

solution.sh: Contains the complete solution.

task.yaml: Defines instructions, difficulty, author email, tags, and timeouts.

tests/test_outputs.py: Validates the solution via automated test cases.

run-tests.sh: Installs test dependencies and executes tests inside the container.

Local Setup

Clone the Terminal-Bench repo:

git clone https://github.com/laude-institute/terminal-bench.git
cd terminal-bench


Install Terminal-Bench dependencies:

uv tool install terminal-bench
uv sync


Recommended environment:

Docker engine + CLI

Python 3.12 (some dependencies fail with 3.13)

Virtual environment (venv/conda/pyenv)

Running & Testing

Test with Oracle agent (should pass 100%):

uv run tb run --agent oracle --task-id <task-id>


Test with Null agent (should fail 0%):

uv run tb run --agent nop --task-id <task-id>


Interactive debugging:

uv run tb tasks interact -t <task-id>

Docker & Compose

Tasks use single-container Dockerfile or multi-service docker-compose.yaml.

Base image example for Ubuntu/Debian:

FROM ubuntu:22.04
RUN apt-get update && apt-get install -y bash coreutils findutils
WORKDIR /workspace


Ensure deterministic builds, pin package versions.

Use environment variables for paths inside the container:

T_BENCH_TEST_DIR – test directory

T_BENCH_TASK_DOCKER_CLIENT_IMAGE_NAME – container name

Assessment Submission

Zip the task folder:

cd tasks/<task-id>
zip -r firstname-lastname-date.zip .


Upload to the AfterQuery portal:
Submit Assessment

Filename rules: lowercase only, hyphens, no underscores.

Wait for “Tests Passed” and “Review Ready” confirmation.

Notes & Best Practices

Keep tasks deterministic and self-contained.

All instructions and file paths must work inside Docker containers.

Avoid Python version mismatches (3.12 recommended).

Non-ASCII characters may break zips – use GUI zipping if needed.

For API-based tasks, bind services to 0.0.0.0 and use container names in tests instead of localhost.

References

Terminal Bench documentation: https://www.tbench.ai/docs

Example tasks: https://github.com/laude-institute/terminal-bench/tree/main/tasks
