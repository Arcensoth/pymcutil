import abc

from pymcutil.data_tag import DataTag
from pymcutil.resource.abc.resource import Resource


class NBTResource(Resource):
    def write_to(self, path):
        with open(path, 'wb') as fp:
            fp.write(self.nbt.to_bytes())

    @property
    @abc.abstractmethod
    def nbt(self) -> DataTag:
        """ Return the root tag of the NBT representation of the object. """
