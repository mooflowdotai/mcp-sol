import asyncio
from solana.rpc.async_api import AsyncClient
from solders.signature import Signature


async def main():
    hash = "test"
    async with AsyncClient("http://explorer.solana.com") as client:
        transaction = await client.get_transaction(Signature.from_string(hash))
        return f"Transaction: {transaction}"


if __name__ == "__main__":
    asyncio.run(main())
