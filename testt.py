import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Function to add text and minor decorations on each image
def add_decorations(ax, title, description):
    ax.text(0.5, 0.9, title, fontsize=16, fontweight="bold", ha="center")
    ax.text(0.5, 0.75, description, fontsize=12, ha="center", color="gray")
    ax.add_patch(patches.Rectangle((0.05, 0.05), 0.9, 0.15, color="lightgray", alpha=0.5))

# Generate individual mockups
fig, axs = plt.subplots(2, 3, figsize=(18, 12))
fig.suptitle("App Screens for Virtual Artifact Hunt", fontsize=20, fontweight="bold")

# Home Screen
axs[0, 0].set_title("Home Screen")
axs[0, 0].imshow([[0.7, 0.8, 0.9]])
add_decorations(axs[0, 0], "Artifact Hunt", "Start exploring or view your collection!")
axs[0, 0].add_patch(patches.Rectangle((0.35, 0.5), 0.3, 0.15, color="lightblue", alpha=0.8))  # Start button

# Scanner Screen
axs[0, 1].set_title("Scanner Screen")
axs[0, 1].imshow([[0.9, 0.8, 0.7]])
add_decorations(axs[0, 1], "Scanning for Artifacts", "Approach a site to collect a treasure.")
axs[0, 1].add_patch(patches.Circle((0.5, 0.5), 0.3, color="blue", alpha=0.2))  # Scanner overlay

# Map Screen
axs[0, 2].set_title("Map Screen")
axs[0, 2].imshow([[0.8, 0.9, 0.7]])
add_decorations(axs[0, 2], "City Map", "Explore the map to find artifacts!")
for x, y in [(0.3, 0.5), (0.5, 0.6), (0.7, 0.4)]:  # Artifact pins
    axs[0, 2].add_patch(patches.Circle((x, y), 0.05, color="orange", alpha=0.8))

# 3D Artifact View Screen
axs[1, 0].set_title("3D Artifact View")
axs[1, 0].imshow([[0.9, 0.7, 0.8]])
add_decorations(axs[1, 0], "Ancient Coin", "Learn more about this treasure.")
axs[1, 0].add_patch(patches.Circle((0.5, 0.5), 0.2, color="gold", alpha=0.4))  # Artifact render

# Leaderboard Screen
axs[1, 1].set_title("Leaderboard")
axs[1, 1].imshow([[0.8, 0.7, 0.9]])
add_decorations(axs[1, 1], "Leaderboard", "Check the top artifact hunters!")
for i, pos in enumerate([(0.3, 0.6), (0.3, 0.5), (0.3, 0.4)], start=1):
    axs[1, 1].text(pos[0], pos[1], f"User{i}: {i*10} Artifacts", ha="center", color="darkblue", fontsize=12)

# Special Page Screen
axs[1, 2].set_title("Special Page")
axs[1, 2].imshow([[0.7, 0.8, 0.85]])
add_decorations(axs[1, 2], "Special Reward!", "You've unlocked exclusive content!")
axs[1, 2].add_patch(patches.Rectangle((0.25, 0.35), 0.5, 0.3, color="purple", alpha=0.3))  # Reward banner

# Hide axes
for ax in axs.flat:
    ax.axis('off')

plt.show()
