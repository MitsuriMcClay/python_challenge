#!/opt/homebrew/bin/python3

#You need this line for both
# from pathlib import Path

#File reading
# #print(Path(__file__).parent.parent / "1119.sh")
# #a = Path(__file__).parent.parent / "1119.sh"
# #filereading = a.read_text()
# #print(filereading)

# File writing 
# a = Path("mytext.txt")
# a.write_text("This is some text")


from pathlib import Path
var = Path("testtextmitsuri.txt")
#var.write_text("Hey It's working!")
newvar = var.read_text()
print(newvar)