import yaml
from game.lib import character

bp = yaml.load(open('./game/data/exampleBodyPlan.yaml'))
cp = yaml.load(open('./game/data/exampleCreature.yaml'))
pp = yaml.load(open('./game/data/examplePartPlan.yaml'))
tp = yaml.load(open('./game/data/exampleType.yaml'))

print('done loading')

race_type = character.RaceType(**tp)
race = character.Race(cp['name'], cp['childScale'], cp['scalingFactorSizeStD'], cp['scalingFactorStrength'],
                      cp['femaleToMaleSizeFactor'], cp['femaleToMaleStrengthFactor'], race_type)
