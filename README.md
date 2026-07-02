# NucME

NucME is a computational mechanics project where I have used Python to implement different numerical methods that were taught in different courses in a different semester in my mechanical engineering program.

- Math 4511: Numerical Analysis
- ME 4637: Computational Mechanics

## Technology

- Coding: Python
- Documentation: Markdown

## Methods

- Approximation
  - Taylor’s Series

- Bracketing Methods
  - Bisection Method
  - False Position Method

- Open Methods
  - Secant Method
  - Newton-Raphson Method
  - Simple Fixed-Point Iteration Method

- Gauss Elimination
  - Naive Gauss Elimination
  - Gauss-Jordan Elimination

- LU Decomposition and Matrix Inversion
  - LU Decomposition
  - The Matrix Inverse

- Optimization
  - One-Dimensional Unconstrained Optimization
    - Newton’s Method
    - Golden Section Search
    - Parabolic Interpolation

  - Multi-Dimensional Unconstrained Optimization
    - Gradient Method

- Interpolation
  - Spline Interpolation
  - Lagrange Interpolating Polynomials
  - Newton’s Divide-Difference Interpolating Polynomials

- Newton-Cotes Integration Formulas
  - Simpson’s Rule
  - Trapezoidal Rule
  - Integration with Unequal Segments

- Runge-Kutta Methods
  - Euler’s Method
    - Explicit Euler
    - Implicit Euler

  - Runge-Kutta Method

## Effective Use of AI

Yeah, the artificial intelligence (AI) has also been used in this project. But, as in my previous project, here, I also used them cautiously. As all of the methods were taught in our lab, I had a clear understanding of what to do next. Still, if I was stuck at one point for quite a long time, then I asked different LLMs to help me answer my questions.

## Project Structure

