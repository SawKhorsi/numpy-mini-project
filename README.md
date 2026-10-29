# NumPy Data Analysis Mini-Project

## Project Overview

This is my Week 1 mini-project from my 6-month AI/ML Engineering learning roadmap.

The project uses NumPy to generate a random dataset, calculate basic statistics, and perform Z-score standardization.

## Technologies Used

- Python
- NumPy
- Git and GitHub

## Project Features

1. Generate 100 reproducible random integers using `np.random.default_rng(42)`.
2. Display the dataset's shape, minimum, and maximum values.
3. Calculate the mean using `np.mean()`.
4. Calculate the standard deviation using `np.std()`.
5. Standardize the dataset using Z-score standardization.
6. Verify that the standardized data has a mean close to 0 and a standard deviation close to 1.

## Z-Score Standardization

The formula used is:

**Z = (X - Mean) / Standard Deviation**

Z-score standardization transforms data so that its mean is approximately 0 and its standard deviation is approximately 1.

This is useful in machine learning because it puts numerical features on comparable scales, which can help certain algorithms train more effectively.

## How to Run

1. Install Python and NumPy.
2. Open the project folder in VS Code.
3. Run the following command:

```bash
pip install numpy
python main.py
```

## What I Learned

Through this project, I learned how to:

- Generate reproducible random datasets using NumPy.
- Work with NumPy arrays and their shapes.
- Calculate basic statistics.
- Apply Z-score standardization.
- Understand why feature scaling is important in machine learning.
- Use Git and GitHub to manage my code.

## Future Improvements

- Analyze datasets with multiple features.
- Standardize each column separately.
- Visualize data distributions using Matplotlib.
- Apply these techniques to real-world datasets.
