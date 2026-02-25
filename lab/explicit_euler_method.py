import marimo

__generated_with = "0.19.11"
app = marimo.App()


@app.cell
def _():
    import numpy as np
    import matplotlib.pyplot as plt

    return np, plt


@app.cell
def _(np):
    def f(y, t):
        return ((np.sin(y)-np.exp(t))/np.cos(t))

    return (f,)


@app.cell
def _(f, np, plt):
    def euler_forward(a, b, h, y0):
        Nf = (b-a)/h
        length = int(round(Nf+1))
        tf = np.linspace(a, b, length)
        yf = np.zeros(length)
        tf[0] = a
        yf[0] = y0

        for i in range(1, length):
            yf[i] = yf[i-1]+h*f(tf[i-1], yf[i-1])
    
        print(f"Number of steps: {Nf}")
        print(f"Time steps: {tf}")
        print(f"Estimates solutions for each time step: {yf}")

        plt.figure(figsize=(10, 6))
        plt.plot(tf, yf, '.', markersize=10, color='red', label="Forward Euler Method $(h=h)$")
        plt.title("Estimated solution of $y(t_{i})$ vs Time using Euler Forward Method $(h=h)$")
        plt.legend()
        plt.grid(True, alpha=0.5)
        # plt.show()
    return (euler_forward,)


@app.cell
def _(euler_forward):
    euler_forward(0, 1, 0.5, 0)
    return


@app.cell
def _(euler_forward):
    euler_forward(0, 1, 0.02, 0)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
