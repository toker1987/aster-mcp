"""单元测试：ConfigManager"""
import pytest
from aster_mcp.config import ConfigManager


@pytest.fixture
def config_manager():
    return ConfigManager()


def test_encrypt_decrypt(config_manager):
    plain = "test_secret"
    enc = config_manager.encrypt_value(plain)
    assert enc != plain
    assert config_manager.decrypt_value(enc) == plain


def test_list_accounts_no_secrets(config_manager):
    accounts = config_manager.list_accounts()
    assert isinstance(accounts, dict)
    for aid, info in accounts.items():
        assert "api_key" not in info and "api_secret" not in info
