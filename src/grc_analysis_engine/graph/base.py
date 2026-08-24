from __future__ import annotations

from abc import ABC, abstractmethod
from collections.abc import Iterable

from grc_analysis_engine.models.domain import GovernanceNode, GovernanceRelationship


class GovernanceGraph(ABC):
    """Provider-neutral graph contract consumed by Analysis Engine modules."""

    @abstractmethod
    def nodes(self) -> Iterable[GovernanceNode]: ...

    @abstractmethod
    def relationships(self) -> Iterable[GovernanceRelationship]: ...

    @abstractmethod
    def node_count(self) -> int: ...

    @abstractmethod
    def relationship_count(self) -> int: ...

    @abstractmethod
    def copy_without_relationship(self, relationship_id: str) -> "GovernanceGraph": ...

    @abstractmethod
    def copy_without_node(self, node_id: str) -> "GovernanceGraph": ...

    @abstractmethod
    def has_directed_path(self, source: str, target: str) -> bool: ...
