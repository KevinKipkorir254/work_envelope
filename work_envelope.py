import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#defined variables
q1_min = -1.54
q1_max = 1.54

q2_min = 0
q2_max = 1.54

q3_min = -1.54
q3_max = 1.54

q4_min = -1.54
q4_max = 1.54

#define link lenghts
link_1 = 100
link_2 = 100
link_3 = 100
link_4 = 100

# Define the joint ranges for each joint (adjust as needed)
q1_values = np.linspace(q1_min, q1_max, num=20)
q2_values = np.linspace(q2_min, q2_max, num=20)
q3_values = np.linspace(q3_min, q3_max, num=20)
q4_values = np.linspace(q4_min, q4_max, num=20)

# Initialize lists to store reachable points
reachable_x = []
reachable_y = []
reachable_z = []


# Calculate reachable points for each joint configuration
for q1 in q1_values:
    for q2 in q2_values:
        for q3 in q3_values:
            for q4 in q4_values:
                # Calculate end effector position using forward kinematics equations
                theta_1 = q1
                theta_2 = q2
                theta_3 = q3
                theta_4 = q4

                x = math.cos(theta_1) * (link_2 * math.cos(theta_2) + link_2 * math.cos(theta_2 + theta_3)) + link_4 * math.cos(theta_1) * math.cos(theta_2 + theta_3 + theta_4)  # Replace with your forward kinematics equations
                y = math.sin(theta_1) * (link_2 * math.cos(theta_2) + link_3 * math.cos(theta_2 + theta_3)) + link_4 * math.sin(theta_1) * math.cos(theta_2 + theta_3 + theta_4)
                z = (link_1 + link_2 * math.sin(theta_2) + link_3 * math.sin(theta_2 + theta_3)) + link_4 * math.sin(theta_2 + theta_3 + theta_4)
            
                # Store the reachable point
                reachable_x.append(x)
                reachable_y.append(y)
                reachable_z.append(z)
                print("working\n")


# Create a 3D scatter plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(reachable_x, reachable_y, reachable_z, marker='.', s=1)

# Customize the plot (labels, title, etc.) as needed
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('Robot Work Envelope')

# Show the plot
plt.show()
print("END")