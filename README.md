# Numerical ODE Solver in Python

A Python project implementing numerical methods for solving first-order ordinary differential equations from scratch.

## Methods Implemented
- Euler's Method
- Heun's Method (Improved Euler)
- Classical Runge-Kutta 4 (RK4)

## Features
- Reusable solver functions
- Error analysis against exact solutions
- Example problems
- Visualization with matplotlib
- Basic testing with pytest

## Example Problem
This repo includes experiments on:
- The exponential growth equation: y' = y, y(0) = 1
- The logistic growth equation: y' = y(1-y), y(0) = 0.1

## Project Structure
```text
numerical-ode-solvers/
├── ode_solver/
├── examples/
├── tests/
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
This project was built to connect mathematical understanding of differential equations and numerical analysis with practical Python implementation.
