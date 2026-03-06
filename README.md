# Aster MCP Server

[![GitHub](https://img.shields.io/badge/GitHub-asterdex%2Faster--mcp-blue)](https://github.com/asterdex/aster-mcp)

An [Model Context Protocol](https://modelcontextprotocol.io/) server for **Aster Futures and Spot** APIs, enabling AI agents (e.g. Cursor, Claude, LangChain) to securely query market data, place orders, and check positions and accounts.

## Features

- **Config & security**: Multi-account, local Fernet-encrypted API key storage (`~/.config/aster-mcp/`)
- **Auth**: **HMAC** (API Key/Secret) and **V3 key signing** (EIP-712, user/signer/private_key; see [aster-finance-futures-api-v3](https://github.com/asterdex/api-docs/blob/master/aster-finance-futures-api-v3_CN.md))
- **MCP tools**:
  - **Futures**: Market data, account/positions, place/cancel orders, leverage & margin, transfers, income, commission rate, leverage bracket
  - **Spot**: Market data, account, place/cancel orders, trades, transaction history, commission rate, spot–futures transfer
- **CLI**: `config` / `list` / `start` / `stop` / `status` / `test` / `backup`

## Installation

```bash
pip install -e .
# or
pip install git+https://github.com/asterdex/aster-mcp.git
```

## Quick start

```bash
# 1. Configure account (interactive, default HMAC)
aster-mcp config

# V3 key-signing account (EIP-712)
aster-mcp config --account-id main --auth-type v3

# 2. List accounts
aster-mcp list

# 3. Start MCP service (default stdio for Cursor/Claude)
aster-mcp start

# 4. Test connection
aster-mcp test main
```

## Using with Cursor

1. Configure at least one account with `aster-mcp config`.
2. Add Aster MCP in Cursor’s MCP settings; command example:
   - `python -m aster_mcp.simple_server` (use a Python environment where `aster_mcp` is installed).
3. Use natural language in chat (e.g. “get Aster BTC price”, “place an Aster order”).

## Tool list (summary)

| Category   | Futures tools | Spot tools |
|------------|---------------|------------|
| Market     | `get_ticker`, `get_order_book`, `get_klines`, `get_funding_rate`, `get_funding_info`, `get_exchange_info`, `ping` | `get_spot_ticker`, `get_spot_price`, `get_spot_order_book`, `get_spot_klines`, `get_spot_exchange_info` |
| Account    | `get_balance`, `get_positions`, `get_account_info`, `get_account_v4` | `get_spot_account` |
| Orders     | `create_order`, `cancel_order`, `cancel_all_orders`, `get_order`, `get_open_orders`, `get_all_orders`, `get_my_trades` | `create_spot_order`, `cancel_spot_order`, `cancel_spot_all_orders`, `get_spot_order`, `get_spot_open_orders`, `get_spot_all_orders`, `get_spot_my_trades` |
| Other      | `set_leverage`, `set_margin_mode`, `transfer_funds`, `get_income`, `get_commission_rate`, `get_leverage_bracket` | `get_spot_transaction_history`, `get_spot_commission_rate`, `transfer_spot_futures` |
| System     | `get_server_info` | |

Full parameters and integration details: [Aster-MCP External Integration Guide](docs/Aster-MCP-External-Integration.md).

## Project structure

```
aster-mcp/
├── aster_mcp/
│   ├── __init__.py
│   ├── config.py       # Config & encryption
│   ├── client.py       # Aster FAPI client (futures, HMAC)
│   ├── v3_client.py    # Aster FAPI v3 client (EIP-712)
│   ├── spot_client.py  # Aster SAPI client (spot)
│   ├── tools.py        # MCP tool implementations
│   ├── simple_server.py
│   └── cli.py
├── docs/
│   └── Aster-MCP-External-Integration.md
├── tests/
├── pyproject.toml
├── requirements.txt
└── README.md
```

## Relation to Aster APIs

- This repo includes **Aster FAPI** (`client.py`, futures) and **SAPI** (`spot_client.py`, spot) clients.
- **Auth**:
  - **HMAC**: API Key/Secret for `/fapi/v1`, `/fapi/v2`, etc.
  - **V3 key signing**: user (main wallet), signer (API wallet), private_key (signer key), EIP-712; for `/fapi/v3`. Requires `eth-account`.
- Futures base URL: `https://fapi.asterdex.com`; Spot base URL: `https://sapi.asterdex.com` (overridable per account in config).
- API docs: [aster-finance-futures-api](https://github.com/asterdex/api-docs/blob/master/aster-finance-futures-api_CN.md), [aster-finance-futures-api-v3](https://github.com/asterdex/api-docs/blob/master/aster-finance-futures-api-v3_CN.md), [aster-finance-spot-api](https://github.com/asterdex/api-docs/blob/master/aster-finance-spot-api_CN.md).

## Risk and compliance

- Futures trading involves risk; verify in a test environment first.
- API keys are stored locally with encryption; do not leak or commit them.
- Comply with local regulations and Aster platform terms.

## License

MIT
