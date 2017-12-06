from pymcutil.data_tag import DataTag
from pymcutil.resource.abc.nbt_resource import NBTResource


class StructureResource(NBTResource):
    def __init__(self, nbt):
        self._nbt = nbt

    @property
    def nbt(self) -> DataTag:
        return self._nbt
