"""Unit Test Generation Agent - Unit Tests."""

import pytest
from src.agent.tools import AgentTools


@pytest.mark.asyncio
async def test_generate_unit_tests():
    """Test Generate unit tests for a function or class."""
    tools = AgentTools()
    result = await tools.generate_unit_tests(source_code="test", language="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_generate_mocks():
    """Test Generate mock objects and test doubles."""
    tools = AgentTools()
    result = await tools.generate_mocks(interface="test", mock_framework="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_find_edge_cases():
    """Test Identify untested edge cases and boundary conditions."""
    tools = AgentTools()
    result = await tools.find_edge_cases(source_code="test", existing_tests="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_run_mutation_testing():
    """Test Run mutation testing to verify test effectiveness."""
    tools = AgentTools()
    result = await tools.run_mutation_testing(source_file="test", test_file="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that the agent initializes correctly."""
    from src.agent.unit_test_generation_agent_agent import UnitTestGenerationAgentAgent
    agent = UnitTestGenerationAgentAgent()
    assert agent.agent_id is not None
    assert agent._system_prompt is not None
    assert len(agent._tool_dispatch) > 0
