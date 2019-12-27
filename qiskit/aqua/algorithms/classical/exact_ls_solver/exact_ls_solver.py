# -*- coding: utf-8 -*-

# This code is part of Qiskit.
#
# (C) Copyright IBM 2019.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.
"""The Exact LinearSystem algorithm."""

import logging

import numpy as np

from qiskit.aqua.algorithms.classical import ClassicalAlgorithm
from qiskit.aqua.utils.validation import validate

logger = logging.getLogger(__name__)


class ExactLSsolver(ClassicalAlgorithm):
    """The Exact LinearSystem algorithm."""

    _INPUT_SCHEMA = {
        '$schema': 'http://json-schema.org/draft-07/schema#',
        'id': 'ExactLSsolver_schema',
        'type': 'object',
        'properties': {
        },
        'additionalProperties': False
    }

    def __init__(self, matrix=None, vector=None):
        """Constructor.

        Args:
            matrix (array): the input matrix of linear system of equations
            vector (array): the input vector of linear system of equations
        """
        validate(locals(), self._INPUT_SCHEMA)
        super().__init__()
        self._matrix = matrix
        self._vector = vector
        self._ret = {}

    def _solve(self):
        self._ret['eigvals'] = np.linalg.eig(self._matrix)[0]
        self._ret['solution'] = list(np.linalg.solve(self._matrix, self._vector))

    def _run(self):
        """
        Run the algorithm to compute eigenvalues and solution.
        Returns:
            dict: Dictionary of results
        """
        self._solve()
        return self._ret