<!-- readme-tree start -->
```
.
├── .github
│   └── workflows
│       ├── Auto_Tree.yaml
│       └── Auto_Tree.yaml:Zone.Identifier
├── .gitignore
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── LICENSE
├── Methods
│   ├── 01_Approximation
│   │   └── 01_Taylors_Series
│   │       ├── 01_Taylors_Series.md
│   │       └── 01_Taylors_Series.py
│   ├── 01_Taylor's_Series.py
│   ├── 02_Bisection_Method.py
│   ├── 02_Bracketing_Methods
│   │   ├── 01_Bisection_Method
│   │   │   ├── 01_Bisection_Method.md
│   │   │   └── 01_Bisection_Method.py
│   │   └── 02_False_Position_Method
│   │       ├── 02_False_Position_Method.md
│   │       └── 02_False_Position_Method.py
│   ├── 03_False_Position_Method.py
│   ├── 03_Open_Methods
│   │   ├── 01_Secant_Method
│   │   │   ├── 01_Secant_Method.md
│   │   │   └── 01_Secant_Method.py
│   │   ├── 02_Newton-Raphson_Method
│   │   │   ├── 02_Newton-Raphson_Method.md
│   │   │   └── 02_Newton-Raphson_Method.py
│   │   └── 03_Simple_Fixed-Point_Iteration_Method
│   │       ├── 03_Simple_Fixed-Point_Iteration_Method.md
│   │       └── 03_Simple_Fixed-Point_Iteration_Method.py
│   ├── 04_Gauss_Elimination
│   │   ├── 01_Naive_Gauss_Elimination
│   │   │   ├── 01_Naive_Gauss_Elimination.md
│   │   │   └── 01_Naive_Gauss_Elimination.py
│   │   └── 02_Gauss_Jordan_Elimination
│   │       ├── 02_Gauss_Jordan_Elimination.md
│   │       └── 02_Gauss_Jordan_Elimination.py
│   ├── 04_Newton_Raphson_Method.ipynb
│   ├── 05_Explicit_Euler_Method.ipynb
│   ├── 05_LU_Decomposition_and_Matrix_Inversion
│   │   ├── 01_LU_Decomposition
│   │   │   ├── 01_LU_Decomposition.md
│   │   │   └── 01_LU_Decomposition.py
│   │   └── 02_The_Matrix_Inverse
│   │       ├── 02_The_Matrix_Inverse.md
│   │       └── 02_The_Matrix_Inverse.py
│   ├── 06_Implicit_Euler_Method.ipynb
│   ├── 06_Optimization
│   │   ├── 01_One-Dimensional_Unconstrained_Optimization
│   │   │   ├── 01_Newtons_Method
│   │   │   │   ├── 01_Newtons_Method.md
│   │   │   │   └── 01_Newtons_Method.py
│   │   │   ├── 02_Golden_Section_Search
│   │   │   │   ├── 02_Golden_Section_Search.md
│   │   │   │   └── 02_Golden_Section_Search.py
│   │   │   └── 03_Parabolic_Interpolation
│   │   │       ├── 03_Parabolic_Interpolation.md
│   │   │       └── 03_Parabolic_Interpolation.py
│   │   └── 02_Multi-Dimensional_Unconstrained_Optimization
│   │       └── 01_Gradient_Method
│   │           ├── 01_Gradient_Method.md
│   │           └── 01_Gradient_Method.py
│   ├── 07_Interpolation
│   │   ├── 01_Spline_Interpolation
│   │   │   ├── 01_Spline_Interpolation.md
│   │   │   └── 01_Spline_Interpolation.py
│   │   ├── 02_Lagrange_Interpolating_Polynomials
│   │   │   ├── 02_Lagrange_Interpolating_Polynomials.md
│   │   │   └── 02_Lagrange_Interpolating_Polynomials.py
│   │   └── 03_Newtons_Divide-Difference_Interpolating_Polynomials
│   │       ├── 03_Newtons_Divide-Difference_Interpolating_Polynomials.md
│   │       └── 03_Newtons_Divide-Difference_Interpolating_Polynomials.py
│   ├── 07_Simple_Fixed_Point_Iteration_Method.py
│   ├── 08_Newton-Cotes_Integration_Formulas
│   │   ├── 01_Simpsons_Rule
│   │   │   ├── 01_Simpsons_Rule.md
│   │   │   └── 01_Simpsons_Rule.py
│   │   ├── 02_Trapezoidal_Rule
│   │   │   ├── 02_Trapezoidal_Rule.md
│   │   │   └── 02_Trapezoidal_Rule.py
│   │   └── 03_Integration_with_Unequal_Segments
│   │       ├── 03_Integration_with_Unequal_Segments.md
│   │       └── 03_Integration_with_Unequal_Segments.py
│   ├── 09_Runge-Kutta_Methods
│   │   ├── 01_Eulers_Method
│   │   │   ├── 01_Explicit_Euler
│   │   │   │   ├── 01_Explicit_Euler.md
│   │   │   │   └── 01_Explicit_Euler.py
│   │   │   └── 02_Implicit_Euler
│   │   │       ├── 02_Implicit_Euler.md
│   │   │       └── 02_Implicit_Euler.py
│   │   └── 02_Runge-Kutta_Method
│   │       ├── 02_Runge-Kutta_Method.md
│   │       └── 02_Runge-Kutta_Method.py
│   └── approximate_sin_using_taylor_polynomials.ipynb
├── README.md
├── fluid-mechanics
│   ├── __marimo__
│   │   └── session
│   │       ├── streamline_pathline_streakline.py.json
│   │       └── velocity_field_visualization.py.json
│   ├── acceleration_vector_field.png
│   ├── field_variables_visualization.py
│   ├── streamline_pathline_streakline.py
│   ├── streamlines_of_2D_flow.png
│   └── velocity_vector_field.png
├── test
│   ├── __marimo__
│   │   └── session
│   │       └── lab_test_01.py.json
│   ├── lab_test_01.py
│   └── newton_method_for_root_approximation.py
└── tree.bak

45 directories, 72 files
```
<!-- readme-tree end -->
