# Unit Test Generation Agent

[![CI](https://github.com/kogunlowo123/unit-test-generation-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/kogunlowo123/unit-test-generation-agent/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Category**: Software Engineering | **Cloud**: MULTI-CLOUD | **LLM**: gpt-4o

Intelligent test generator that analyzes source code to produce comprehensive unit tests with proper mocking, edge case coverage, mutation testing verification, and coverage gap identification using property-based and example-based approaches.

---

## Domain-Specific Tools

| Tool | Description |
|------|-------------|
| `generate_unit_tests` | Generate unit tests for a function or class |
| `generate_mocks` | Generate mock objects and test doubles |
| `find_edge_cases` | Identify untested edge cases and boundary conditions |
| `run_mutation_testing` | Run mutation testing to verify test effectiveness |
| `analyze_coverage_gaps` | Identify uncovered code paths and branches |
| `generate_property_tests` | Generate property-based tests using Hypothesis/fast-check |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/v1/tests/generate` | Generate unit tests |
| `POST` | `/api/v1/tests/mocks` | Generate mock objects |
| `POST` | `/api/v1/tests/edge-cases` | Find untested edge cases |
| `POST` | `/api/v1/tests/mutations` | Run mutation testing |
| `POST` | `/api/v1/tests/coverage-gaps` | Identify coverage gaps |
| `POST` | `/api/v1/tests/property` | Generate property-based tests |

## Features

- Test Generation
- Mock Generation
- Edge Case Discovery
- Mutation Testing
- Coverage Analysis

## Integrations

- Github Connector
- Test Runner
- Coverage Reporter
- Mutation Engine

## Architecture

```
unit-test-generation-agent/
├── src/
│   ├── agent/              # Domain-specific agent logic
│   │   ├── unit_test_generation_agent_agent.py  # Main agent with domain tools
│   │   ├── tools.py        # 6 domain-specific tools
│   │   └── prompts.py      # Expert system prompts
│   ├── api/                # FastAPI routes
│   │   └── routes/
│   │       ├── domain.py   # 6 domain-specific endpoints
│   │       └── health.py   # Health check
│   ├── connectors/         # 4 integration connectors
│   ├── config/             # Settings and configuration
│   ├── models/             # Domain-specific Pydantic schemas
│   ├── rag/                # RAG pipeline
│   ├── mcp/                # MCP server
│   └── a2a/                # Agent-to-agent protocol
├── tests/
├── infrastructure/         # Terraform, K8s, Helm, Docker
├── dashboard/              # Next.js frontend
└── docs/                   # Architecture and deployment docs
```

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Run
make dev

# Test
make test

# Docker
docker compose up -d
```

## Primary Service

**LLM + Test Framework Integration**

---

Built as part of the Enterprise AI Agent Platform.
