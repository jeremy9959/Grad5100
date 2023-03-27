# Grad 5100: Fundamentals of Data Science

## Introduction

Grad 5100 is a foundational course in the MS in Data Science Program. It is designed to provide
the essential background in programming, statistics, linear algebra, and multivariate calculus
that the core and elective courses in the program rely on. The course will run intensively during
the first few weeks of the semester and then drop back to a regular weekly schedule.

## References

We will rely on the following materials.

- [The anaconda machine learning environment for python and associated libraries](http://www.anaconda.com)
- [The R language, Rstudio IDE, and associated libraries](https://posit.co/download/rstudio-desktop)
- [The VScode IDE](https://code.visualstudio.com)

There is no formal textbook for the course. Some useful references include the following, all of which
are either open source or available through the UConn Library.

- [An Introduction to Statistical Learning](http://www.statlearning.com) by James, _et. al._ Note that the original
  version of this book uses the R language, but a new edition available in Summer 2023 uses Python.
- [R for Data Science](https://r4ds.hadley.nz/) by Wickham and Grolemund.
- [Python for Data Science, 3E](https://wesmckinney.com/book) by Wes McKinney.
- _Practical Statistics for Data Scientists_ by Bruce, Bruce, and Gedeck. Note that this is available for free to UConn students through the UConn library's subscription to the O'Reilly Learning Platform.
- _Statistical Practice for Data Science_ by Bar, Ravishankar, and Asha (draft).
- [Mathematics for Machine Learning](https://jeremy9959.net/Mathematics-for-Machine-Learning) (draft) by Teitelbaum.
- _Fluent Python_ by Ramalho. Available to UConn students through the UConn Library's subscription to the O'Reilly Learning Platform.

More advanced technical references include:

- [The Elements of Statistical Learning](https://hastie.su.domains/ElemStatLearn) by Hastie, _et. al._
- [Pattern Recognition and Machine Learning](https://www.microsoft.com/en-us/research/uploads/prod/2006/01/Bishop-Pattern-Recognition-and-Machine-Learning-2006.pdf) by Bishop

## Assessment

Course grades will be based on:

- biweekly homework assignments (60 %)
- a take home final exam (40 %)

## Disclaimer

The instructor reserves the right to modify or adapt this syllabus to account for disruption due to COVID-19 or other
unexpected circumstances.

## University Policies

Students with disabilities should work with the [Center for Students with Disabilities](https://csd.uconn.edu) to request academic accommodations. The CSD is located in Wilbur Cross, Room 204 and can be reached at (860)-486-2020 or at csd@uconn.edu.

Students are bound by the university's policies on academic misconduct. Academic misconduct is dishonest or unethical behavior that includes but is not limited to misrepresenting mastery in an academic area (e.g. cheating), failing to properly credit information, research, or ideas to their rightful originators or representing such information, research, or ideas as your own (e.g. plagiarism).

Students, faculty, and staff are bound by the university's [policy against discrimination, harassment, and related interpersonal violence.](https://policy.uconn.edu/2015/12/29/policy-against-discrimination-harassment-and-related-interpersonal-violence/)

<div style="page-break-after: always"></div>

# Week by Week Schedule

## Week 1 Setting up a data science working environment

- Key tools:
  - the anaconda environment
  - vscode
  - Rstudio
- Projects
  - projects, files, directories
  - the terminal
  - self documenting code
    - jupyter notebooks, markdown, and R markdown
  - essentials of REPL python in jupyter
    - numeric variables, arithmetic, scientific functions;
    - lists and arrays; indexing and slicing; vectorization
  - basics of R
    - datatypes, arrays, arithmetic, slicing and indexing, vectorization
  - a minimal introduction to plotting in R and Python

## Week 2 Probability and Statistics: a first look at the normal distribution

- Working with normally distributed populations
  - Events and Outcomes
  - The Normal Distribution
    - probability mass functions and area under the curve
  - Mean and Variance
  - Hypothesis testing
    - sampling from a univariate normal distribution
    - Null and alternative hypotheses
    - p-values, statistical significance and confidence intervals (for univariate normally distributed populations)
  - illustrated with examples in R and Python

## Week 3 Programming with Data in R and Python

- Key tools
  - R dataframes and the tidyverse
  - Numpy and Pandas
  - functions in R and Python
- working with files and I/O in R and Python
- pandas Series and dataframe basics (reading files, indices, selecting, summarizing data)
- R factors and dataframes (reading files, indices, selecting, summarizing)

## Week 4 Discrete Probability and Bayes Theorem

- Discrete probability;
  - events and outcomes;
  - mean and variance
  - independent events;
  - conditional probability and Bayes theorem in the discrete case
  - bernoulli and binomial distributions
  - false positives, false negatives, versions of the base rate fallacy
  - discusssion of the Naive Bayes spam filter (?)
  - illustrated with R and Python examples

## Week 5 Slicing and dicing data in R and Python

- One day on pandas grouping, summarizing, selecting data
- One day on R grouping, summarizing, selecting data (tidyverse)

## Week 6 Linear Algebra

- Geometry of n-dimensional space, vectors, addition and scalar multiplication of vectors, the dot product, orthogonality
- Matrices, matrix multiplication, column space of a matrix
- Ordinary Least Squares as an illustration(?) of geometry and linear algebra
- computational examples in both R and Python (numpy)

## Week 7-8 Multivariate calculus

- discussion of functions of several variables:
  - graphs of functions
  - contour graphs and level surfaces
- review of the derivative in one dimension; rates of change
- partial derivatives
- directional derivatives and the gradient
- relationship of the gradient to the level curves
- Use of calculus to solve the OLS problem done by linear algebra in week 5 (exact solution)
- Use of gradient descent to solve OLS problem
- includes programming examples for gradient descent in the least squares case

## Week 9 A deeper dive into Visualization

- more on ggplot and its capabilities
- python plotting packages (seaborn? bokeh?)

## Week 10 Statistical models

- What is a statistical model?
- Likelihood and model parameters
- Maximum likelihood estimation and gradient descent
- Illustrated with OLS and Logistic Regression?

## Week 11-12 More on Statistics

- Another look at the normal distribution; the multivariate normal
- covariance, correlation
- estimation of parameters for linear regression and logistic regression
- significance and confidence intervals
- null and alternative hypotheses
- p-values

## Week 13 Version Control

- Git as a tool (command line and through R studio)
- commits, branches
- remotes and github
- using github to host a web page for a project
- collaboration using Git -- pull requests; contributing to open source projects

## Week 14 Advanced topics in programming

- Data structures; object oriented concepts
- Essential notions from data structures:
  - stacks, lists, hashing
- Python classes
  - data attributes and methods

## Week 14 Databases

- What is a relational database? tables, keys, indices, joins
- Basic SQL for getting data from a database
