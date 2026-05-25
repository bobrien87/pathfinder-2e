---
type: creature
group: ["Hobgoblin", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Hobgoblin Spellbreaker"
level: "3"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Hobgoblin"
trait_02: "Humanoid"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+9; [[Darkvision]]"
languages: "Common, Goblin"
skills:
  - name: Skills
    desc: "Acrobatics +9, Arcana +10, Athletics +10, Intimidation +9, Stealth +9"
abilityMods: ["+3", "+1", "+1", "+3", "+1", "+1"]
abilities_top: []
armorclass:
  - name: AC
    desc: "18; **Fort** +12, **Ref** +6, **Will** +9"
health:
  - name: HP
    desc: "50"
abilities_mid:
  - name: "Arcane Magic Sense"
    desc: "The hobgoblin spellbreaker can detect the source of any arcane magic within range as an imprecise sense."
  - name: "Spellbreaking Reactive Strike"
    desc: "`pf2:r` As [[Reactive Strike]], but if it was triggered by a creature casting an arcane spell, the target must succeed at a DC 11 flat check or the spell is disrupted. If the Strike was a critical hit, the spell is disrupted automatically."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Breaching Pike +12 (`pf2:1`) (razing, reach), **Damage** 1d6+6 piercing"
  - name: "Melee strike"
    desc: "Shortsword +12 (`pf2:1`) (agile, versatile s), **Damage** 1d6+6 piercing"
  - name: "Melee strike"
    desc: "Fist +12 (`pf2:1`) (agile, nonlethal, unarmed), **Damage** 1d4+6 bludgeoning"
  - name: "Ranged strike"
    desc: "Crossbow +10 (`pf2:1`) (reload 1, range 120 ft.), **Damage** 1d8+3 piercing"
spellcasting: []
abilities_bot:
  - name: "Shatter Spell"
    desc: "`pf2:2` The hobgoblin spellbreaker attempts a melee Strike against a creature under the effects of a beneficial arcane spell. If the Strike hits and deals damage, the hobgoblin spellbreaker can attempt to counteract a single arcane spell or arcane magical effect on the target (counteract rank 2, counteract modifier +10). If it fails, the hobgoblin spellbreaker can't attempt to counteract the same effect for 1 hour."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Largely due to an ancestral grudge against all things elven, many hobgoblins have an inherent distrust for magic, particularly the "elf magic" of the arcane tradition. Most hobgoblin armies maintain a contingent of special "spellbreaker" forces trained to assassinate high-value spellcasting targets prior to military engagement or quickly identify and terminate enemy battle mages.

Hobgoblins are respected across Golarion for their unmatched expertise in the art of war. The recent foundation of the hobgoblin nation of Oprak and its unprecedented acts of diplomacy, including non-aggression pacts with the neighboring nations of Nidal and Nirmathas, has given some hope that a lasting peace might finally be established; however, there remains no shortage of unaffiliated hobgoblin raiders and pillagers.

```statblock
creature: "Hobgoblin Spellbreaker"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
