# Tutorial: D-Wave SA, QPU and Hybrid
=========================================

This small tutorial covers a usage of D-Wave Systems hardware
for sampling protein design problem represented as QUBO.
Problem represented as a triangular matrix of 1-body and 2-bodies
energies.

To open this project in D-Wave Leap IDE use this link:

    https://ide.dwavesys.io/#https://github.com/vsergeyev/simanneal

Entry point is `app.py`.

Energies representation
-----------------------

Upper triangular matrix for aminoacids should be prepared before
running D-Wave samplers.

In example below we have protein with 3 aminoacids in chain,
and for each position we have available rotamers:
 * 3 rotamers - for aminoacid at position 1
 * 4 rotamers - for aminoacid at position 2
 * 3 rotamers - for aminoacid at position 3

Here is and example NumPy matrix:

        [        pos 0        ][             pos 1            ][         pos 2        ]
    mat = np.array(
       [[1.0,   50000,  50000,  1121.0, 1122.0, 1123.0, 1124.0, 1131.0, 1132.0, 1133.0],
        [0,     2.0,    50000,  1221.0, 1222.0, 1223.0, 1224.0, 1231.0, 1232.0, 1233.0],
        [0,     0,      3.0,    1321.0, 1322.0, 1323.0, 1324.0, 1331.0, 1332.0, 1333.0],
        [0,     0,      0,      4.0,    50000,  50000,  50000,  2131.0, 2132.0, 2133.0],
        [0,     0,      0,      0,      5.0,    50000,  50000,  2231.0, 2232.0, 2233.0],
        [0,     0,      0,      0,      0,      6.0,    50000,  2331.0, 2332.0, 2333.0],
        [0,     0,      0,      0,      0,      0,      7.0,    2431.0, 2432.0, 2433.0],
        [0,     0,      0,      0,      0,      0,      0,      8.0,    50000,  50000 ],
        [0,     0,      0,      0,      0,      0,      0,      0,      9.0,    50000 ],
        [0,     0,      0,      0,      0,      0,      0,      0,      0,      10.0  ]]
    )

Main diagonal in this representation stores 1-body energies, e.g. particular rotamer self-energy.
Other cells are represent the energy between a pair, 2-bodies energies.
E.g., rotamer 1 at position 1 and rotamer 3 at position 2, for example.
Note: in computers indexing starts with "0". So for example above we may say `(0, 0) <-> (1, 2)` energy,
where notation equals to `(position, rotamer)`.


Useful links
------------

D-Wave Leap login & signup: https://cloud.dwavesys.com/leap/

Documentation for QPU / Hybrid samplers:
https://docs.ocean.dwavesys.com/projects/system/en/stable/reference/samplers.html#dwave.system.samplers.LeapHybridDQMSampler
