# Cow Solver Simulation

This project simulates the **Cow Protocol** using two solvers: **MiP Solver** (Mixed Integer Programming) and **Quasi-Linear Solver (Quasimodo)**, to optimize trade pair matching between cryptocurrencies, focusing on the USDC/ETH pair.

The solvers evaluate **trade orders** in batches, solving them using the **CBC MILP solver** (for MiP Solver) and the custom Quasi-Linear Solver, and match the most optimal trade pairs to maximize the objective value.

## Installation

This project has several dependencies that you need to install. These dependencies are listed in the `requirements.txt` file.

To install them, run the following command:

*`pip install -r requirements.txt`*

After running the above command, ensure that everything is installed correctly by checking the installed libraries:

*`pip list`*

You should see libraries like `pulp` and `cbc` in the list.

## Running the Simulation

Once you've installed the dependencies, you can run the simulation using the following command:

*`python main.py --solver <solver_name>`*

Where `<solver_name>` can be either:
- `mip`: To use the MiP Solver (Mixed Integer Programming Solver).
- `quasi_linear`: To use the Quasi Linear Solver.

For example, to run the simulation using the MiP Solver:

*`python main.py --solver mip`*

## Trade Intents

The function `generate_trade_intents` generates random trade intents, which are the orders that the solvers try to match. Each `TradeIntent` consists of the following:

- `from_token`: The cryptocurrency being traded (e.g., USDC).
- `to_token`: The cryptocurrency being received (e.g., ETH).
- `from_amount`: The amount of the `from_token` to trade.
- `to_amount`: The amount of the `to_token` that will be received.

**Exchange Rate:** The exchange rate used is fixed at 1 ETH = 3000 USDC.

## Solvers

### MiPSolver

The `MiPSolver` uses **Mixed Integer Programming (MIP)** to solve the optimization problem. It creates binary decision variables for each possible trade pair and tries to maximize the number of optimal matches between trade intents.

### QuasiLinearSolver

The `QuasiLinearSolver` uses a **heuristic method** to find the most optimal matches between trade pairs. It iterates over trade intents, calculating price differences, and matches the closest pairs.

## Running the Solver

The solvers iterate through batches of trade intents, solve the optimization problem, and print the matched trade pairs.
