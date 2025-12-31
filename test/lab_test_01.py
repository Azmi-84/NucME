# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "matplotlib==3.10.8",
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
    return np, plt, sns


@app.cell
def _(sns):
    sns.set_theme()
    return


@app.cell
def _(np):
    x = np.linspace(-4, 6, 2000)
    y = np.log(1+x**2)
    return x, y


@app.cell
def _(plt, x, y):
    # plt.xlim(-4, 6)
    # plt.ylim(4, 0)
    plt.grid(True)

    plt.figure(figsize=(8, 6))
    plt.plot(x, y, 'k', linewidth=2)
    plt.title("Approximating log(1+x**2) function using Taylor Series")
    plt.xlabel("X Axis")
    plt.ylabel("Y Axis")

    plt.tight_layout()
    plt.show()
    return


@app.cell
def _(np, plt, x, y):
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, 'k', linewidth=2)
    plt.title("Approximating log(1+x**2) function using Taylor Series")
    plt.xlabel("X Axis")
    plt.ylabel("Y Axis")

    _polynomial_cofficient = [1, 0, 0]
    _val = np.polyval(_polynomial_cofficient, x)
    plt.plot(x, _val, 'g--', linewidth=2)

    _polynomial_cofficient = [-1/2, 0, 1, 0, 0]
    _val = np.polyval(_polynomial_cofficient, x)
    plt.plot(x, _val, 'b--', linewidth=2)

    _polynomial_cofficient = [1/3, 0, -1/2, 0, 1, 0, 0]
    _val = np.polyval(_polynomial_cofficient, x)
    plt.plot(x, _val, 'y--', linewidth=2)

    _polynomial_cofficient = [-1/4, 0, 1/3, 0, -1/2, 0, 1, 0, 0]
    _val = np.polyval(_polynomial_cofficient, x)
    plt.plot(x, _val, 'r--', linewidth=2)

    _polynomial_cofficient = [1/5, 0, -1/4, 0, 1/3, 0, -1/2, 0, 1, 0, 0]
    _val = np.polyval(_polynomial_cofficient, x)
    plt.plot(x, _val, 'c--', linewidth=2)

    plt.legend(('log(1+x**2)', 'second order', 'fourth order', 'sixth order', 'eight order', 'tenth order'))
    plt.tight_layout()
    plt.show()
    return


if __name__ == "__main__":
    app.run()
