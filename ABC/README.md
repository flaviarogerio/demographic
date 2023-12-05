ABC pipeline -- models with assymetrical recombination
======================================================

This document lists the scripts and results in this directory and the
order in which they should considered. More details are available as
comments within each of the scripts.

params.yml
----------

YAML-formatted configuration file with parameters used by the scripts in
the pipeline. Some parameters are used by several scripts, some by only
one script (in the latter case they are grouped in a specific section).

windows.py
----------

Extracts sites from the input VCF and group them in windows.

* Requires: VCF + sample structure.
* Generates: windows.yml, windows/*

stats.py
--------

By default, compute statistics from the observed dataset. If imported,
computes statistics from simulated datasets.

* Requires: windows.yml, windows/*
* Generates: obs.txt (unless imported)

simul.py
--------

Run simulations according to several models. If imported, expose models
and prior generators. Models are hardcoded in the file.

* Requires: stats.py, windows.yml, windows/*
* Generates: simuls/* (unless imported)

priors.py
---------

Performs a few samples from each model to represent the prior
distribution of parameters (without any bias). Models are hardcoded in
the file.

* Requires: simul.py
* Generates: priors/*

clean.py
--------

Utility script that removes all pairs of output files which have less
than the required number of simulations. All files in simuls/ are
treated.

plot.py
-------

Perform prior distribution of parameters (after filtering for replicates
with e.g. no polymorphic sites), and distribution of statistics. Process
all models defined in params.yml.

* Requires: simul.py, simuls/*, obs.txt
* Generates: plots/*

lda.py
------

Generate a LDA plot. Process all models defined in params.yml.

* Requires: simuls/*, obs.txt
* Generates: lda.png

abcranger.py
------------

Perform model choice using a range of numbers of replicates (in order to
assess robustness of answer), and parameter estimation using the best
model at the last number of replicates.

* Requires: simuls/*, obs.txt
* Generates: abcranger.res
