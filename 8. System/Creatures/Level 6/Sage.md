---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Sage"
level: "6"
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
    desc: "+14"
languages: "Common (up to 4 additional languages)"
skills:
  - name: Skills
    desc: "Arcana +12, Diplomacy +13, Medicine +12, Nature +14, Occultism +12, Religion +12, Society +14"
abilityMods: ["+2", "+2", "+1", "+4", "+3", "+0"]
abilities_top: []
armorclass:
  - name: AC
    desc: "22; **Fort** +10, **Ref** +12, **Will** +16"
health:
  - name: HP
    desc: "86"
abilities_mid:
  - name: "Timely Advice"
    desc: "`pf2:r` **Trigger** An ally is about to attempt an attack roll or skill check and has not yet rolled <br>  <br> **Effect** The sage gives the ally a savvy piece of advice, providing valuable insight. The ally gains a +2 circumstance bonus to the triggering roll. <br>  <br> > [!danger] Effect: Timely Advice"
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Staff +13 (`pf2:1`) (magical, two hand d8), **Damage** 1d4+6 bludgeoning"
  - name: "Melee strike"
    desc: "Fist +12 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4+6 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Sage's Analysis"
    desc: "`pf2:1` The sage studies a creature, attempting an [[Arcana]] check, [[Nature]] check, [[Occultism]] check, [[Religion]] check, or [[Society]] check against the creature's [[Recall Knowledge]] DC. On a success, the sage gains a +2 circumstance bonus to attack rolls and AC against that creature and deals an additional 2d6 damage to the creature with weapon attacks. <br>  <br> These benefits last for 1 minute or until the sage uses this ability again. <br>  <br> > [!danger] Effect: Sage's Analysis"
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

The greatest knowledge comes from experience. Village elders, ancient seers, and advisors to royalty are examples of those valued for such wisdom. Sages educate and guide their people from straying from their cultures' norms and traditions.

True power comes from knowledge—the power to shape the growth of kingdoms by mere whispers, stay three steps ahead of adversaries, or even know which flora is best for creating untraceable poisons.

```statblock
creature: "Sage"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
