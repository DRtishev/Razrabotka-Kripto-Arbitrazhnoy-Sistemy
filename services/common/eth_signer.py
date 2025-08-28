import os


def load_private_key():
    """Load the Ethereum private key from environment variables."""
    return os.environ.get("ETH_PRIVATE_KEY", "")


def build_eip1559_tx(to, value, gas, gas_price, nonce, chain_id):
    """Build a simple EIP-1559 transaction dict."""
    return {
        "to": to,
        "value": value,
        "gas": gas,
        "maxFeePerGas": gas_price,
        "maxPriorityFeePerGas": gas_price,
        "nonce": nonce,
        "chainId": chain_id,
        "type": 2
    }


def sign_transaction(private_key, tx_dict):
    """Sign a transaction (placeholder)."""
    # TODO: integrate with eth_account or another lib
    return f"signed_tx_for_{tx_dict['to']}"


def send_flashbots_bundle(signed_tx, rpc_url):
    """Send a transaction bundle to Flashbots (placeholder)."""
    print(f"Sending signed tx to {rpc_url}: {signed_tx}")
