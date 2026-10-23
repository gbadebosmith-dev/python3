# Build a python 3.11 script that imports the statistics module and creates a class the includes the statistics functions also known as methods of which pass into them a maximum of two variables and ignore the functions with more than two variables maximum. You can include the statistics functions where two variables are mandatory and the other variables are optional. Utilise a data list of [1,2,3,4,5,5,6,7,8,5,5,9]. And for the other variable in the function you choose the value that is adequate. And if there is only one data variable use the data list or something that is more adequate of your choosing. Then print the results of the functions in the class.

# Claude Agent Result is incomplete list of functions 16 but there should be 19
"""
statistics_analysis.py
Python 3.11 — Wraps every statistics-module function that accepts
at most two parameters (mandatory or optional) inside a class.

Data list  : [1, 2, 3, 4, 5, 5, 6, 7, 8, 5, 5, 9]
Second var : chosen per function (see class docstrings).
"""

import statistics


# ─────────────────────────────────────────────────────────────────────────────
# Helper
# ─────────────────────────────────────────────────────────────────────────────

def section(title: str) -> None:
    """Print a section banner."""
    print(f"\n{'─' * 55}")
    print(f"  {title}")
    print(f"{'─' * 55}")


# ─────────────────────────────────────────────────────────────────────────────
# Class
# ─────────────────────────────────────────────────────────────────────────────

class StatisticsAnalysis:
    """
    Wraps statistics-module functions that take ≤ 2 parameters.

    Included (signature → max params):
        mean(data)                          → 1
        fmean(data, weights=None)           → 2
        geometric_mean(data)               → 1
        harmonic_mean(data, weights=None)  → 2
        median(data)                        → 1
        median_low(data)                   → 1
        median_high(data)                  → 1
        median_grouped(data, interval=1)   → 2
        mode(data)                          → 1
        multimode(data)                    → 1
        pstdev(data, mu=None)              → 2
        pvariance(data, mu=None)           → 2
        stdev(data, xbar=None)             → 2
        variance(data, xbar=None)          → 2
        covariance(x, y)                   → 2
        correlation(x, y)                  → 2

    Excluded (> 2 total parameters):
        quantiles(data, *, n=4, method=…)  → 3
    """

    def __init__(self, data: list):
        self.data = data

    # ── Averages / Central Tendency ──────────────────────────────────────────

    def mean(self) -> float:
        """Arithmetic mean.  statistics.mean(data)"""
        return statistics.mean(self.data)

    def fmean(self, weights: list | None = None) -> float:
        """
        Fast float mean.  statistics.fmean(data, weights=None)
        Second var: weights=[1,1,1,1,2,2,1,1,1,2,2,1]
        reflecting that the value 5 appears four times.
        """
        return statistics.fmean(self.data, weights)

    def geometric_mean(self) -> float:
        """Geometric mean.  statistics.geometric_mean(data)"""
        return statistics.geometric_mean(self.data)

    def harmonic_mean(self, weights: list | None = None) -> float:
        """
        Harmonic mean.  statistics.harmonic_mean(data, weights=None)
        Second var: same weight list as fmean.
        """
        return statistics.harmonic_mean(self.data, weights)

    # ── Medians ──────────────────────────────────────────────────────────────

    def median(self) -> float:
        """Middle value.  statistics.median(data)"""
        return statistics.median(self.data)

    def median_low(self) -> float:
        """Low median.  statistics.median_low(data)"""
        return statistics.median_low(self.data)

    def median_high(self) -> float:
        """High median.  statistics.median_high(data)"""
        return statistics.median_high(self.data)

    def median_grouped(self, interval: int | float = 1) -> float:
        """
        Grouped median.  statistics.median_grouped(data, interval=1)
        Second var: interval=2  (bin width of 2 for this spread of values).
        """
        return statistics.median_grouped(self.data, interval)

    # ── Mode ─────────────────────────────────────────────────────────────────

    def mode(self):
        """Single mode.  statistics.mode(data)"""
        return statistics.mode(self.data)

    def multimode(self) -> list:
        """All modes.  statistics.multimode(data)"""
        return statistics.multimode(self.data)

    # ── Spread / Dispersion ──────────────────────────────────────────────────

    def pstdev(self, mu: float | None = None) -> float:
        """
        Population standard deviation.  statistics.pstdev(data, mu=None)
        Second var: mu = population mean (pre-calculated for efficiency).
        """
        return statistics.pstdev(self.data, mu)

    def pvariance(self, mu: float | None = None) -> float:
        """
        Population variance.  statistics.pvariance(data, mu=None)
        Second var: mu = population mean.
        """
        return statistics.pvariance(self.data, mu)

    def stdev(self, xbar: float | None = None) -> float:
        """
        Sample standard deviation.  statistics.stdev(data, xbar=None)
        Second var: xbar = sample mean.
        """
        return statistics.stdev(self.data, xbar)

    def variance(self, xbar: float | None = None) -> float:
        """
        Sample variance.  statistics.variance(data, xbar=None)
        Second var: xbar = sample mean.
        """
        return statistics.variance(self.data, xbar)

    # ── Two-variable (x, y) ──────────────────────────────────────────────────

    def covariance(self, y: list) -> float:
        """
        Sample covariance.  statistics.covariance(x, y)
        Both x and y must have the same length.
        """
        return statistics.covariance(self.data, y)

    def correlation(self, y: list) -> float:
        """
        Pearson correlation coefficient.  statistics.correlation(x, y)
        Returns a value in [-1, 1].
        """
        return statistics.correlation(self.data, y)


