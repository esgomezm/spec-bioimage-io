from dataclasses import dataclass
from typing import List, Union

from marshmallow import missing
from marshmallow.utils import _Missing

from bioimageio.spec.shared.raw_nodes import Dependencies, RawNode, ResourceDescription, URI
from . import base_nodes

# reassign to use imported classes
Dependencies = Dependencies


@dataclass
class CiteEntry(RawNode, base_nodes.CiteEntry):
    pass


@dataclass
class Author(RawNode, base_nodes.Author):
    pass


@dataclass
class Badge(RawNode, base_nodes.Badge):
    pass


# to pass mypy:
# separate dataclass and abstract class as a workaround for abstract dataclasses
# from https://github.com/python/mypy/issues/5374#issuecomment-650656381
@dataclass(init=False)  # to allow for additional unknown kwargs
class _RDF(ResourceDescription, base_nodes._RDF):
    covers: Union[_Missing, List[URI]] = missing


@dataclass(init=False)
class RDF(_RDF, base_nodes.RDF):
    pass


@dataclass
class CollectionEntry(RawNode, base_nodes.CollectionEntry):
    source: URI = missing


@dataclass
class ModelCollectionEntry(CollectionEntry, base_nodes.ModelCollectionEntry):
    download_url: URI = missing


@dataclass
class Collection(RDF, base_nodes.Collection):
    pass
