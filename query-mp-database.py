from argparse import ArgumentParser
from querier import Querier

"""
This program queries the Materials Project database with specified
materials using user's API key.
"""

__author__ = "Erpan Arkin"
__email__ = "erpan14ar@gmail.com"


description = 'Materials Project Querying Tool'

parser = ArgumentParser(description=description)
parser.add_argument('API_KEY', metavar='API_KEY', type=str,
                    help="User's API Key to connect to the MP")
parser.add_argument('MATERIAL', metavar='MATERIAL', type=str,
                    help='Chemical formula of the target material, e.g. Fe2O3')
parser.add_argument('-p', action='store_true',
                    help="plot all entries' id verse energy per atom")

args = parser.parse_args()

my_query = Querier(args.API_KEY, args.MATERIAL)
my_query.GS_finder()
my_query.print_results()
if args.p:
    my_query.plot()
