from platform import system

osSystem = system()
unixSystem = ["Linux", "Darwin"]

if osSystem in unixSystem:
    clearScreenCommand = "clear"
else:
    clearScreenCommand = "cls"

if __name__ == "__main__":
    print(osSystem)
    print(clearScreenCommand)
