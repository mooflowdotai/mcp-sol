from mcp.server import FastMCP
from solana.rpc.async_api import AsyncClient
from solders.pubkey import Pubkey  # type: ignore
from solders.signature import Signature  # type: ignore

mcp = FastMCP("Solana Client")
rpc_url = "https://api.mainnet-beta.solana.com"


@mcp.tool()
async def get_balance(address: str) -> str:
    async with AsyncClient(rpc_url) as client:
        balance = await client.get_balance(Pubkey.from_string(address))
        return f"Balance of {address}: {balance}"


@mcp.tool()
async def get_transaction(hash: str) -> str:
    async with AsyncClient(rpc_url) as client:
        transaction = await client.get_transaction(Signature.from_string(hash))
        return f"Transaction: {transaction}"


@mcp.tool()
async def get_block(slot: int) -> str:
    async with AsyncClient(rpc_url) as client:
        block = await client.get_block(slot)
        return f"Block: {block}"
