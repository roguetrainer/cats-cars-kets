import pennylane as qml
from pennylane import numpy as np
import matplotlib.pyplot as plt

dev = qml.device("default.qubit", wires=1)

@qml.qnode(dev)
def order_XY(theta):
    qml.RX(theta, wires=0)
    qml.RY(theta, wires=0)
    return [qml.expval(qml.PauliX(0)), qml.expval(qml.PauliY(0)), qml.expval(qml.PauliZ(0))]

@qml.qnode(dev)
def order_YX(theta):
    qml.RY(theta, wires=0)
    qml.RX(theta, wires=0)
    return [qml.expval(qml.PauliX(0)), qml.expval(qml.PauliY(0)), qml.expval(qml.PauliZ(0))]

def visualize_commutator():
    theta = np.pi / 2
    pos_1 = order_XY(theta)
    pos_2 = order_YX(theta)
    
    fig = plt.figure(figsize=(8,8))
    ax = fig.add_subplot(111, projection='3d')
    # Wireframe Sphere
    u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
    x = np.cos(u)*np.sin(v)
    y = np.sin(u)*np.sin(v)
    z = np.cos(v)
    ax.plot_wireframe(x, y, z, color="gray", alpha=0.1)
    
    ax.quiver(0,0,0, pos_1[0], pos_1[1], pos_1[2], color='blue', label='XY')
    ax.quiver(0,0,0, pos_2[0], pos_2[1], pos_2[2], color='red', label='YX')
    ax.plot([pos_1[0], pos_2[0]], [pos_1[1], pos_2[1]], [pos_1[2], pos_2[2]], 
            color='purple', linestyle='--', linewidth=3, label='Commutator')
            
    ax.set_title("Kets (SU(2)): Quantum Commutator [X, Y] != 0")
    plt.legend()
    plt.savefig('quantum_commutator.png')

if __name__ == "__main__":
    visualize_commutator()
