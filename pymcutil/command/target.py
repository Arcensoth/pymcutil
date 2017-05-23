from typing import Union

from pymcutil.command.selector.selector import Selector

# A target can be either a single name/UUID or a target selector.
Target = Union[str, Selector]
