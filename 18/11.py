serial = 5535

rackID = x+10
powerLevel = rackID * y
powerLevel += serial
powerLevel *= rackID
hundreds = (powerLevel//100) % 10
powerLevel = hundreds - 5
