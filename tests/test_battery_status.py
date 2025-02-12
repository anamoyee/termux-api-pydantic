import termux_api_pydantic as tmx


def test_battery_status():
	assert 0 <= tmx.battery_status.battery_status().percentage <= 100
