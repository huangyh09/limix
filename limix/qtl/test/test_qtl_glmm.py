from __future__ import division

import pytest
from numpy import dot, sqrt, zeros
from numpy.random import RandomState
from numpy.testing import assert_allclose

from limix.qtl import scan


def test_qtl_glmm_binomial():
    random = RandomState(0)
    nsamples = 50

    X = random.randn(50, 2)
    G = random.randn(50, 100)
    K = dot(G, G.T)
    ntrials = random.randint(1, 100, nsamples)
    z = dot(G, random.randn(100)) / sqrt(100)

    successes = zeros(len(ntrials), int)
    for i, nt in enumerate(ntrials):
        for _ in range(nt):
            successes[i] += int(z[i] + 0.5 * random.randn() > 0)

    y = (successes, ntrials)

    lmm = scan(X, y, 'binomial', K, verbose=False)
    pv = lmm.variant_pvalues
    assert_allclose(pv, [0.409114, 0.697728], atol=1e-6, rtol=1e-6)


def test_qtl_glmm_wrong_dimensions():
    random = RandomState(0)
    nsamples = 50

    X = random.randn(50, 2)
    G = random.randn(50, 100)
    K = dot(G, G.T)
    ntrials = random.randint(1, 100, nsamples)
    z = dot(G, random.randn(100)) / sqrt(100)

    successes = zeros(len(ntrials), int)
    for i, nt in enumerate(ntrials):
        for _ in range(nt):
            successes[i] += int(z[i] + 0.5 * random.randn() > 0)

    y = (successes, ntrials)

    M = random.randn(49, 2)
    with pytest.raises(ValueError):
        scan(X, y, 'binomial', K, M=M, verbose=False)


def test_qtl_glmm_bernoulli():
    random = RandomState(0)
    nsamples = 50

    X = random.randn(50, 2)
    G = random.randn(50, 100)
    K = dot(G, G.T)
    ntrials = random.randint(1, 2, nsamples)
    z = dot(G, random.randn(100)) / sqrt(100)

    successes = zeros(len(ntrials), int)
    for i, nt in enumerate(ntrials):
        for _ in range(nt):
            successes[i] += int(z[i] + 0.5 * random.randn() > 0)

    lmm = scan(X, successes, 'bernoulli', K, verbose=False)
    pv = lmm.variant_pvalues
    assert_allclose(
        pv, [0.38268514676745735, 0.39206106093718096], atol=1e-6, rtol=1e-6)
