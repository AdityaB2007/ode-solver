# Numerical ODE Solver in Python

A Python project implementing and analyzing numerical methods for solving first-order ordinary differential equations (ODEs) from scratch.

## Methods Implemented
- Euler's Method
- Heun's Method (Improved Euler)
- Classical Runge-Kutta 4 (RK4)

## Features
- Modular, reusable solver implementations
- Error analysis compared to exact solutions
- Visualization of solution accuracy and behavior
- Example problems with varying dynamics
- Unit testing using pytest

## Example Problems
This project includes experiments on:
- Exponential growth: y' = y, y(0) = 1  
- Logistic growth: y' = y(1 - y), y(0) = 0.1  

These examples are used to compare method accuracy and observe how step size affects numerical stability and error.

## Key Insights
- Euler’s method accumulates significant error for larger step sizes  
- Heun’s method improves accuracy by incorporating slope correction  
- RK4 provides significantly higher accuracy with modest computational cost  
- Step size plays a critical role in stability and convergence  

## Project Structure
```text
ode-solver/
├── ode_solver/
│   ├── __init__.py
│   ├── euler.py
│   ├── heun.py
│   ├── rk4.py
│   ├── analysis.py
│   └── utils.py
├── examples/
│   ├── exponential_growth.py
│   └── logistic_growth.py
├── tests/
│   └── test_solvers.py
├── README.md
├── requirements.txt
└── main.py
```

## Installation
```bash
pip install -r requirements.txt
```

## Run
```bash
python main.py
```

## Test
```bash
pytest
```

## Motivation
This project was built to bridge mathematical understanding of differential equations with practical implementation. It focuses not only on coding the methods, but also on analyzing their behavior, accuracy, and limitations.
