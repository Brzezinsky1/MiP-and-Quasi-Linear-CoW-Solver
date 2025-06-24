import argparse
from core.trade_intent import generate_trade_intents
from solvers.mip_solver import MiPSolver
from solvers.quasi_linear_solver import QuasiLinearSolver

BATCHES = 10
INTENTS_PER_BATCH = (4, 8)

def run_simulation(solver_name: str):
    if solver_name == "mip":
        solver = MiPSolver()
        print("\n=== Running simulation with MiPSolver ===\n")
    elif solver_name == "quasi_linear":
        solver = QuasiLinearSolver()
        print("\n=== Running simulation with QuasiLinearSolver ===\n")
    else:
        raise ValueError(f"Unknown solver: {solver_name}")

    total_matched = 0

    for batch in range(1, BATCHES + 1):
        print(f"=== Batch {batch} ===")
        intents = generate_trade_intents(*INTENTS_PER_BATCH)
        print(f"Generated {len(intents)} trade intents:")
        for idx, intent in enumerate(intents, 1):
            print(f"  Intent {idx}: {intent.from_amount:.2f} {intent.from_token} → {intent.to_token} (exp {intent.expected_return:.6f})")

        matches = solver.solve(intents)

        print(f"\nMatched {len(matches)} pairs:")
        for a, b in matches:
            print(f"  {a.from_token}→{a.to_token} matched with {b.from_token}→{b.to_token}")
        print()

        total_matched += len(matches)

    print(f"--- Auction Summary ---")
    print(f"Total matched pairs: {total_matched}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--solver", type=str, default="mip", help="Which solver to use: mip or quasi_linear")
    args = parser.parse_args()

    run_simulation(args.solver)
