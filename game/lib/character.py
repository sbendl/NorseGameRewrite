

class Character:

    def __init__(self):
        self.skills = []
        self.attributes = []
        self.traits = []
        self.body = None
        self.relationships = []
        self.name = '_defaultName'


class Skill:

    def __init__(self):
        self.level = -1
        self.name = '_defaultName'
        self.governing_attribute = None
        self.transfers_to = []


class Attribute:

    def __init__(self):
        self.level = -1
        self.name = '_defaultName'
        self.governs = []


class Trait:
    # TODO nail down what these do/are and comment them before you forget again
    def __init__(self):
        self.name = '_defaultName'


class RaceType:

    def __init__(self, name='_defaultName', mortal=False, godlike=False):
        self.name = name
        self.mortal = mortal
        self.godlike = godlike


class Race:

    def __init__(self, name='_defaultName', child_scale=-1.0, size_scaling_factor_std=-1.0,
                 strength_scaling_factor=-1.0, female_male_size_factor=-1.0, female_male_strength_factor=-1.0,
                 race_type=None):
        self.name = name
        self.child_scale = child_scale
        self.size_scaling_factor_std = size_scaling_factor_std
        self.strength_scaling_factor = strength_scaling_factor
        self.female_male_size_factor = female_male_size_factor
        self.female_male_strength_factor = female_male_strength_factor
        self.race_type = race_type


class Body:

    def __init__(self):
        self.body_plan = None   # Each race should have part scaling factors and material mappings used for body plan
        self.scaling_factor = -1.0
        self.body_parts = []
        self.race = None


class BodyPlan:

    def __init__(self, name='_defaultName', root=None, symmetry_type=None):
        self.root = root
        self.name = name
        self.symmetry_type = symmetry_type
        self.parts_list = []
        self.joint_list = []


class BodyPart:     # Can infer if is a leaf part if no children - no need for separate child class
    """
    Body Parts are considered to be rectangular prisms with layers of different materials making up 'shells' inside.
    They may also contain 'continuous organs' such as tendons and nerves that run the full length of the part.
    """

    def __init__(self, name='_defaultName', parent_body=None, parent_part=None, child_parts=None, layers=None,
                 continuous_organs=None, length=-1, width=-1, depth=-1):
        if child_parts is None:
            self.child_parts = []
        if layers is None:
            self.layers = []
        if continuous_organs is None:
            self.continuous_organs = []
        self.name = name
        self.parent_body = parent_body
        self.parent_part = parent_part
        self.length = length    # Length from last part connection to next part connection
        self.width = width    # Width as viewed from front of body
        self.depth = depth     # Depth as viewed from front of body


class Organ:

    def __init__(self, name='_defaultName', parent_body=None, parent_part=None, relative_size=-1.0, critical=False,
                 deathTime='_defaultTime'):
        self.name = name
        self.parent_body = parent_body
        self.parent_part = parent_part
        self.relative_size = relative_size
        self.critical = critical
        self.time_to_death = deathTime


class Joint:

    def __init__(self):
        self.name = '_defaultName'
        self.parent_body = None
        self.parent_part = None
        self.child_part = None
        self.controlled_by = []


class Layer:

    def __init__(self, name='_defaultName', material=None, next_layer_out=None, next_layer_in=None, thickness=-1):
        self.material = material
        self.name = name
        self.next_layer_out = next_layer_out
        self.next_layer_in = next_layer_in
        self.thickness = thickness
