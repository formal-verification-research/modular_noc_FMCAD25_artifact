# Python Scripts

## [noc](noc.py)

Exposes the `Noc` class that can be used to generate arbitrary nxn NoC models in
the Modest language.

### Example

```python
from noc import *

_2x2 = Noc(2)

with open("2x2.modest", "w") as f:
    f.write(_2x2.print())
```

## [modest](modest.py)

Exposes the following methods:

### `check`

```python
def check(model: str | Path, output_path: Path | None = None) -> str
```

Runs `modest check` on the given `model` argument and returns the output of
`modest check` as a string.

Inputs:
- `model`: Either the model as a string (useful when using the NoC library) or
  the filepath to the model file (ending in .modest).
- `output_path`: the location to store the output. If not specified the output
  is only returned as a string.

Returns:
- `modest check` output as a string.

### `simulate`

```python
def simulate(model: str | Path, output_path: Path | None = None) -> str
```

Runs `modest simulate` on the given `model` argument and returns the output of
`modest check` as a string.

Inputs:
- `model`: Either the model as a string (useful when using the NoC library) or
  the filepath to the model file (ending in .modest).
- `output_path`: the location to store the output. If not specified the output
  is only returned as a string.

Returns:
- `modest check` output as a string.