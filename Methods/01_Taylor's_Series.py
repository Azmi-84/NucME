# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "matplotlib==3.10.7",
#     "numpy==2.3.5",
#     "seaborn==0.13.2",
# ]
# ///

import marimo

__generated_with = "0.17.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import math
    import numpy as np
    import seaborn as sns
    import matplotlib.pyplot as plt

    sns.set_theme()
    return math, np, plt


@app.cell
def _(np):
    x = np.linspace(-10, 10, 2000)
    y = np.sin(x)
    return x, y


@app.cell
def _(math, np, plt, x, y):
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, 'k', linewidth=2)
    plt.title("Approximating Sin Curve using Taylor Polynomials")
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.grid(True)

    _polynomials_coefficients = [1, 0]
    _yt = np.polyval(_polynomials_coefficients, x)
    plt.plot(x, _yt, 'b--', linewidth=2)

    _polynomials_coefficients = [-1/math.factorial(3), 0, 1, 0]
    _yt = np.polyval(_polynomials_coefficients, x)
    plt.plot(x, _yt, 'r--', linewidth=2)

    _polynomials_coefficients = [1/math.factorial(5), 0, -1/math.factorial(3), 0, 1, 0]
    _yt = np.polyval(_polynomials_coefficients, x)
    plt.plot(x, _yt, 'g--', linewidth=2)

    _polynomials_coefficients = [-1/math.factorial(7), 0, 1/math.factorial(5), 0, -1/math.factorial(3), 0, 1, 0]
    _yt = np.polyval(_polynomials_coefficients, x)
    plt.plot(x, _yt, 'y--', linewidth=2)

    _polynomials_coefficients = [1/math.factorial(9), 0, -1/math.factorial(7), 0, 1/math.factorial(5), 0, -1/math.factorial(3), 0, 1, 0]
    _yt = np.polyval(_polynomials_coefficients, x)
    plt.plot(x, _yt, 'c--', linewidth=2)


    plt.legend(('sin(x)', '1st order', '3rd order', '5th order', '7th order', '9th order'))
    plt.tight_layout()
    plt.show()
    return


if __name__ == "__main__":
    app.run()
