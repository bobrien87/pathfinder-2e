---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Diver"
level: "3"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+9"
languages: "Common, Thalassic"
skills:
  - name: Skills
    desc: "Acrobatics +10, Athletics +10, Nature +9, Thievery +9, Ocean Lore +11"
abilityMods: ["+3", "+3", "+2", "+0", "+2", "+0"]
abilities_top:
  - name: "Adjusted Eyes"
    desc: "Divers are used to the murky conditions underwater and train for them. If the diver spends 1 hour preparing for their dive, they have low-light vision while underwater."
  - name: "Diving Specialist"
    desc: "For encounters involving underwater exploration, the diver is a 10th-level challenge."
  - name: "Skilled Diver"
    desc: "The diver gains a +12 circumstance bonus to any skill check involved in underwater exploration activities and is considered a master in the skill for such checks. This bonus also applies to any initiative roll while the driver is underwater."
  - name: "Strong Lungs"
    desc: "The diver can hold their breath for up to 5 minutes (50 rounds)."
  - name: "Underwater Fighter"
    desc: "The diver isn't [[Off Guard]] underwater and doesn't take penalties for using a bludgeoning or slashing melee weapon in water."
armorclass:
  - name: AC
    desc: "17; **Fort** +9, **Ref** +12, **Will** +6"
health:
  - name: HP
    desc: "50"
abilities_mid:
  - name: "Underwater Awareness"
    desc: "`pf2:r` **Trigger** An enemy Strikes the diver while they're underwater <br>  <br> **Effect** The diver senses the movement of their enemy in the water and jerks back in time. They gain a +2 circumstance bonus to their AC against the triggering attack."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Trident +12 (`pf2:1`), **Damage** 1d8+5 piercing"
  - name: "Melee strike"
    desc: "Trident +12 (`pf2:1`) (thrown 20), **Damage** 1d8+5 piercing"
  - name: "Melee strike"
    desc: "Fist +12 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4+5 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Dive"
    desc: "`pf2:1` The diver moves up to twice their swim Speed downward."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Divers can often make large amounts of money by diving for treasures and selling them at a markup to tourists and antiquities dealers.

Adventurers may need passage on a swift vessel, or they might face danger from raiders at sea or in coastal settlements.

```statblock
creature: "Diver"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
