class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

print(bcolors.OK + "File Saved Successfully!" + bcolors.RESET)
print(bcolors.WARNING + "Warning: Are you sure you want to continue?" + bcolors.RESET)
print(bcolors.FAIL + "Unable to delete record." + bcolors.RESET)
