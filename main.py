import numpy as np 
# 1. Generate reproducible random data
rng=np.random.default_rng(42)
data=rng.integers(1,101,100)

print(data)
print(f"Data Shape: {data.shape}")
print(f"Minimum {data.min()}" )
print(f"Maximum {data.max()}")

mean=np.mean(data)
print(f"Mean: {mean}")

std=np.std(data)
print(f"Standard Deviation: {std}")

z_score=(data-mean)/std
print(z_score)

#Check that the normalized mean is close to 0 and std is close to 1.
print(f"Normalized Mean: {np.mean(z_score)}")
print(f"Normalized STD: {np.std(z_score)}")
# Save the code and a README.md, then push the project to GitHub.