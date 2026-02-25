# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "matplotlib==3.10.8",
#     "numpy==2.4.0",
#     "scipy==1.16.3",
# ]
# ///

import marimo

__generated_with = "0.18.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import numpy as np
    import scipy as sp
    import matplotlib.pyplot as plt
    return np, plt, sp


@app.cell
def _(np):
    x_range = np.linspace(-2, 2, 15)
    y_range = np.linspace(0, 5, 15)

    x, y = np.meshgrid(x_range, y_range)
    return x, y


@app.cell
def _(np):
    def velocity(position, time):
        _x, _y = position
        u = 0.5 + 0.8 * _x
        v = 1.5 + 2.5 * np.sin((2*np.pi) * time) - 0.8 * _y
        return [u, v]
    return (velocity,)


@app.cell
def _(x, y, np, plt):
    _u =  0.5 + 0.8 * x
    _v = 1.5 + 2.5 * np.sin((2*np.pi) * 2.0) - 0.8 * y

    plt.figure(figsize=(8, 6))
    plt.streamplot(x, y, _u, _v)
    plt.title('Instantaneous Streamlines at t = 2s')
    plt.tight_layout()
    plt.show()
    return


@app.cell
def _(np, plt, sp, velocity):
    t_span = np.linspace(0, 2, 100)
    initial_position = [0.5, 0.5]

    pathline_coordinates = sp.integrate.odeint(velocity, initial_position, t_span)

    plt.figure(figsize=(8, 6))
    plt.plot(pathline_coordinates[:, 0], pathline_coordinates[:, 1], 'r-', label='Pathline')
    plt.legend()
    plt.grid(True, alpha=0.4)
    plt.tight_layout()
    plt.show()
    return


@app.cell
def _(np, plt, sp, velocity):
    t_present = 2.0
    release_times = np.linspace(0, t_present, 50)
    injection_point = [0.5, 0.5]
    streak_x, streak_y = [], []

    for tau in release_times:
        t_track = np.linspace(tau, t_present, 10)
        sol = sp.integrate.odeint(velocity, injection_point, t_track)

        streak_x.append(sol[-1, 0])
        streak_y.append(sol[-1, 1])

    plt.plot(streak_x, streak_y, 'b--', label="Streakline")
    return


if __name__ == "__main__":
    app.run()
