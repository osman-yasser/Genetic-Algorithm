# Genetic Algorithm for Function Optimization

This repository contains an implementation of a genetic algorithm for optimizing the function **Y(x) = √x, where 1 ≤ x ≤ 16**. The genetic algorithm aims to minimize the value of the function by evolving a population of candidate solutions over multiple generations.

## Function Description

The function Y(x) = √x represents a mathematical function that calculates the square root of the input value x. The function is defined for values of x in the range [1, 16].

## Genetic Algorithm

The genetic algorithm is a search and optimization technique inspired by the process of natural selection. It operates on a population of candidate solutions and applies genetic operators such as selection, crossover, and mutation to evolve the population towards better solutions.

The implementation of the genetic algorithm consists of the following steps:

1. Initialization: The population of candidate solutions is initialized with random values within the defined range [1, 16].

2. Fitness Evaluation: The fitness of each candidate solution is evaluated using the function Y(x) = √x. The fitness represents the quality or suitability of a solution.

3. Selection: The selection step uses the roulette wheel selection method to choose candidate solutions based on their fitness. Solutions with higher fitness have a higher chance of being selected for reproduction.

4. Crossover: Crossover is applied to the selected solutions to create offspring. Intermediate recombination is used, where a random value is generated between -0.25 and 1.24 to determine the crossover point between two parents.

5. Mutation: Mutation is performed on the offspring solutions with a probability of pm. If a solution is selected for mutation, a random value within the defined range [1, 16] is generated and replaces the original value.

6. Replacement: The offspring solutions replace a portion of the population based on elitism. The best solutions from the current population and offspring are preserved, ensuring that the overall fitness improves.

7. Iteration: Steps 2-6 are repeated for multiple generations until the termination condition is met. In this implementation, the algorithm iterates for 100,000,000 generations.

## Usage

To run the code, ensure you have a Python environment set up and execute the `main.py` script.

```bash
python main.py
```

## License

This code is provided under the [MIT License](LICENSE).

Feel free to explore, modify, and use this implementation according to the terms of the license.


Feel free to modify the README.md file to suit your specific needs and add any additional sections or information as required.