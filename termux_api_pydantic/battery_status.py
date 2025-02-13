from ._base import _BM, _execute


# Not making an enum for the inner values here, since i dont know every value, and the termux api docs are LACKING...
class BatteryStatus(_BM):
	health: str
	"""### Possible values i've seen:
	- `"GOOD"`
	"""

	percentage: int
	"""### `0..=100`"""

	plugged: str
	"""### Possible values i've seen:
	- `"UNPLUGGED"`
	- `"PLUGGED_USB"`
	"""

	status: str
	"""### Possible values i've seen:
	- `"CHARGING"`
	- `"DISCHARGING"`
	- `"FULL"`
	"""

	temperature: float
	"""### Presumably in °C"""

	current: int
	"""### Positive when charging, negative when discharging"""

	def is_charging(self):
		return self.status != "DISCHARGING"

	def is_plugged(self):
		return self.status != "UNPLUGGED"

	def get_percentage_emoji(
		self,
		*,
		warn_only_if_not_charging: bool = True,
		threshold_tenth: int = 10,
		threshold_quarter: int = 25,
	) -> str:
		if (warn_only_if_not_charging and self.is_charging()) or self.percentage > threshold_quarter:
			return "🔋"

		if self.percentage > threshold_tenth:
			return "🔋⚠️"

		return "🔋‼️"

	def get_plugged_emoji(self) -> str:
		return "🔌" if self.is_plugged() else ""

	def display(
		self,
		*,
		pattern: str = "%(percentage_emoji)s%(plugged_emoji)s %(percentage)s%%",
	):
		return pattern % {
			"percentage_emoji": self.get_percentage_emoji(),
			"plugged_emoji": self.get_plugged_emoji(),
			"percentage": str(self.percentage),
		}


def battery_status():
	return BatteryStatus(**_execute("termux-battery-status"))
