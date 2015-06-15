def como_variables():
	try:
		raise ValueError("Esto es un argumento")
	except ValueError as e:
		print("Los argumentos exception fueron:", e.args)