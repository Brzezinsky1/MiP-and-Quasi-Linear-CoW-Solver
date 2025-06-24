import random
from typing import List

class TradeIntent:
    def __init__(self, from_token: str, to_token: str, from_amount: float, to_amount: float):
        self.from_token = from_token
        self.to_token = to_token
        self.from_amount = from_amount
        self.to_amount = to_amount

    @property
    def expected_return(self):
        return self.to_amount


def generate_trade_intents(min_intents: int, max_intents: int) -> List[TradeIntent]:
    pairs = [("USDC", "ETH"), ("ETH", "USDC")]
    n = random.randint(min_intents, max_intents)
    intents = []

    for _ in range(n):
        from_token, to_token = random.choice(pairs)
        from_amount = round(random.uniform(10, 1000), 2)

        # fixed exchange rate: 1 ETH = 3000 USDC
        if from_token == "USDC":
            to_amount = round(from_amount / 3000, 6)
        else:
            to_amount = round(from_amount * 3000, 2)

        intents.append(TradeIntent(from_token, to_token, from_amount, to_amount))

    return intents
