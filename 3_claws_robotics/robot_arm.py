import numpy as np
import matplotlib.pyplot as plt

# SE(3): Homogeneous Transformation Matrices (4x4)
# Represents Rotation (R) and Translation (T) combined

def get_se3(theta, axis, translation):
    c, s = np.cos(theta), np.sin(theta)
    if axis == 'x':
        R = np.array([[1, 0, 0], [0, c, -s], [0, s, c]])
    elif axis == 'y':
        R = np.array([[c, 0, s], [0, 1, 0], [-s, 0, c]])
    
    # Combined [ R  T ]
    #          [ 0  1 ]
    T_mat = np.eye(4)
    T_mat[:3, :3] = R
    T_mat[:3, 3] = translation
    return T_mat

def simulate_se3_arm():
    origin = np.array([0, 0, 0, 1]) 
    
    # Operation A: Rotate X by 90 deg AND Extend Arm
    Op_A = get_se3(np.pi/2, 'x', [0, 0, 1])
    
    # Operation B: Rotate Y by 90 deg AND Extend Arm
    Op_B = get_se3(np.pi/2, 'y', [0, 0, 1])
    
    # Path 1: A then B (Matrix mult: B @ A)
    pos_1 = Op_B @ (Op_A @ origin)
    
    # Path 2: B then A (Matrix mult: A @ B)
    pos_2 = Op_A @ (Op_B @ origin)
    
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot([0, pos_1[0]], [0, pos_1[1]], [0, pos_1[2]], color='blue', linewidth=2, label='Path A->B')
    ax.plot([0, pos_2[0]], [0, pos_2[1]], [0, pos_2[2]], color='red', linewidth=2, label='Path B->A')
    
    # Commutator
    ax.plot([pos_1[0], pos_2[0]], [pos_1[1], pos_2[1]], [pos_1[2], pos_2[2]], 
            color='purple', linestyle='--', linewidth=2, label='Commutator')
            
    ax.set_title("Claws (SE(3)): Non-Commutativity (Pos + Rot)")
    ax.legend()
    plt.savefig('robot_se3_commutator.png')

if __name__ == "__main__":
    simulate_se3_arm()
