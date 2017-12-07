from pymcutil.util.common_mapping import CommonMapping


class ArgumentMapping(CommonMapping):
    def __str__(self):
        return ''.join(('{', self.innards, '}'))

    @staticmethod
    def _convert(value):
        if isinstance(value, bool):
            return 'true' if value else 'false'
        return str(value)

    @property
    def innards(self):
        return ','.join(['{}={}'.format(k, self._convert(v)) for k, v in self.items()])
