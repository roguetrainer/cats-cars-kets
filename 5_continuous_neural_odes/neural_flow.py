import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Continuous Depth: Neural ODEs
# We compare flowing through Field A then Field B vs Field B then Field A

def vector_field_A(t, state):
    # Rotation [[0, -1], [1, 0]]
    x, y = state
    return [-y, x]

def vector_field_B(t, state):
    # Shearing [[0, 1], [1, 0]]
    x, y = state
    return [y, x]

def run_neural_ode():
    initial_state = [1.0, 0.0]
    t_span = [0, 1.5]
    
    # Path 1: A then B
    sol1 = solve_ivp(vector_field_A, t_span, initial_state)
    mid_1 = sol1.y[:, -1]
    sol2 = solve_ivp(vector_field_B, t_span, mid_1)
    end_1 = sol2.y[:, -1]
    
    # Path 2: B then A
    sol3 = solve_ivp(vector_field_B, t_span, initial_state)
    mid_2 = sol3.y[:, -1]
    sol4 = solve_ivp(vector_field_A, t_span, mid_2)
    end_2 = sol4.y[:, -1]
    
    fig, ax = plt.subplots(figsize=(8, 8))
    # Visualize Start/Ends
    ax.scatter([1], [0], c='green', s=100, label='Input')
    ax.scatter(end_1[0], end_1[1], c='blue', s=100, label='Flow A->B')
    ax.scatter(end_2[0], end_2[1], c='red', s=100, label='Flow B->A')
    ax.arrow(end_1[0], end_1[1], end_2[0]-end_1[0], end_2[1]-end_1[1], 
             color='purple', width=0.05, label='Non-Commutativity')
    
    ax.set_title("Continuous: Neural ODE Flows are Non-Commutative")
    ax.legend(); ax.grid(True); ax.axis('equal')
    plt.savefig('neural_flow.png')

if __name__ == "__main__":
    run_neural_ode()
