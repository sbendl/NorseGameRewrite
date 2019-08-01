import yaml
from game.lib import character, material

cp = next(yaml.load_all(open('./game/data/exampleCreature.yaml')))


parts = {}

for pp in yaml.load_all(open(cp['using']['partPlan'])):
    materials = {}
    organs = {}
    print(pp)
    if 'material' in pp['using'].keys():
        for mp in yaml.load_all(open(pp['using']['material'])):
            materials[mp['name']] = material.Material(name=mp['name'])
    if 'organ' in pp['using'].keys():
        for op in yaml.load_all(open(pp['using']['organ'])):
            organs[op['name']] = character.Organ(name=op['name'], critical=op['critical'],
                                                 deathTime=op['deathTime'] if op['critical'] else None)
    layers = []
    last_layer=None
    for layer in pp['layers']:
        if layer['name'] == 'organContainer':

        this_layer = character.Layer(material=materials[layer['material']], name=layer['name'], next_layer_out=last_layer)
        if last_layer is not None:
            last_layer.next_layer_in = this_layer
        layers.append(this_layer)
        last_layer = this_layer
    parts[pp['name']] = character.BodyPart(name=pp['name'], layers=layers)

body_plans = {}
for bp in yaml.load_all(open(cp['using']['bodyPlan'])):
    pass

bp = yaml.load_all(open(cp['using']['bodyPlan']))
pp = yaml.load_all(open(cp['using']['partPlan']))
tp = yaml.load_all(open(cp['using']['type']))

print('done loading')

race_type = character.RaceType(**tp)
race = character.Race(cp['name'], cp['childScale'], cp['scalingFactorSizeStD'], cp['scalingFactorStrength'],
                      cp['femaleToMaleSizeFactor'], cp['femaleToMaleStrengthFactor'], race_type)
