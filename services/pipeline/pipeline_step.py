"""
Pipeline Step.
"""

from abc import ABC, abstractmethod
from typing import Any


class PipelineStep(ABC):
    """Base class for all pipeline steps."""

    @abstractmethod
    def execute(self, context: Any) -> Any:
        """Execute the pipeline step."""
        raise NotImplementedError