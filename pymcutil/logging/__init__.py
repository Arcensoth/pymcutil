import logging.config

DEFAULT_LEVEL = logging.WARNING
DEFAULT_FMT = '%(asctime)s | %(levelname)-8s | %(message)s'


def install(level=DEFAULT_LEVEL, fmt=DEFAULT_FMT):
    logging.basicConfig(level=level, format=fmt)

    try:
        import sys
        import colorlog

        formatter = colorlog.ColoredFormatter(
            fmt='%(log_color)s' + fmt + '%(reset)s',
            log_colors={
                'DEBUG': 'blue',
                'INFO': 'green',
                'WARNING': 'yellow',
                'ERROR': 'red',
                'CRITICAL': 'white,bg_red',
            }
        )

        handler = colorlog.StreamHandler(sys.stdout)
        handler.setFormatter(formatter)

        logging.root.handlers.clear()
        logging.root.addHandler(handler)

    except:
        pass
