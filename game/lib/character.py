

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

    def __init__(self):
        self.name = '_defaultName'
        self.parent_body = None
        self.parent_part = None
        self.child_parts = []
        self.layers = []    # index 0 is innermost layer, index -1 is outermost
        self.continuous_organs = []
        self.length = -1    # Length from last part connection to next part connection
        self.width = -1     # Width as viewed from front of body
        self.depth = -1     # Depth as viewed from front of body


class Joint:

    def __init__(self):
        self.name = '_defaultName'
        self.parent_body = None
        self.parent_part = None
        self.child_part = None
        self.controlled_by = []


class Layer:

    def __init__(self):
        self.material = None
        self.name = '_defaultName'
        self.next_layer_out = None
        self.next_layer_in = None
        self.thickness = -1
        self.is_rigid = None