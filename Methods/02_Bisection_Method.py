# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "matplotlib==3.10.8",
#     "pandas==2.3.3",
# ]
# ///

import marimo

__generated_with = "0.18.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    return np, pd, plt


@app.cell
def _(pd):
    def bisection_method(fn, xl, xu, es, imax):
        """
        Standard Bisection Method implementation.
        :param fn: The function for which we are finding root.
        :param xl: Lower guess
        :param xu: Upper guess
        :param es: Desired relative error (%)
        :param imax: Maximum iterations
        :return:
        """

        history = []
        itr = 0
        xr = 0.0
        ea = 100.0 # Initial error

        # Check if root exists in the given interval
        if fn(xl) * fn(xu) >= 0:
            print("Bisection method fails: f(xl) and f(xu) must be opposite signs.")
            return None

        while True:
            xr_old = xr
            xr = (xl + xu) / 2
            itr += 1

            if xr != 0:
                ea = abs((xr - xr_old) / xr) * 100

            history.append({
                "Iteration": itr,
                "xl": xl,
                "xu": xu,
                "xr": xr,
                "ea (%)": ea,
                "es (%)": es
            })

            test = fn(xl) * fn(xr)

            if test < 0:
                xu = xr
            elif test > 0:
                xl = xr
            else:
                ea = 0

            if ea < es or itr >= imax:
                break

        return xr, pd.DataFrame(history)
    return (bisection_method,)


@app.function
def my_function(x):
    return x**3 - 2 * x**2 - 0.5


@app.cell
def _(bisection_method):
    # Parameters: f, xl=0, xu=3, es=0.01%, imax=100
    root, df = bisection_method(my_function, xl=0, xu=5, es=0.01, imax=100)

    print(f"Final Root: {root}")
    print("\nIteration Table:")
    return (df,)


@app.cell
def _(df):
    df
    return


@app.cell
def _(df, np):
    x_min, x_max = df['xl'].min() - 1, df['xu'].max() + 1
    x = np.linspace(x_min, x_max, 500)
    y = my_function(x)
    return x, y


@app.cell
def _(df, plt, x, y):
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, 'b-', linewidth=2, label='f(x)')
    plt.axhline(0, color='black')
    plt.axvline(0, color='black')

    for i in range(len(df)):
        plt.plot([df['xl'], df['xu'], df['xr']], [my_function(df['xl']), my_function(df['xu']), my_function(df['xr'])], 'ko')
        plt.plot([df['xl'], df['xu']], [my_function(df['xl']), my_function(df['xu'])], 'r:', label='Secent line')


    plt.title(f"Root Finding Visualization | Range (xl={df['xl'].iloc[0]}, xu={df['xu'].iloc[0]})")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True, alpha=0.5)
    plt.tight_layout()
    plt.show()
    return


@app.cell
def _(df, plt):
    plt.figure(figsize=(8, 6))
    plt.plot(df['Iteration'], df['ea (%)'], marker='o', label="Actual error")
    plt.axhline(y=df["es (%)"].iloc[0], color='r', linestyle='--', label="Target error")

    plt.title("Bisection Method Convergence: Error vs. Iteration")
    plt.xlabel("Iteration")
    plt.ylabel("Error (%)")
    plt.legend()
    plt.grid(True, alpha=0.5)
    plt.tight_layout()
    plt.show()
    return


if __name__ == "__main__":
    app.run()
