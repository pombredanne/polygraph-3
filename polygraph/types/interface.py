from polygraph.exceptions import PolygraphSchemaError
from polygraph.types.basic_type import PolygraphOutputType, PolygraphType
from polygraph.types.field import Field


class Interface(PolygraphOutputType, PolygraphType):
    """
    GraphQL Interfaces represent a list of named fields and their
    arguments. GraphQL objects can then implement an interface, which
    guarantees that they will contain the specified fields.
    """
    pass


def validate_interface_schema(interface_class):
    attributes = (getattr(interface_class, attr) for attr in dir(interface_class))
    fields = [attr for attr in attributes if isinstance(attr, Field)]

    if len(fields) < 1:
        raise PolygraphSchemaError("Interfaces require at least one field")

    names = [field.name for field in fields]
    if len(set(names)) != len(names):
        raise PolygraphSchemaError("Interface field names should all be unique")

    if any(name.startswith("__") for name in names):
        raise PolygraphSchemaError("Interface field names cannot start with '__'")
