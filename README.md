# Sorting Algorithm Performance Analysis - Bonus Assignment

## Educational Context

This repository contains a bonus assignment for data science bootcamp students focusing on **algorithm optimization and performance analysis**. This assignment bridges computer science fundamentals with data science practices, teaching students how to:

- Implement and compare different algorithms
- Conduct systematic performance experiments
- Analyze time and space complexity empirically
- Visualize performance data using matplotlib
- Apply statistical analysis to experimental results

## Learning Objectives

By completing this assignment, students will:

### 1. **Algorithm Implementation & Understanding**
- Understand how different sorting algorithms work (bubble sort, merge sort, built-in sort, NumPy sort)
- Learn to refactor code into reusable modules
- Practice writing clear, documented functions with proper docstrings

### 2. **Performance Analysis Skills**
- Design and conduct controlled experiments to measure algorithm performance
- Understand the difference between theoretical and empirical complexity analysis
- Learn to measure both time complexity (execution speed) and space complexity (memory usage)
- Apply statistical methods (mean, standard deviation) to experimental data

### 3. **Data Science Tools & Techniques**
- Use Python libraries essential for data science: NumPy, matplotlib, memory_profiler
- Create informative data visualizations with error bars and confidence intervals
- Analyze scaling behavior of algorithms with increasing input sizes
- Present findings through clear plots and written analysis

### 4. **Scientific Computing Best Practices**
- Structure experiments with proper controls and multiple trials
- Handle randomness and variability in experimental data
- Document methodology and interpret results scientifically

## Repository Structure

```
├── README.md                    # This file
├── requirements.txt             # Python dependencies
├── sort_functions.py           # Modular sorting algorithm implementations
├── sort_optimization.ipynb     # Main Jupyter notebook with experiments
└── assets/                     # Directory for any additional resources
```

## Getting Started

### Option 1: GitHub Codespaces (Recommended)

1. **Fork this repository** to your GitHub account:
   - Click the "Fork" button in the top-right corner of this repository
   - Select your GitHub account as the destination

2. **Open in GitHub Codespaces**:
   - In your forked repository, click the green "Code" button
   - Select the "Codespaces" tab
   - Click "Create codespace on main"
   - Wait for the environment to load (this may take a few minutes)

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Open the notebook**:
   - Navigate to `sort_optimization.ipynb` in the file explorer
   - Click to open it in Jupyter notebook interface
   - Run cells sequentially using Shift+Enter

### Option 2: Local Development

1. **Clone your forked repository**:
   ```bash
   git clone https://github.com/YOUR_USERNAME/gperdrizet-sort-bonus-assignment.git
   cd gperdrizet-sort-bonus-assignment
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Start Jupyter**:
   ```bash
   jupyter notebook
   ```

5. **Open `sort_optimization.ipynb`** in your browser

## Assignment Overview

The notebook is structured into four main sections:

### 1. Algorithm Implementations
- Four different sorting approaches: built-in sort, NumPy sort, bubble sort, and merge sort
- Each algorithm is implemented with detailed docstrings explaining how it works
- Functions are modularized in `sort_functions.py` for reusability

### 2. Basic Performance Testing
- Memory footprint measurement across multiple trials
- Execution time measurement with statistical analysis
- Histogram visualization of performance distributions

### 3. Time Complexity Analysis
- Systematic testing with increasing input sizes (powers of 2)
- Empirical observation of O(n log n) scaling behavior
- Line plots with confidence intervals showing scaling relationships

### 4. Space Complexity Analysis
- Memory usage measurement as a function of input size
- Comparison of memory efficiency between algorithms
- Analysis of overhead costs (e.g., NumPy array conversion)

## Key Experiments

Students will conduct three types of performance experiments:

1. **Fixed-size performance comparison**: Multiple trials with the same input size to understand variability
2. **Scaling analysis**: Testing with increasing input sizes to observe complexity growth
3. **Memory profiling**: Understanding space requirements and memory efficiency

## Expected Outcomes

After completing this assignment, students should be able to:

- Explain why Python's built-in sort (Timsort) generally outperforms other implementations
- Understand the trade-offs between different sorting algorithms
- Recognize O(n log n) scaling behavior in empirical data
- Design their own performance experiments for other algorithms
- Create publication-quality plots with proper error bars and legends

## Technologies Used

- **Python 3.11+**: Core programming language
- **Jupyter Notebook**: Interactive development environment
- **NumPy**: Numerical computing and array operations
- **Matplotlib**: Data visualization and plotting
- **memory_profiler**: Memory usage measurement
- **Statistics module**: Statistical analysis of experimental data

## Extension Ideas

For students who complete the basic assignment, consider these extensions:

1. **Additional algorithms**: Implement quicksort, heapsort, or radix sort
2. **Different data types**: Test performance with strings, objects, or custom data types
3. **Memory optimization**: Investigate in-place sorting algorithms
4. **Parallel processing**: Explore how sorting scales with multiple cores
5. **Real-world data**: Test algorithms on partially sorted or structured data

## Additional Resources

- [Big O Notation Explained](https://www.khanacademy.org/computing/computer-science/algorithms)
- [Python Sorting HOW TO](https://docs.python.org/3/howto/sorting.html)
- [Timsort Algorithm Analysis](https://en.wikipedia.org/wiki/Timsort)
- [Memory Profiling in Python](https://pypi.org/project/memory-profiler/)

## Contributing

This is an educational assignment repository. Students should:

1. Fork the repository to their own GitHub account
2. Complete the assignment in their fork
3. Submit their completed work according to bootcamp guidelines

Instructors and TAs can contribute improvements via pull requests to the main repository.

## License

This educational content is provided under the GNU GPL v3 License. See `LICENSE` file for details.

---

**Happy coding and learning! 🚀**

*Remember: The goal is not just to complete the assignment, but to understand the underlying concepts and develop skills in empirical algorithm analysis that will serve you throughout your data science career.*
