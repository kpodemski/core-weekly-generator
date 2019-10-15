#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import argparse
import logging
from core_weekly import CoreWeekly


def main():
    parser = argparse.ArgumentParser(description="PrestaShop Core Weekly")
    parser.add_argument('--no-cache', action='store_const', const=True, help='Disable cache')
    parser.add_argument('--debug', action='store_const', const=True, help='Use Debug')
    parser.add_argument('--community', action='store_const', const=True, help='Print community report')
    parser.add_argument('date_range', type=str, help='Date range')

    args = parser.parse_args()
    logging.basicConfig()
    if args.debug:
        logging.getLogger().setLevel(logging.DEBUG)

    core_weekly = CoreWeekly(args)
    if args.community:
        print(core_weekly.generate_community())
    else:
        print(core_weekly.generate())


if __name__ == '__main__':
    main()
