import BaseClasses
from ..generic.Rules import set_rule, add_rule, add_item_rule
from ..AutoWorld import World
from .GeneratedRules import set_generated_rules
from .GodhomeData import set_godhome_rules
from typing import NamedTuple


class CostTerm(NamedTuple):
    term: str
    option: str
    singular: str
    plural: str
    weight: int  # CostSanity
    sort: int


cost_terms = {x.term: x for x in (
    CostTerm("RANCIDEGGS", "Egg", "Rancid Egg", "Rancid Eggs", 1, 3),
    CostTerm("GRUBS", "Grub", "Grub", "Grubs", 1, 2),
    CostTerm("ESSENCE", "Essence", "Essence", "Essence", 1, 4),
    CostTerm("CHARMS", "Charm", "Charm", "Charms", 1, 1),
    CostTerm("GEO", "Geo", "Geo", "Geo", 8, 9999),
)}


def hk_set_rule(hk_world: World, location: str, rule):
    player = hk_world.player

    locations = hk_world.created_multi_locations.get(location)
    if locations is None:
        try:
            locations = [hk_world.multiworld.get_location(location, player)]
        except KeyError:
            return

    for location in locations:
        set_rule(location, rule)


def set_rules(hk_world: World):
    def no_geo_rule(item: BaseClasses.Item) -> bool:
        if item.game != hk_world.game:
            return False
        return item.type not in {"Boss_Geo", "Geo", "Rock"}

    player = hk_world.player
    set_generated_rules(hk_world, hk_set_rule)
    set_godhome_rules(hk_world, hk_set_rule)

    # Shop costs
    for location in hk_world.multiworld.get_locations(player):
        if location.costs:
            for term, amount in location.costs.items():
                if term == "GEO":  # No geo logic!
                    continue
                add_rule(location, lambda state, term=term, amount=amount: state.count(term, player) >= amount)
        if location.name in {
            'Sly_1',
            'Sly_2',
            'Sly_3',
            'Sly_4',
            'Sly_5',
            'Sly_6',
            'Sly_7',
            'Sly_8',
            'Sly_9',
            'Sly_10',
            'Sly_11',
            'Sly_12',
            'Sly_13',
            'Sly_14',
            'Sly_15',
            'Sly_16',
            'Sly_(Key)_1',
            'Sly_(Key)_2',
            'Sly_(Key)_3',
            'Sly_(Key)_4',
            'Sly_(Key)_5',
            'Sly_(Key)_6',
            'Sly_(Key)_7',
            'Sly_(Key)_8',
            'Sly_(Key)_9',
            'Sly_(Key)_10',
            'Sly_(Key)_11',
            'Sly_(Key)_12',
            'Sly_(Key)_13',
            'Sly_(Key)_14',
            'Sly_(Key)_15',
            'Sly_(Key)_16',
            'Iselda_1',
            'Iselda_2',
            'Iselda_3',
            'Iselda_4',
            'Iselda_5',
            'Iselda_6',
            'Iselda_7',
            'Iselda_8',
            'Iselda_9',
            'Iselda_10',
            'Iselda_11',
            'Iselda_12',
            'Iselda_13',
            'Iselda_14',
            'Iselda_15',
            'Iselda_16',
            'Salubra_1',
            'Salubra_2',
            'Salubra_3',
            'Salubra_4',
            'Salubra_5',
            'Salubra_6',
            'Salubra_7',
            'Salubra_8',
            'Salubra_9',
            'Salubra_10',
            'Salubra_11',
            'Salubra_12',
            'Salubra_13',
            'Salubra_14',
            'Salubra_15',
            'Salubra_16',
            'Salubra_(Requires_Charms)_1',
            'Salubra_(Requires_Charms)_2',
            'Salubra_(Requires_Charms)_3',
            'Salubra_(Requires_Charms)_4',
            'Salubra_(Requires_Charms)_5',
            'Salubra_(Requires_Charms)_6',
            'Salubra_(Requires_Charms)_7',
            'Salubra_(Requires_Charms)_8',
            'Salubra_(Requires_Charms)_9',
            'Salubra_(Requires_Charms)_10',
            'Salubra_(Requires_Charms)_11',
            'Salubra_(Requires_Charms)_12',
            'Salubra_(Requires_Charms)_13',
            'Salubra_(Requires_Charms)_14',
            'Salubra_(Requires_Charms)_15',
            'Salubra_(Requires_Charms)_16',
            'Leg_Eater_1',
            'Leg_Eater_2',
            'Leg_Eater_3',
            'Leg_Eater_4',
            'Leg_Eater_5',
            'Leg_Eater_6',
            'Leg_Eater_7',
            'Leg_Eater_8',
            'Leg_Eater_9',
            'Leg_Eater_10',
            'Leg_Eater_11',
            'Leg_Eater_12',
            'Leg_Eater_13',
            'Leg_Eater_14',
            'Leg_Eater_15',
            'Leg_Eater_16',
            'Vessel_Fragment-Basin',
            'Whispering_Root-Crossroads',
            'Whispering_Root-Greenpath',
            'Whispering_Root-Leg_Eater',
            'Whispering_Root-Mantis_Village',
            'Whispering_Root-Deepnest',
            'Whispering_Root-Queens_Gardens',
            'Whispering_Root-Kingdoms_Edge',
            'Whispering_Root-Waterways',
            'Whispering_Root-City',
            'Whispering_Root-Resting_Grounds',
            'Whispering_Root-Spirits_Glade',
            'Whispering_Root-Crystal_Peak',
            'Whispering_Root-Howling_Cliffs',
            'Whispering_Root-Ancestral_Mound',
            'Whispering_Root-Hive',
            'Crossroads_Map',
            'Greenpath_Map',
            'Fog_Canyon_Map',
            'Fungal_Wastes_Map',
            'Deepnest_Map-Upper',
            'Deepnest_Map-Right',
            'Ancient_Basin_Map',
            "Kingdom's_Edge_Map",
            'City_of_Tears_Map',
            'Royal_Waterways_Map',
            'Howling_Cliffs_Map',
            'Crystal_Peak_Map',
            "Queen's_Gardens_Map",
            'Resting_Grounds_Map',
            'Dirtmouth_Stag',
            'Crossroads_Stag',
            'Greenpath_Stag',
            "Queen's_Station_Stag",
            "Queen's_Gardens_Stag",
            'City_Storerooms_Stag',
            "King's_Station_Stag",
            'Resting_Grounds_Stag',
            'Distant_Village_Stag',
            'Hidden_Station_Stag',
            'Stag_Nest_Stag',
        }:
            add_item_rule(location, no_geo_rule)


