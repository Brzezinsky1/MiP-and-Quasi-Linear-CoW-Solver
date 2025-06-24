from typing import List, Tuple
from core.trade_intent import TradeIntent
from .base_solver import BaseSolver

class QuasiLinearSolver(BaseSolver):
    def solve(self, intents: List[TradeIntent]) -> List[Tuple[TradeIntent, TradeIntent]]:
        matches = []
        used = set()

        for i, a in enumerate(intents):
            if i in used:
                continue
            best_match = None
            best_diff = float("inf")

            for j, b in enumerate(intents):
                if j in used or i == j:
                    continue
                if a.from_token != b.to_token or a.to_token != b.from_token:
                    continue

                price_a = a.to_amount / a.from_amount
                price_b = b.from_amount / b.to_amount
                diff = abs(price_a - price_b)

                if diff < best_diff:
                    best_diff = diff
                    best_match = j

            if best_match is not None:
                matches.append((a, intents[best_match]))
                used.add(i)
                used.add(best_match)
                # Adding a print statement to show the matched pairs clearly
                print(f"Matched pair: {a.from_amount} {a.from_token} → {a.to_token} "
                      f"with {intents[best_match].from_amount} {intents[best_match].from_token} → {intents[best_match].to_token}")

        return matches
