from typing import Optional
from mcp.server import FastMCP
from solana.rpc.async_api import AsyncClient
from solana.rpc.commitment import Commitment
from solana.rpc.types import TokenAccountOpts
from solders.message import Message  # type: ignore
from solders.pubkey import Pubkey  # type: ignore
from solders.signature import Signature  # type: ignore
from solders.system_program import TransferParams, transfer

mcp = FastMCP("Solana Client")
rpc_url = "https://api.mainnet-beta.solana.com"


@mcp.tool()
async def get_balance(address: str) -> str:
    """Returns the balance of the account of provided Pubkey.

    Args:
        address (str): Pubkey of account to query

    Returns:
        str: Account balance response in the format "Balance of {address}: {balance}"
    """
    async with AsyncClient(rpc_url) as client:
        balance = await client.get_balance(Pubkey.from_string(address))
        return f"Balance of {address}: {balance}"


@mcp.tool()
async def get_transaction(hash: str) -> str:
    """Returns transaction details for a confirmed transaction.

    Args:
        hash (str): Transaction signature as base-58 encoded string

    Returns:
        str: Transaction details in the format "Transaction: {transaction}"
    """
    async with AsyncClient(rpc_url) as client:
        transaction = await client.get_transaction(Signature.from_string(hash))
        return f"Transaction: {transaction}"


@mcp.tool()
async def get_block(slot: int) -> str:
    """Returns identity and transaction information about a confirmed block in the ledger.

    Args:
        slot (int): Slot number as u64 integer

    Returns:
        str: Block information in the format "Block: {block}"
    """
    async with AsyncClient(rpc_url) as client:
        block = await client.get_block(slot)
        return f"Block: {block}"


@mcp.tool()
async def get_block_height() -> str:
    """Returns the current block height of the node.

    Returns:
        str: Current block height in the format "Block height: {height}"
    """
    async with AsyncClient(rpc_url) as client:
        height = await client.get_block_height()
        return f"Block height: {height}"


@mcp.tool()
async def get_block_time(slot: int) -> str:
    """Fetch the estimated production time of a block.

    Args:
        slot (int): Block slot number

    Returns:
        str: Block time in the format "Block time: {time}"
    """
    async with AsyncClient(rpc_url) as client:
        time = await client.get_block_time(slot)
        return f"Block time: {time}"


@mcp.tool()
async def get_blocks(start_slot: int, end_slot: Optional[int] = None) -> str:
    """Returns a list of confirmed blocks between two slots.

    Args:
        start_slot (int): Start slot as u64 integer
        end_slot (Optional[int], optional): End slot as u64 integer. Defaults to None.

    Returns:
        str: List of blocks in the format "Blocks: {blocks}"
    """
    async with AsyncClient(rpc_url) as client:
        blocks = await client.get_blocks(start_slot, end_slot)
        return f"Blocks: {blocks}"


@mcp.tool()
async def get_cluster_nodes() -> str:
    """Returns information about all the nodes participating in the cluster.

    Returns:
        str: Cluster nodes information in the format "Cluster nodes: {nodes}"
    """
    async with AsyncClient(rpc_url) as client:
        nodes = await client.get_cluster_nodes()
        return f"Cluster nodes: {nodes}"


@mcp.tool()
async def get_epoch_info() -> str:
    """Returns information about the current epoch.

    Returns:
        str: Epoch information in the format "Epoch info: {info}"
    """
    async with AsyncClient(rpc_url) as client:
        info = await client.get_epoch_info()
        return f"Epoch info: {info}"


@mcp.tool()
async def get_epoch_schedule() -> str:
    """Returns epoch schedule information from this cluster's genesis config.

    Returns:
        str: Epoch schedule in the format "Epoch schedule: {schedule}"
    """
    async with AsyncClient(rpc_url) as client:
        schedule = await client.get_epoch_schedule()
        return f"Epoch schedule: {schedule}"


@mcp.tool()
async def get_genesis_hash() -> str:
    """Returns the genesis hash.

    Returns:
        str: Genesis hash in the format "Genesis hash: {hash}"
    """
    async with AsyncClient(rpc_url) as client:
        hash = await client.get_genesis_hash()
        return f"Genesis hash: {hash}"


@mcp.tool()
async def get_identity() -> str:
    """Returns the identity pubkey for the current node.

    Returns:
        str: Node identity in the format "Node identity: {identity}"
    """
    async with AsyncClient(rpc_url) as client:
        identity = await client.get_identity()
        return f"Node identity: {identity}"


