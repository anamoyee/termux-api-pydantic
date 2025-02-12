import json
import subprocess

from pydantic import BaseModel as _BaseModel
from pydantic import ConfigDict as _ConfigDict


class _BM(_BaseModel):
	model_config = _ConfigDict(
		arbitrary_types_allowed=True,
		extra="allow",
		validate_assignment=True,
		validate_default=True,
	)


def _execute(s: str, timeout: float = 5.0):
	"""Execute as shell command, capture the outpu and parse as json.

	Raises:
		- subprocess.TimeoutExpired when the timeout expired
		- json.JSONDecodeError when the data received was malformed
		- possibly any subprocess error if enough shit happened
	"""
	result = subprocess.run(s.split(" "), capture_output=True, text=True, timeout=timeout)

	return json.loads(result.stdout)
