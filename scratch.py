import yaml
from game.lib import character

cp = next(yaml.load_all(open('./game/data/exampleCreature.yaml')))


parts = {}
materials = {}
for pp in yaml.load_all(open(cp['using']['partPlan'])):
    print(pp)
    parts[pp['name']] =

bp = yaml.load_all(open(cp['using']['bodyPlan']))
pp = yaml.load_all(open(cp['using']['partPlan']))
tp = yaml.load_all(open(cp['using']['type']))

print('done loading')

race_type = character.RaceType(**tp)
race = character.Race(cp['name'], cp['childScale'], cp['scalingFactorSizeStD'], cp['scalingFactorStrength'],
                      cp['femaleToMaleSizeFactor'], cp['femaleToMaleStrengthFactor'], race_type)
