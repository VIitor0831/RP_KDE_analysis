
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde

# Original rod photoreceptor counts
data = np.array([21, 28, 34, 38, 42, 44, 45, 50, 52, 55,
                 102, 104, 108, 109, 112, 115, 117, 119, 122])

# Kernel Density Estimation
kde = gaussian_kde(data, bw_method='scott')  # you can adjust bw_method if needed
x_range = np.linspace(min(data) - 10, max(data) + 10, 1000)
density = kde(x_range)

# Save KDE result to CSV
df = pd.DataFrame({'Rod Cell Count': x_range, 'KDE Density': density})
df.to_csv('kde_analysis_output.csv', index=False)

# Plot and save figure
plt.figure(figsize=(8, 6))
plt.plot(x_range, density, label='KDE Curve')
plt.fill_between(x_range, density, alpha=0.3)
plt.title('KDE of Rod Photoreceptor Counts')
plt.xlabel('Rod Cell Count')
plt.ylabel('Density')
plt.legend()
plt.savefig('kde_plot.png', dpi=300)
plt.close()
