import json

with open ("sample-data.json", "r") as ourfile:
    ourdata = json.load(ourfile)

ourinterfaces = ourdata["imdata"]

print("Interface Status")
print("================================================================================")
print("DN                                                 Description           Speed    MTU")
print("-------------------------------------------------- --------------------  ------  ------")


for item in ourinterfaces:
    attributes = item["l1PhysIf"]["attributes"]
    dn = attributes["dn"]
    speed = attributes["speed"]
    mtu = attributes["mtu"]
    print(dn + "                              " + speed + "   " + mtu)