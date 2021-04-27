from py2neo.ogm import GraphObject, Property


class User(GraphObject):
    __primarylabel__ = "user"
    __primarykey__ = "email"
    name = Property()
    email = Property()
    password = Property()
    hashed_password = Property()
    created_on = Property()
    last_logon = Property()

#class Events(GraphObject):
#    __primarylabel__="event"
#    __primarykey__="email"
#    title=Property()
#    email=Property()
#    detail=Property()




