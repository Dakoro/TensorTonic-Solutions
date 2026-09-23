import math

def binomial_pmf_cdf(n: int, p: float, k: int) -> dict:
    """
    Returns a dictionary with pmf and cdf.
    """
    results = []
    for i in range(k + 1):
        print(i, n, k)
        binomial_coeff = math.comb(n, i)
        result = binomial_coeff * p**i * (1 - p)**(n - i)
        results.append(result)
    pmf, cdf = (results[-1],  sum(results))
    return {
        "pmf": float(pmf),
        "cdf": float(cdf)
    }