continue_reading = True


def get_continue_reading():
	return continue_reading


def stop_reading():
	global continue_reading
	continue_reading = False
