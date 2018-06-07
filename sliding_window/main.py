def window(iterable, size=2):
	i = iter(iterable)
	win = []

	for e in range (0, size):
		win.append(next(i))

	yield win # Yields Generator instance of first window

	for e in i:
		win = win[1:] + [e]
		yield win  # Yields the next instance of the window


