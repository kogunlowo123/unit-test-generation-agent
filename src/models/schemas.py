"""Unit Test Generation Agent - Domain-Specific Schemas."""

from datetime import datetime
from uuid import UUID, uuid4
from typing import Any, Optional
from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    """Chat request."""
    message: str
    conversation_id: UUID | None = None
    stream: bool = False
    context: dict[str, Any] | None = None


class ChatResponse(BaseModel):
    """Chat response."""
    message: str
    conversation_id: UUID
    message_id: UUID
    sources: list[dict[str, Any]] = []
    tool_results: list[dict[str, Any]] = []
    model: str
    latency_ms: float
    timestamp: datetime


class StreamChunk(BaseModel):
    """Streaming response chunk."""
    chunk: str
    conversation_id: UUID
    done: bool = False


class HealthResponse(BaseModel):
    """Health check response."""
    status: str
    version: str
    uptime_seconds: float
    agent: str
    features: list[str]


class TestGenerationRequest(BaseModel):
    """TestGenerationRequest for Unit Test Generation Agent."""
    source_code: str
    language: str
    test_framework: str = 'pytest'
    coverage_target: float = 0.8


class GeneratedTestSuite(BaseModel):
    """GeneratedTestSuite for Unit Test Generation Agent."""
    test_code: str
    test_count: int
    edge_cases_covered: list[str]
    mock_dependencies: list[str]


class MutationReport(BaseModel):
    """MutationReport for Unit Test Generation Agent."""
    total_mutants: int
    killed: int
    survived: int
    mutation_score: float
    surviving_mutants: list[dict]