@mcp.tool()
async def get_inflation_governor() -> str:
    """Returns the current inflation governor.

    Returns:
        str: Inflation governor info in the format "Inflation governor: {governor}"
    """
    async with AsyncClient(rpc_url) as client:
        governor = await client.get_inflation_governor()
        return f"Inflation governor: {governor}"


@mcp.tool()
async def get_inflation_rate() -> str:
    """Returns the specific inflation values for the current epoch.

    Returns:
        str: Inflation rate info in the format "Inflation rate: {rate}"
    """
    async with AsyncClient(rpc_url) as client:
        rate = await client.get_inflation_rate()
        return f"Inflation rate: {rate}"


@mcp.tool()
async def get_largest_accounts() -> str:
    """Returns the 20 largest accounts, by lamport balance.

    Returns:
        str: Largest accounts info in the format "Largest accounts: {accounts}"
    """
    async with AsyncClient(rpc_url) as client:
        accounts = await client.get_largest_accounts()
        return f"Largest accounts: {accounts}"


@mcp.tool()
async def get_latest_blockhash() -> str:
    """Returns the latest block hash from the ledger.

    Returns:
        str: Latest blockhash in the format "Latest blockhash: {blockhash}"
    """
    async with AsyncClient(rpc_url) as client:
        blockhash = await client.get_latest_blockhash()
        return f"Latest blockhash: {blockhash}"


@mcp.tool()
async def get_minimum_balance_for_rent_exemption(size: int) -> str:
    """Returns minimum balance required to make account rent exempt.

    Args:
        size (int): Account data length

    Returns:
        str: Minimum balance in the format "Minimum balance for rent exemption: {balance}"
    """
    async with AsyncClient(rpc_url) as client:
        balance = await client.get_minimum_balance_for_rent_exemption(size)
        return f"Minimum balance for rent exemption: {balance}"


@mcp.tool()
async def get_program_accounts(program_id: str) -> str:
    """Returns all accounts owned by the provided program Pubkey.

    Args:
        program_id (str): Pubkey of program to query

    Returns:
        str: Program accounts in the format "Program accounts: {accounts}"
    """
    async with AsyncClient(rpc_url) as client:
        accounts = await client.get_program_accounts(Pubkey.from_string(program_id))
        return f"Program accounts: {accounts}"


@mcp.tool()
async def get_recent_performance_samples(limit: Optional[int] = None) -> str:
    """Returns a list of recent performance samples, in reverse slot order.

    Args:
        limit (Optional[int], optional): Number of samples to return (maximum 720). Defaults to None.

    Returns:
        str: Performance samples in the format "Performance samples: {samples}"
    """
    async with AsyncClient(rpc_url) as client:
        samples = await client.get_recent_performance_samples(limit)
        return f"Performance samples: {samples}"


@mcp.tool()
async def get_signature_statuses(signatures: list[str]) -> str:
    """Returns the statuses of a list of signatures.

    Args:
        signatures (list[str]): List of transaction signatures to confirm

    Returns:
        str: Signature statuses in the format "Signature statuses: {statuses}"
    """
    async with AsyncClient(rpc_url) as client:
        sigs = [Signature.from_string(sig) for sig in signatures]
        statuses = await client.get_signature_statuses(sigs)
        return f"Signature statuses: {statuses}"


@mcp.tool()
async def get_slot() -> str:
    """Returns the current slot the node is processing.

    Returns:
        str: Current slot in the format "Current slot: {slot}"
    """
    async with AsyncClient(rpc_url) as client:
        slot = await client.get_slot()
        return f"Current slot: {slot}"


@mcp.tool()
async def get_slot_leader() -> str:
    """Returns the current slot leader.

    Returns:
        str: Slot leader in the format "Slot leader: {leader}"
    """
    async with AsyncClient(rpc_url) as client:
        leader = await client.get_slot_leader()
        return f"Slot leader: {leader}"


@mcp.tool()
async def get_supply() -> str:
    """Returns information about the current supply.

    Returns:
        str: Supply information in the format "Supply info: {supply}"
    """
    async with AsyncClient(rpc_url) as client:
        supply = await client.get_supply()
        return f"Supply info: {supply}"


@mcp.tool()
async def get_token_account_balance(token_account: str) -> str:
    """Returns the token balance of an SPL Token account.

    Args:
        token_account (str): Pubkey of Token account to query

    Returns:
        str: Token account balance in the format "Token account balance: {balance}"
    """
    async with AsyncClient(rpc_url) as client:
        balance = await client.get_token_account_balance(
            Pubkey.from_string(token_account)
        )
        return f"Token account balance: {balance}"


