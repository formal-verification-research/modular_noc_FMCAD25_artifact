# Python Scripts

This directory contains two small Python libraries that we developed to facilitate
modular development of our NoC model in the Modest language. The first library,
[noc.py](noc.py), provides a simple interface for generating arbitrary nxn NoC 
models in the Modest language. The second library, [modest.py](modest.py) provides 
a basic interface to the Modest Toolset from Python. When characterizing PSN,
Modest requires that a separate property is generated for each clock cycle, so 
it's advantageous to automate that.

Additionally, this directory contains a script, [example.py](example.py), that 
provides an example of how to use each of the libraries to generate a NoC model,
characterize PSN, and ensure functional correctness.

## [noc](noc.py) Library

Exposes the `Noc` class that can be used to generate arbitrary nxn NoC models in
the Modest language.

### Example

```python
from noc import *

_2x2 = Noc(2)

with open("2x2.modest", "w") as f:
    f.write(_2x2.print())
```

## [modest](modest.py) Library

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
