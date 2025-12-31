# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "matplotlib==3.10.8",
#     "numpy==2.4.0",
# ]
# ///

import marimo

__generated_with = "0.17.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import numpy as np
    import matplotlib.pyplot as plt
    return np, plt


@app.cell
def _(np):
    x_range = np.linspace(-2, 2,15)
    y_range = np.linspace(0, 5, 15)

    x, y = np.meshgrid(x_range, y_range)
    return x, y


@app.cell
def _(x, y):
    # Velocity Vector Field

    u = 0.5 + 0.8 * x
    v = 1.5 - 0.8 * y
    return u, v


@app.cell
def _(x, y, np, plt, u, v):
    # Speed Calculation at Each Point
    speed = np.sqrt(u**2 + v**2)

    plt.figure(figsize=(8, 6))
    _q = plt.quiver(x, y, u, v, speed, cmap='viridis', pivot='mid')

    # Colorbar to define 'speed' colors
    _cbar = plt.colorbar(_q)
    _cbar.set_label('Flow Speed (m/s)')

    # Stagnation Point
    plt.plot(-0.625, 1.875, 'ro', label='Stagnation Point (-0.625, 1.875)')

    plt.title('Velocity Vector Field (Steady 2D Fow)')
    plt.xlabel('X-axis (m)')
    plt.ylabel('Y-axis (m)')
    plt.axhline(0, color='black', lw=1)
    plt.axvline(0, color='black', lw=1)
    plt.grid(alpha=0.5)
    plt.legend()
    plt.tight_layout()

    # Saving the Plot
    plt.savefig('velocity_vector_field.png', dpi=300, bbox_inches='tight')

    plt.show()
    return


@app.cell
def _(x, y):
    # Acceleration Vector Field

    ax = 0.4 + 0.64 * x
    ay = -1.2 + 0.64 * y
    return ax, ay


@app.cell
def _(x, y, ax, ay, np, plt):
    # Acceleration Calculation at Each Point
    acceleration = np.sqrt(ax ** 2 + ay ** 2)

    plt.figure(figsize=(8, 6))
    _q = plt.quiver(x, y, ax, ay, acceleration, cmap='viridis', pivot='mid')

    # Colorbar to define 'acceleration' colors
    _cbar = plt.colorbar(_q)
    _cbar.set_label('Flow Acceleration (m/s²)')

    # Zero Acceleration
    plt.plot(-0.625, 1.875, 'ro', label='Zero Acceleration (-0.625, 1.875)')

    plt.title('Acceleration Vector Field (Steady 2D Fow)')
    plt.xlabel('X-axis (m)')
    plt.ylabel('Y-axis (m)')
    plt.axhline(0, color='black', lw=1)
    plt.axvline(0, color='black', lw=1)
    plt.grid(alpha=0.3)
    plt.legend()
    plt.tight_layout()

    # Saving the Plot
    plt.savefig('acceleration_vector_field.png', dpi=300, bbox_inches='tight')

    plt.show()
    return


@app.cell
def _(x, y, plt, u, v):
    # Streamlines for 2D Steady Flow

    plt.figure(figsize=(8, 6))
    plt.streamplot(x, y, u, v, color='blue', linewidth=1, density=1.2)

    plt.title('Streamlines (Steady 2D Fow)')
    plt.xlabel('X-axis (m)')
    plt.ylabel('Y-axis (m)')
    plt.axhline(0, color='black', lw=1)
    plt.axvline(0, color='black', lw=1)
    plt.grid(alpha=0.5)
    plt.tight_layout()

    # Saving the Plot
    plt.savefig('streamlines_of_2D_flow.png', dpi=300, bbox_inches='tight')

    plt.show()
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
