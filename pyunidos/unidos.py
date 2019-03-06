import sys
import serial
import logging
import argparse

logger = logging.getLogger(__name__)


class Unidos(object):
    """
    """

    # telegrams
    _tg_read = b'U'
    _tg_voltage = b'V'
    _tg_status = b'S'
    _tg_range = b'R'
    _tg_range_low = b'RL'
    _tg_range_med = b'RM'
    _tg_range_high = b'RH'
    _tg_ptw = b'PTW'  # for getting firmware version etc.

    def __init__(self):
        """
        """
        self.firmware_version = ""
        self.tty = ""

    def open(self, tty="/dev/ttyS0", speed=9600, timeout=1, config="8N1"):
        """
        Establish contact to device.
        """
        self.device = serial.Serial(tty, speed, timeout)

        # test the device
        self.firmware_version()

    def firmware_version(self):
        """
        Get firmware version.
        """

        self.device.write(self._tg_ptw)
        ans = self.device.readline()
        print(ans)

    def close(self):
        """
        """
        self.device.close()


def main(args=sys.argv[1:]):
    """
    """
    # parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbosity", action='count', help="increase output verbosity", default=0)
    parsed_args = parser.parse_args(args)

    if parsed_args.verbosity == 1:
        logging.basicConfig(level=logging.INFO)
    elif parsed_args.verbosity > 1:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig()

    md = Unidos()
    md.open()
    md.close()

    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
