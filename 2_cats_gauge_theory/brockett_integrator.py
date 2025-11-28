import numpy as np
import matplotlib.pyplot as plt

def run_brockett():
    t = np.linspace(0, 4 * np.pi, 1000)
    dt = t[1] - t[0]
    # Input 1: "Bend" (Cosine)
    u1 = np.cos(t)
    # Input 2: "Twist" (Sine)
    u2 = np.sin(t)
    x, y, z = np.zeros_like(t), np.zeros_like(t), np.zeros_like(t)

    for i in range(1, len(t)):
        x[i] = x[i-1] + u1[i-1] * dt
        y[i] = y[i-1] + u2[i-1] * dt
        # The Commutator Effect: z (Rotation) changes based on area swept by Bend/Twist
        z[i] = z[i-1] + (x[i-1] * u2[i-1] - y[i-1] * u1[i-1]) * dt

    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(x, y, z, label='Cat Trajectory', linewidth=2)
    ax.set_title('Cats (SO(3)): [Bend, Twist] != 0 creates Rotation')
    plt.savefig('cat_gauge_field.png')

if __name__ == "__main__":
    run_brockett()
