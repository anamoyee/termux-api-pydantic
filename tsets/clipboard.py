from termux_api_pydantic import clipboard


def main():
	try:
		while 1:
			choice = input(
				"""
<enter without typing anything> : clipboard.get()
<anything>                      : clipboard.set()
^C                              :            exit
>>> 
"""[1:-1]
			).strip()

			if not choice:
				print(f"{clipboard.get()=}")

			clipboard.set(content___I_ACKNOWLEDGE_THIS_RUNS_SHELL_COMMAND_WITHOUT_ESCAPING_ANYTHING_AND_IS_INSECURE_IF_USER_INPUT_IS_PASSED_IN=choice)

	except KeyboardInterrupt:
		print("^C")


if __name__ == "__main__":
	main()
