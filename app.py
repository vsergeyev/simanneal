# D-Wave Leap access: https://cloud.dwavesys.com/leap/
# 
# Docs for QPU / Hybrid samplers
# https://docs.ocean.dwavesys.com/projects/system/en/stable/reference/samplers.html#dwave.system.samplers.LeapHybridDQMSampler

import numpy as np

import dimod
from hybrid.reference.kerberos import KerberosSampler
from dwave.system import LeapHybridSampler
from dwave.system import DWaveSampler


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

#   [          pos 0          ][              pos 1                ][         pos 2        ]
#   (0, 0) <-> (1, 3) <-> (2, 1)
mat2 = np.array(
    [[-100.0,   50000,  50000,  -1121.0,    1122.0, 1123.0, -1124.0, 1131.0, 1132.0, -1133.0],
    [0,         200.0,  50000,  1221.0,     1222.0, 1223.0, 1224.0, 1231.0,  1232.0, -1233.0],
    [0,         0,      -300.0, -1321.0,    1322.0, -1323.0, 1324.0, 1331.0, 1332.0, 1333.0],
    [0,         0,      0,      400.0,      50000,  50000,  50000,  -2131.0, 2132.0, -2133.0],
    [0,         0,      0,      0,          -500.0, 50000,  50000,  2231.0,  -2232.0, 2233.0],
    [0,         0,      0,      0,          0,      600.0,  50000,  -2331.0, 2332.0, -2333.0],
    [0,         0,      0,      0,          0,      0,      -700.0, 2431.0,  -2432.0, 2433.0],
    [0,         0,      0,      0,          0,      0,      0,      800.0,   50000,   50000 ],
    [0,         0,      0,      0,          0,      0,      0,      0,       -900.0,  50000 ],
    [0,         0,      0,      0,          0,      0,      0,      0,       0,       10.0  ]]
)

variable_order = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 1), (2, 2)]

bqm = dimod.BinaryQuadraticModel.from_numpy_matrix(mat, variable_order)
# print(bqm)
solution = KerberosSampler().sample(bqm, max_iter=10, convergence=3)   
print("Energy for all positive:", solution.first.energy)

bqm2 = dimod.BinaryQuadraticModel.from_numpy_matrix(mat2, variable_order)
solution2 = KerberosSampler().sample(bqm2, max_iter=10, convergence=3)   
print("Energy for mixed:", solution2.first.energy)
print("Solution:", solution2.first)

hybrid = LeapHybridSampler().sample(bqm2)
print("[HYBRID] Energy for mixed:", hybrid.first.energy)
print("[HYBRID] Solution:", hybrid.first)

dwave = DWaveSampler().sample(bqm2)
print("[DWAVE] Energy for mixed:", dwave.first.energy)
print("[DWAVE] Solution:", dwave.first)

# > Energy for all positive: 0.0
# > Energy for mixed: -4124.0
# > Solution: Sample(sample={(0, 0): 1, (0, 1): 0, (0, 2): 0, (1, 0): 0, (1, 1): 0, (1, 2): 0, (1, 3): 1, (2, 0): 0, (2, 1): 1, (2, 2): 0}, energy=-4124.0, num_occurrences=1)
# > [HYBRID] Energy for mixed: -4124.0
# > [HYBRID] Solution: Sample(sample={(0, 0): 1, (0, 1): 0, (0, 2): 0, (1, 0): 0, (1, 1): 0, (1, 2): 0, (1, 3): 1, (2, 0): 0, (2, 1): 1, (2, 2): 0}, energy=-4124.0, num_occurrences=1)
# Traceback (most recent call last):
#   File "/workspace/simanneal/app.py", line 53, in <module>
#     dwave = DWaveSampler().sample(bqm2)
#   File "/usr/local/lib/python3.7/site-packages/dwave/system/samplers/dwave_sampler.py", line 46, in wrapper
#     return f(sampler, *args, **kwargs)
#   File "/usr/local/lib/python3.7/site-packages/dwave/system/samplers/dwave_sampler.py", line 342, in sample
#     raise BinaryQuadraticModelStructureError(msg)
# dimod.exceptions.BinaryQuadraticModelStructureError: Problem graph incompatible with solver.
