"""Parsing and processing script arguments from CLI."""

import argparse
import os


parser = argparse.ArgumentParser(prog='page_loader',
                                 description='Downloads a web page')
parser.add_argument('-o', '--output',
                    default=os.getcwd(),
                    help='Path to output directory (Default: current directory)'
                    )
parser.add_argument('url',  # Web page url
                    help='URL of the web page you want to download'
                    )

args = parser.parse_args()
