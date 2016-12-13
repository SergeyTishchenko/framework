from locators.locator import user_name_field, password_field, subm

def login(user):
    print "Found %s" % user_name_field
    print "Found %s" % password_field
    print "Pressing %s" % subm
    print "{0} is logged in with password {1}".format(user[0], user[1])
