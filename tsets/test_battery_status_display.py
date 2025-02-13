import termux_api_pydantic as tmx


def test_battery_status_display():
	battery_status = tmx.battery_status.battery_status()

	print(battery_status.display())


if __name__ == "__main__":
	test_battery_status_display()
