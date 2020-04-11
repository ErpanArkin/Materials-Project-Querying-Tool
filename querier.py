"""
This class can be used to queries the Materials Project database with specified
material MATER using user's API key API_KEY, and print or plot the results.
packages used: pymatgen, pandas, tabulate, matplotlib, seaborn
"""

__author__ = "Erpan Arkin"
__email__ = "erpan14ar@gmail.com"


class Querier:

    def __init__(self, API_KEY, MATERIAL):
        from pymatgen.ext.matproj import MPRester
        import pandas as pd

        self.API_KEY = API_KEY
        self.MATERIAL = MATERIAL

        with MPRester(self.API_KEY) as m:
            self.mp_all = m.query(criteria={"pretty_formula": self.MATERIAL},
                                  properties=["material_id", "energy_per_atom"])
        if len(self.mp_all) < 1:  # if no entry matched
            raise ValueError('Could not find any entry related to {}!'.format(self.MATERIAL))
        else:
            self.data = pd.DataFrame(self.mp_all)

    def GS_finder(self):
        # get the index of ground state energy
        GS_IX = self.data['energy_per_atom'].idxmin(axis=1)
        # get the ground state energy
        self.GS_E = self.data['energy_per_atom'].iloc[GS_IX]
        # get the id of ground state material
        self.GS_ID = self.data['material_id'].iloc[GS_IX]

        # set material_id as index
        self.data.set_index('material_id', inplace=True)
        # sort by energy
        self.data.sort_values('energy_per_atom', inplace=True, ascending=False)

    def print_results(self):
        # print results as a formatted table
        from tabulate import tabulate
        print(tabulate(self.data, headers='keys', tablefmt='psql'))
        # print summary
        print('{} entries found for query: {}'.format(len(self.data), self.MATERIAL))
        print("Most stable material: {0} ({1:.6f} eV/atom)".format(self.GS_ID, self.GS_E))

    def plot(self):
        import matplotlib.pylab as plt
        import seaborn as sns
        sns.barplot(self.data.index, 'energy_per_atom', data=self.data)
        plt.title('All entries for {}'.format(self.MATERIAL))
        plt.xticks(rotation=60)
        plt.tight_layout()
        plt.show()
