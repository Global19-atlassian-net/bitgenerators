'''
Bit Generators
--------------

The random values produced by :class:`~Generator`
orignate in a BitGenerator.  The BitGenerators do not directly provide
random numbers and only contains methods used for seeding, getting or
setting the state, jumping or advancing the state, and for accessing
low-level wrappers for consumption by code that can efficiently
access the functions provided, e.g., `numba <https://numba.pydata.org>`_.

Seeding and Entropy
-------------------

A BitGenerator provides a stream of random values. In order to generate
reproducableis streams, BitGenerators support setting their initial state via a
seed. But how best to seed the BitGenerator? On first impulse one would like to
do something like ``[bg(i) for i in range(12)]`` to obtain 12 non-correlated,
independent BitGenerators. However using a highly correlated set of seed could
generate BitGenerators that are correlated or overlap within a few samples.
NumPy uses a `SeedSequence` class to mix the seed in a reproducable way that
introduces the necesarry entroy to produce independent and largely non-
overlapping streams.

BitGenerator Streams
--------------------
MT19937
DSFMT
GJRAND
JSF64
PCG32
PCG64
Philox
ThreeFry
SFC64
Xoshiro256
Xoshiro512
===================
'''

from .mt19937 import MT19937
from .dsfmt import DSFMT
from .gjrand import GJrand
from .jsf64 import JSF64
from .pcg32 import PCG32
from .pcg64 import PCG64
from .philox import Philox
from .sfc64 import SFC64
from .threefry import ThreeFry
from .xoshiro256 import Xoshiro256
from .xoshiro512 import Xoshiro512

__all__ = ['MT19937', 'DSFMT', 'GJrand', 'JSF64', 'Philox', 'PCG64', 'PCG32',
           'SFC64', 'ThreeFry', 'Xoshiro256', 'Xoshiro512']

# register the bit generators for pickling

import numpy.random._pickle
numpy.random._pickle.BitGenerators.update({
        'MT19937': MT19937,
        'DSFMT': DSFMT,
        'GJRAND': GJrand,
        'JSF64': JSF64,
        'PCG32': PCG32,
        'PCG64': PCG64,
        'Philox': Philox,
        'SFC64': SFC64,
        'ThreeFry': ThreeFry,
        'Xoshiro256': Xoshiro256,
        'Xoshiro512': Xoshiro512
    })
