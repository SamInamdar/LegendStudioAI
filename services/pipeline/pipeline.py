"""
Pipeline.
"""

from typing import Any

from services.pipeline.pipeline_context import PipelineContext
from services.pipeline.pipeline_step import PipelineStep


class Pipeline:
    """Executes pipeline steps sequentially."""

    def __init__(self) -> None:
        self.steps: list[PipelineStep] = []

    def add_step(self, step: PipelineStep) -> "Pipeline":
        """Add a step to the pipeline."""

        self.steps.append(step)

        return self

    def execute(self, context: PipelineContext) -> PipelineContext:
        """Execute all pipeline steps."""

        for step in self.steps:
            result = step.execute(context)

            if result is not None:
                context = result

        return context