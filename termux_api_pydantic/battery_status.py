from ._base import _BM, _execute


class BatteryStatus(_BM):
	health: str
	percentage: int
	plugged: str
	status: str
	temperature: float
	current: int


def battery_status():
	return BatteryStatus(**_execute("termux-battery-status"))
