# The get() method on dicts
# and its "default" argument

name_for_userid = {
    382: "Alice",
    590: "Bob",
    951: "Dilbert",
}

def greeting(userid):
    return "Hi %s!" % name_for_userid.get(userid, "there")

#wywołanie
# greeting(382)
# greeting(333333)

#dla cwiczenie print
print(greeting(382))
print(greeting(3333333))