@mcp.tool()
async def get_token_largest_accounts(mint: str) -> str:
    """Returns the 20 largest accounts of a particular SPL Token type.

    Args:
        mint (str): Pubkey of token mint to query

    Returns:
        str: Largest token accounts in the format "Largest token accounts: {accounts}"
    """
    async with AsyncClient(rpc_url) as client:
        accounts = await client.get_token_largest_accounts(Pubkey.from_string(mint))
        return f"Largest token accounts: {accounts}"


@mcp.tool()
async def get_transaction_count() -> str:
    """Returns the current Transaction count from the ledger.

    Returns:
        str: Transaction count in the format "Transaction count: {count}"
    """
    async with AsyncClient(rpc_url) as client:
        count = await client.get_transaction_count()
        return f"Transaction count: {count}"


@mcp.tool()
async def get_version() -> str:
    """Returns the current solana versions running on the node.

    Returns:
        str: Version information in the format "Version info: {version}"
    """
    async with AsyncClient(rpc_url) as client:
        version = await client.get_version()
        return f"Version info: {version}"


@mcp.tool()
async def get_vote_accounts() -> str:
    """Returns the account info and associated stake for all the voting accounts in the current bank.

    Returns:
        str: Vote accounts information in the format "Vote accounts: {accounts}"
    """
    async with AsyncClient(rpc_url) as client:
        accounts = await client.get_vote_accounts()
        return f"Vote accounts: {accounts}"


@mcp.tool()
async def is_connected() -> str:
    """Health check to verify if the client is connected.

    Returns:
        str: Connection status in the format "Connected: {connected}"
    """
    async with AsyncClient(rpc_url) as client:
        connected = await client.is_connected()
        return f"Connected: {connected}"


@mcp.tool()
async def get_block_commitment(slot: int) -> str:
    """Fetch the commitment for particular block.

    Args:
        slot (int): Block slot number to query

    Returns:
        str: Block commitment information
    """
    async with AsyncClient(rpc_url) as client:
        commitment = await client.get_block_commitment(slot)
        return f"Block commitment: {commitment}"


@mcp.tool()
async def confirm_transaction(tx_sig: str, commitment: Optional[str] = None) -> str:
    """Confirm the transaction identified by the specified signature.

    Args:
        tx_sig (str): Transaction signature to confirm
        commitment (Optional[str]): Bank state to query ("finalized", "confirmed" or "processed")

    Returns:
        str: Transaction confirmation status
    """
    async with AsyncClient(rpc_url) as client:
        result = await client.confirm_transaction(
            Signature.from_string(tx_sig),
            Commitment(commitment) if commitment else None,
        )
        return f"Transaction confirmation: {result}"


@mcp.tool()
async def get_account_info(pubkey: str, encoding: str = "base64") -> str:
    """Returns all account info for the specified public key.

    Args:
        pubkey (str): Pubkey of account to query
        encoding (str): Encoding for Account data ("base58", "base64", or "jsonParsed")

    Returns:
        str: Account information
    """
    async with AsyncClient(rpc_url) as client:
        info = await client.get_account_info(
            Pubkey.from_string(pubkey), encoding=encoding
        )
        return f"Account info: {info}"


@mcp.tool()
async def get_fee_for_message(from_pubkey: str, to_pubkey: str, lamports: int) -> str:
    """Returns the fee for a message.

    Args:
        from_pubkey (str): Sender's public key
        to_pubkey (str): Recipient's public key
        lamports (int): Amount of lamports to transfer

    Returns:
        str: Fee information
    """
    async with AsyncClient(rpc_url) as client:
        msg = Message(
            [
                transfer(
                    TransferParams(
                        from_pubkey=Pubkey.from_string(from_pubkey),
                        to_pubkey=Pubkey.from_string(to_pubkey),
                        lamports=lamports,
                    )
                )
            ]
        )
        fee = await client.get_fee_for_message(msg)
        return f"Message fee: {fee}"


@mcp.tool()
async def get_first_available_block() -> str:
    """Returns the slot of the lowest confirmed block available.

    Returns:
        str: First available block information
    """
    async with AsyncClient(rpc_url) as client:
        block = await client.get_first_available_block()
        return f"First available block: {block}"


@mcp.tool()
async def get_inflation_reward(pubkeys: list[str], epoch: Optional[int] = None) -> str:
    """Returns the inflation/staking reward for a list of addresses for an epoch.

    Args:
        pubkeys (list[str]): List of account addresses
        epoch (Optional[int]): Epoch for which to calculate rewards

    Returns:
        str: Inflation reward information
    """
    async with AsyncClient(rpc_url) as client:
        pks = [Pubkey.from_string(pk) for pk in pubkeys]
        rewards = await client.get_inflation_reward(pks, epoch)
        return f"Inflation rewards: {rewards}"


