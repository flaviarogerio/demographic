ABC pipeline -- models with assymetrical recombination
======================================================

This document lists the scripts and results in this directory and the
order in which they should considered. More details are available as
comments within each of the scripts.

| file   | summary   |
| -- | -- |
| params.yml   | YAML-formatted configuration paramaters               |
| windows.py   | Extracts sites from input VCF                         |
| stats.py     | Compute statistics from observed/simulated data       |
| priors.py    | Plot prior distributions based on models              |
| simul.py     | Define models and run simulations                     |
| monitor.py   | Display progress of simulations                       |
| clean.py     | Delete uncompleted simulation files                   |
| lda.py       | Perform linear discriminant analysis on simulations   |
| plot.py      | Plot parameters/statistics from simulations           |
| abcranger.py | Perform model choice/parameter estimation             |
| post.py      | Plot posterior distribution and posterior simulations |