# ─────────────────────────────────────────────────────────────────────────────
# Data
# ─────────────────────────────────────────────────────────────────────────────

DATA = [1, 2, 3, 4, 5, 5, 6, 7, 8, 5, 5, 9]

# Weights — length matches DATA; the four 5s get weight 2, others weight 1
WEIGHTS = [1, 1, 1, 1, 2, 2, 1, 1, 1, 2, 2, 1]

# Pre-computed mean values (passed as the optional second parameter)
POPULATION_MEAN = statistics.mean(DATA)          # used as mu
SAMPLE_MEAN     = statistics.mean(DATA)          # used as xbar (same formula here)

# A correlated y-sequence for covariance / correlation
# Each value is DATA[i] + 1, giving perfect positive correlation baseline
# with a slight shuffle to make the covariance non-trivial but still positive
DATA_Y = [2, 3, 5, 4, 6, 7, 5, 8, 9, 6, 7, 10]

# ─────────────────────────────────────────────────────────────────────────────
# Run & Print
# ─────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":

    sa = StatisticsAnalysis(DATA)

    print("=" * 55)
    print("   Python 3.11 — statistics module class demo")
    print("=" * 55)
    print(f"\n  Data    : {DATA}")
    print(f"  Weights : {WEIGHTS}  (5 gets weight 2)")
    print(f"  Data Y  : {DATA_Y}  (for covariance/correlation)")

    # ── Averages ─────────────────────────────────────────────────────────────
    section("AVERAGES / CENTRAL TENDENCY")

    print(f"  mean()                          → {sa.mean()}")
    print(f"  fmean()          (no weights)   → {sa.fmean()}")
    print(f"  fmean(weights)   (weighted)     → {sa.fmean(WEIGHTS):.6f}")
    print(f"  geometric_mean()                → {sa.geometric_mean():.6f}")
    print(f"  harmonic_mean()  (no weights)   → {sa.harmonic_mean():.6f}")
    print(f"  harmonic_mean(weights)          → {sa.harmonic_mean(WEIGHTS):.6f}")

    # ── Medians ───────────────────────────────────────────────────────────────
    section("MEDIANS")

    print(f"  median()                        → {sa.median()}")
    print(f"  median_low()                    → {sa.median_low()}")
    print(f"  median_high()                   → {sa.median_high()}")
    print(f"  median_grouped(interval=1)      → {sa.median_grouped(1):.1f}")
    print(f"  median_grouped(interval=2)      → {sa.median_grouped(2):.1f}")

    # ── Mode ──────────────────────────────────────────────────────────────────
    section("MODE")

    print(f"  mode()                          → {sa.mode()}")
    print(f"  multimode()                     → {sa.multimode()}")

    # ── Spread ────────────────────────────────────────────────────────────────
    section("SPREAD / DISPERSION")

    print(f"  pstdev()         (no mu)        → {sa.pstdev():.6f}")
    print(f"  pstdev(mu)       mu={POPULATION_MEAN}     → {sa.pstdev(POPULATION_MEAN):.6f}")
    print(f"  pvariance()      (no mu)        → {sa.pvariance():.6f}")
    print(f"  pvariance(mu)    mu={POPULATION_MEAN}     → {sa.pvariance(POPULATION_MEAN):.6f}")
    print(f"  stdev()          (no xbar)      → {sa.stdev():.6f}")
    print(f"  stdev(xbar)      xbar={SAMPLE_MEAN}   → {sa.stdev(SAMPLE_MEAN):.6f}")
    print(f"  variance()       (no xbar)      → {sa.variance():.6f}")
    print(f"  variance(xbar)   xbar={SAMPLE_MEAN}   → {sa.variance(SAMPLE_MEAN):.6f}")

    # ── Two-variable ──────────────────────────────────────────────────────────
    section("TWO-VARIABLE  (x=DATA, y=DATA_Y)")

    print(f"  covariance(y)                   → {sa.covariance(DATA_Y):.6f}")
    print(f"  correlation(y)                  → {sa.correlation(DATA_Y):.6f}")

    print(f"\n{'=' * 55}")
    print("  Done.")
    print(f"{'=' * 55}\n")
