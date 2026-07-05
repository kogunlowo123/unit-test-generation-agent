# Unit Test Generation Agent Architecture

Intelligent test generator that analyzes source code to produce comprehensive unit tests with proper mocking, edge case coverage, mutation testing verification, and coverage gap identification using property-based and example-based approaches.

## Domain Tools

- **generate_unit_tests**: Generate unit tests for a function or class
- **generate_mocks**: Generate mock objects and test doubles
- **find_edge_cases**: Identify untested edge cases and boundary conditions
- **run_mutation_testing**: Run mutation testing to verify test effectiveness
- **analyze_coverage_gaps**: Identify uncovered code paths and branches
- **generate_property_tests**: Generate property-based tests using Hypothesis/fast-check