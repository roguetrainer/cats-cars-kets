import numpy as np
import matplotlib.pyplot as plt

def apply_commutator_parking():
    # Initial State [x, y, theta]
    state = np.array([0.0, 0.0, 0.0])
    path = [state.copy()]
    phi = np.pi / 4  
    dt = 0.01 
    
    def update_state(current_state, v, w, duration):
        steps = int(duration / dt)
        temp_state = current_state.copy()
        for _ in range(steps):
            theta = temp_state[2]
            temp_state[0] += v * np.cos(theta) * dt
            temp_state[1] += v * np.sin(theta) * dt
            temp_state[2] += w * dt
            path.append(temp_state.copy())
        return temp_state

    # COMMUTATOR: Steer, Drive, Un-Steer, Un-Drive
    state = update_state(state, v=0, w=phi, duration=1.0)  # A
    state = update_state(state, v=1, w=0, duration=1.0)    # B
    state = update_state(state, v=0, w=-phi, duration=1.0) # A_inv
    state = update_state(state, v=-1, w=0, duration=1.0)   # B_inv

    path = np.array(path)
    plt.figure(figsize=(8, 8))
    plt.plot(path[:, 0], path[:, 1], label='Path', linewidth=2)
    plt.scatter(path[-1, 0], path[-1, 1], color='red', s=100, label='End')
    plt.arrow(0, 0, path[-1, 0], path[-1, 1], width=0.01, color='orange', label='Commutator Shift')
    plt.title(f"Cars (SE(2)): The Lie Bracket [Drive, Steer]")
    plt.grid(True); plt.legend(); plt.axis('equal')
    plt.savefig('car_commutator.png')

if __name__ == "__main__":
    apply_commutator_parking()
