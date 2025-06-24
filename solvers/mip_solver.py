from pulp import LpProblem, LpMaximize, LpVariable, lpSum, LpBinary
from core.trade_intent import TradeIntent
from typing import List, Tuple
from .base_solver import BaseSolver

class MiPSolver(BaseSolver):
    def solve(self, intents: List[TradeIntent]) -> List[Tuple[TradeIntent, TradeIntent]]:
        matches = []
        n = len(intents)
        prob = LpProblem("Matching", LpMaximize)

        x = {}
        for i in range(n):
            for j in range(i + 1, n):
                a, b = intents[i], intents[j]
                if a.from_token == b.to_token and a.to_token == b.from_token:
                    x[(i, j)] = LpVariable(f"x_{i}_{j}", cat=LpBinary)

        prob += lpSum(x.values()), "Maximize matches"

        for i in range(n):
            prob += lpSum(x[j, i] for j, k in x if k == i) + lpSum(x[i, k] for j, k in x if j == i) <= 1

        prob.solve()

        for (i, j), var in x.items():
            if var.value() == 1:
                matches.append((intents[i], intents[j]))
                # Adding a print statement to show the matched pairs clearly
                print(f"Matched pair: {intents[i].from_amount} {intents[i].from_token} → {intents[i].to_token} "
                      f"with {intents[j].from_amount} {intents[j].from_token} → {intents[j].to_token}")

        return matches
