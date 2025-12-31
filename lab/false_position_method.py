# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "matplotlib==3.10.8",
#     "numpy==2.4.0",
#     "pandas==2.3.3",
#     "seaborn==0.13.2",
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
    def false_position_method(fn, xl, xu, es, imax):
        history = []
        itr = 0
        xr = 0.0
        fl = fn(xl)
        fu = fn(xu)
        ea = 100 # Initial error
        il = 0 # Counter stagnant lower bound
        iu = 0 # Counter stagnant upper bound

        # Check if root exists in the given interval
        if fl * fu >= 0:
            print("False-Position method fails. f(xl) and f(xu) must be opposite signs.")
            return None

        while True:
            xr_old = xr
            xr = xu - fn(xu) * (xl - xu) / (fn(xl) - fn(xu))

            fr = fn(xr)
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

            test = fl * fr

            if test < 0:
                xu = xr
                fu = fn(xu)
                iu = 0
                il += 1
                if il >= 2:
                    fl = fl / 2
            elif test > 0:
                xl = xr
                fl = fn(xl)
                il = 0
                iu += 1
                if iu >= 2:
                    fu = fu / 2
            else:
                ea = 0

            if ea < es or itr >= imax:
                break

        return xr, pd.DataFrame(history)
    return (false_position_method,)


@app.function
def my_function(x):
    return x**3 - 2 * x**2 - 0.005


@app.cell
def _(false_position_method):
    root, df = false_position_method(my_function, xl=0, xu=5, es=0.01, imax=1000)

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

    plt.title("False-Positon Method Convergence: Error vs. Iteration")
    plt.xlabel("Iteration")
    plt.ylabel("Error (%)")
    plt.legend()
    plt.grid(True, alpha=0.5)
    plt.tight_layout()
    plt.show()
    return


if __name__ == "__main__":
    app.run()