def _hk_nail_combat(state, player) -> bool:
    return state.has_any({'LEFTSLASH', 'RIGHTSLASH', 'UPSLASH'}, player)


def _hk_can_beat_thk(state, player) -> bool:
    return (
        state.has('Opened_Black_Egg_Temple', player)
        and (state.count('FIREBALL', player) + state.count('SCREAM', player) + state.count('QUAKE', player)) > 1
        and _hk_nail_combat(state, player)
        and (
            state.has_any({'LEFTDASH', 'RIGHTDASH'}, player)
            or state._hk_option(player, 'ProficientCombat')
        )
        and state.has('FOCUS', player)
    )


def _hk_siblings_ending(state, player) -> bool:
    return _hk_can_beat_thk(state, player) and state.has('WHITEFRAGMENT', player, 3)


def _hk_can_beat_radiance(state, player) -> bool:
    return (
        state.has('Opened_Black_Egg_Temple', player)
        and _hk_nail_combat(state, player)
        and state.has('WHITEFRAGMENT', player, 3)
        and state.has('DREAMNAIL', player)
        and (
            (state.has('LEFTCLAW', player) and state.has('RIGHTCLAW', player))
            or state.has('WINGS', player)
        )
        and (state.count('FIREBALL', player) + state.count('SCREAM', player) + state.count('QUAKE', player)) > 1
        and (
            (state.has('LEFTDASH', player, 2) and state.has('RIGHTDASH', player, 2))  # Both Shade Cloaks
            or (state._hk_option(player, 'ProficientCombat') and state.has('QUAKE', player))  # or Dive
        )
    )
