import structure
print()
print()
print("                                              *                            ")
print("                                             * *                           ")
print("                  ***************************   ***************************")
print("                  *                                                       *")
print("                  *     ##   ##    # #     ######     #       ####        *")
print("                  *     #  #  #  #     #        #    # #     #            *")
print("                  *     #     #  #     #        #   #   #     ###         *")
print("                  *     #     #  #     #   #    #  # ### #       #        *")
print("                  *     #     #    # #      ####  #       #  ####         *")
print("                  *                                                       *")
print("                  *                                                       *")
print("                  *                  Developed by @sif                    *")
print("                  ***************************   ***************************")
print("                                             * *                           ")
print("                                              *                            ")
print()
print()
while True:
	text = input(':: Mojas >>> ')
	result, error = structure.run('<stdin>', text)

	if error: print(error.as_string())
	elif result: print(result)