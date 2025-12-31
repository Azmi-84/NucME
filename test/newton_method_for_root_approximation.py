# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "matplotlib==3.10.8",
#     "numpy==2.4.0",
#     "pandas==2.3.3",
# ]
# ///

import marimo

__generated_with = "0.18.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import math
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    return np, plt


@app.cell
def _(np):
    def f(x):
        return 8 * (np.sin(x) * np.exp(-x) * np.cos(x)) - 1

    def df1(x):
        return 8 * (((-np.sin(x) * np.exp(-x)) + (np.cos(x) * np.exp(-x)) * np.cos(x)) - (8 * (np.sin(x) * np.exp(-x) * np.cos(x)) - 1) *np.sin(x))
    return df1, f


@app.cell
def _(f, np, plt):
    _ran = np.arange(-5, 5, 0.1)
    _val = f(_ran)
    _dfval = f(_ran)

    plt.plot(_ran, _val, label=r'$f(x) = 8sin(x)e^(-x) -1$')
    plt.title("Graph of f(x) = 8sin(x)e^(-x) -1")
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()
    return


@app.cell
def _(f, np, plt):
    _ran = np.arange(-5, 5, 0.1)
    _dfval = f(_ran)

    plt.plot(_ran, _dfval, label=r'$df1(x) = 8 * ((-np.sin(x) * np.exp(-x)) + (np.cos(x) * np.exp(-x)))')
    plt.title("Graph of df1(x) = 8 * ((-np.sin(x) * np.exp(-x)) + (np.cos(x) * np.exp(-x)))")
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()
    return


@app.function
def g(x, f, df1):
    return x-f(x)/df1(x)


@app.cell
def _(df1, f, np):
    max_itr = 8
    xn = np.zeros(max_itr)
    xn[0] = 0.3

    for _i in range(1, max_itr):
        xn[_i] = g(xn[_i-1], f, df1)
    return (xn,)


@app.cell
def _(f, np, plt, xn):
    _ran = np.arange(-5, 5, 0.1)
    _val = f(_ran)
    fn = f(xn)

    plt.plot(_ran, _val)
    plt.plot(xn, fn, "x", label='Approximate Roots')
    plt.title("Approximation of Roots of function f(x)")
    plt.grid()
    plt.legend()
    plt.tight_layout()
    plt.show()
    return


@app.cell
def _(xn):
    print(f"Approximated Roots: {xn}")
    return


if __name__ == "__main__":
    app.run()
