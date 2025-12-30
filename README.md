# Combined-Spectral-Analysis-Method

Instructions (linux) (Python3):

1. Simulation (MCNP 6.2)

Note: post simulation data is in DetectorReadings.csv, this step is to generate these, if only interested in analysis, skip to step 2.

- go to Simulation/
- while in Simulation/ run bash gen/setup_workspace.sh
- in gen/scriptgen run all cells in generateSimulations.ipynb
- in gen/command edit command_template.sh
- in gen/command run python3 command_gen.py
- go to Simulation/compute
- run bash batch.sh
- go to Simulation/gen/
- run python3 mctallies.py

2. Analysis

- go to Analysis/
- run all cells in analysismultivar.ipynb
- 