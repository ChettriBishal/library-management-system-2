import logging


class Log:
    """
    Create a logger object
    """

    def __init__(self, current_file):
        self.logger = logging.getLogger(
            f'library_management_system.{current_file}')
        logging.basicConfig(
            format=
            '%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d]  %(message)s',
            datefmt='%d-%m-%Y:%H:%M:%S',
            level=logging.INFO,
            filename=f'logs.txt')