@mcp.tool()
async def get_leader_schedule(epoch: Optional[int] = None) -> str:
    """Returns the leader schedule for an epoch.

    Args:
        epoch (Optional[int]): Epoch to get schedule for

    Returns:
        str: Leader schedule information
    """
    async with AsyncClient(rpc_url) as client:
        schedule = await client.get_leader_schedule(epoch)
        return f"Leader schedule: {schedule}"


@mcp.tool()
async def get_minimum_ledger_slot() -> str:
    """Returns the lowest slot that the node has information about in its ledger.

    Returns:
        str: Minimum ledger slot information
    """
    async with AsyncClient(rpc_url) as client:
        slot = await client.get_minimum_ledger_slot()
        return f"Minimum ledger slot: {slot}"


@mcp.tool()
async def get_multiple_accounts(pubkeys: list[str], encoding: str = "base64") -> str:
    """Returns the account information for a list of public keys.

    Args:
        pubkeys (list[str]): List of account public keys
        encoding (str): Encoding for the account data

    Returns:
        str: Multiple accounts information
    """
    async with AsyncClient(rpc_url) as client:
        pks = [Pubkey.from_string(pk) for pk in pubkeys]
        accounts = await client.get_multiple_accounts(pks, encoding=encoding)
        return f"Multiple accounts info: {accounts}"


@mcp.tool()
async def get_signatures_for_address(
    account: str,
    before: Optional[str] = None,
    until: Optional[str] = None,
    limit: Optional[int] = None,
) -> str:
    """Returns confirmed signatures for transactions involving an address.

    Args:
        account (str): Account address to query
        before (Optional[str]): Start searching backwards from this signature
        until (Optional[str]): Search until this signature
        limit (Optional[int]): Maximum number of signatures to return

    Returns:
        str: Signatures information
    """
    async with AsyncClient(rpc_url) as client:
        sigs = await client.get_signatures_for_address(
            Pubkey.from_string(account),
            before=Signature.from_string(before) if before else None,
            until=Signature.from_string(until) if until else None,
            limit=limit,
        )
        return f"Signatures for address: {sigs}"


@mcp.tool()
async def get_token_accounts_by_delegate(delegate: str, mint: str) -> str:
    """Returns all SPL Token accounts by approved delegate.

    Args:
        delegate (str): Public key of delegate owner
        mint (str): Token mint address

    Returns:
        str: Token accounts information
    """
    async with AsyncClient(rpc_url) as client:
        accounts = await client.get_token_accounts_by_delegate(
            Pubkey.from_string(delegate), TokenAccountOpts(Pubkey.from_string(mint))
        )
        return f"Token accounts by delegate: {accounts}"


@mcp.tool()
async def get_token_accounts_by_owner(owner: str, mint: str) -> str:
    """Returns all SPL Token accounts by token owner.

    Args:
        owner (str): Public key of token owner
        mint (str): Token mint address

    Returns:
        str: Token accounts information
    """
    async with AsyncClient(rpc_url) as client:
        accounts = await client.get_token_accounts_by_owner(
            Pubkey.from_string(owner), TokenAccountOpts(Pubkey.from_string(mint))
        )
        return f"Token accounts by owner: {accounts}"


@mcp.tool()
async def get_token_supply(mint: str) -> str:
    """Returns the total supply of an SPL Token type.

    Args:
        mint (str): Public key of token mint

    Returns:
        str: Token supply information
    """
    async with AsyncClient(rpc_url) as client:
        supply = await client.get_token_supply(Pubkey.from_string(mint))
        return f"Token supply: {supply}"


@mcp.tool()
async def request_airdrop(address: str, lamports: int) -> str:
    """Request an airdrop of lamports to a Pubkey.

    Args:
        address (str): Public key of recipient
        lamports (int): Amount of lamports to request

    Returns:
        str: Airdrop request result
    """
    async with AsyncClient(rpc_url) as client:
        result = await client.request_airdrop(Pubkey.from_string(address), lamports)
        return f"Airdrop request: {result}"


@mcp.tool()
async def send_transaction(txn: bytes) -> str:
    """Send a transaction that has already been signed and serialized into the wire format.

    Args:
        txn (bytes): Signed transaction as bytes

    Returns:
        str: Transaction send result
    """
    async with AsyncClient(rpc_url) as client:
        result = await client.send_raw_transaction(txn)
        return f"Transaction sent: {result}"


@mcp.tool()
async def validator_exit() -> str:
    """Request to have the validator exit.

    Returns:
        str: Validator exit request result
    """
    async with AsyncClient(rpc_url) as client:
        result = await client.validator_exit()
        return f"Validator exit request: {result}"
