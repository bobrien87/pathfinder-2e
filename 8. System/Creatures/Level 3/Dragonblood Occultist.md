---
type: creature
group: ["Dragonblood", "Human"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Dragonblood Occultist"
level: "3"
rare_01: "Rare"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Dragonblood"
trait_02: "Human"
trait_03: "Humanoid"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+10"
languages: "Aklo, Common, Draconic, Elven, Sakvroth"
skills:
  - name: Skills
    desc: "Acrobatics +8, Arcana +9, Deception +8, Occultism +10, Religion +6, Thievery +10"
abilityMods: ["+1", "+3", "+0", "+4", "+1", "+1"]
abilities_top: []
armorclass:
  - name: AC
    desc: "18; **Fort** +6, **Ref** +9, **Will** +12"
health:
  - name: HP
    desc: "35"
abilities_mid:
  - name: "Draconic Willpower"
    desc: "When the occultist rolls a success on a saving throw against a fear effect, they get a critical success instead."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Shortsword +10 (`pf2:1`) (agile, finesse, versatile s), **Damage** 1d6+4 piercing"
  - name: "Melee strike"
    desc: "Fist +10 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4+4 bludgeoning"
  - name: "Ranged strike"
    desc: "Crossbow +10 (`pf2:1`) (reload 1, range 120 ft.), **Damage** 1d8+3 piercing"
spellcasting: []
abilities_bot:
  - name: "Light of Fate"
    desc: "`pf2:1` **Requirements** The dragonblood occultist is holding a lit lantern <br>  <br> **Effect** The dragonblood occultist shines the lantern's light on one creature within 20 feet, revealing wounds yet to occur. The dragonblood occultist then chooses bludgeoning, mental, piercing, or slashing, and the target gains weakness 4 to that damage until the end of the dragonblood occultist's next turn."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

The dragonblood occultist draws power from their omen dragon benefactor. This occult connection allows the occultist to perceive glimpses of the near future.

When a dragon holds influence in a community, either by exerting their might or blending in and living among them, a child might be born that exhibits physical or mental aspects of that dragon. These offspring are known as dragonbloods and often have draconic features belying their heritage. Dragonbloods can be found among all ancestries, though many dragonbloods are either humans or have some kind of extant dragon connection, such as kobolds who have a close association with a dragon.

A dragonblood typically possesses some physical feature that gives away their draconic nature. These can be subtle features such as elongated fingernails that resemble claws or unique eye coloration. For many dragonbloods, these features are more overt, taking the form of horns, draconic tails, wings, or patches of scales. In some cases, a dragonblood resembles a bipedal dragon outright, often leading to confusing them with other reptilian ancestries such as kobolds and lizardfolk. For dragonbloods who have no obvious features, there are still the occasional hints of their draconic influence, typically manifesting in times of overwhelming emotions, if only for a moment.

Dragonbloods can trace their connection to a specific type of dragon, commonly referred to as a draconic exemplar. The physical features and abilities of a dragonblood always match that of their draconic exemplar. A dragonblood whose exemplar is a cinder dragon, for example, will manifest crimson scales or the ability to breathe fire. A dragon's opinion of a related dragonblood can vary. Most dragons tend to look at dragonbloods with indifference. Benevolent and social dragons often find a kinship in learning of a related dragonblood. Some dragons see dragonbloods as beneath them, however. As a dragonblood isn't a "true" dragon, the draconic exemplar cares little for them.

```statblock
creature: "Dragonblood Occultist"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
