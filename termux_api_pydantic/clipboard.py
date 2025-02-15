from ._base import _execute


def get() -> str:
	return _execute("termux-clipboard-get")


def set(*, content___I_ACKNOWLEDGE_THIS_RUNS_SHELL_COMMAND_WITHOUT_ESCAPING_ANYTHING_AND_IS_INSECURE_IF_USER_INPUT_IS_PASSED_IN: str) -> None:
	_execute(f"termux-clipboard-set {content___I_ACKNOWLEDGE_THIS_RUNS_SHELL_COMMAND_WITHOUT_ESCAPING_ANYTHING_AND_IS_INSECURE_IF_USER_INPUT_IS_PASSED_IN}")
