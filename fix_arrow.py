"""
Workaround for PyArrow extension type registration issues.
Import this before using pandas with parquet files.
"""
import pyarrow as pa

# Clear any existing pandas extension types to avoid conflicts
_types_to_unregister = [
    "pandas.period",
    "pandas.interval",
    "pandas.categorical",
]

for type_name in _types_to_unregister:
    try:
        pa.unregister_extension_type(type_name)
    except pa.ArrowKeyError:
        pass  # Type not registered, that's fine
