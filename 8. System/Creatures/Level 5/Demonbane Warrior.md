---
type: creature
group: ["Elf", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Demonbane Warrior"
level: "5"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Elf"
trait_02: "Humanoid"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+13; [[Low-Light Vision]]"
languages: "Chthonian, Common, Elven"
skills:
  - name: Skills
    desc: "Acrobatics +13, Religion +11, Stealth +10, Survival +11, Demon Lore +12"
abilityMods: ["+3", "+4", "+2", "+1", "+2", "+0"]
abilities_top:
  - name: "Sin Sense"
    desc: "A demonbane warrior automatically learns all weaknesses of a demon they've identified by [[Recalling Knowledge]]."
  - name: "Demonbane"
    desc: "A demonbane warrior gains a +1 circumstance bonus to damage rolls against demons. If their actions force a demon to take damage from its sin vulnerability, increase the damage from the vulnerability by 2."
armorclass:
  - name: AC
    desc: "22; **Fort** +11, **Ref** +13, **Will** +11"
health:
  - name: HP
    desc: "76"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Cold Iron Elven Branched Spear +15 (`pf2:1`) (cold iron, deadly d8, finesse, reach), **Damage** 1d6+9 piercing"
  - name: "Melee strike"
    desc: "Fist +15 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4+9 bludgeoning"
  - name: "Ranged strike"
    desc: "Composite Shortbow +15 (`pf2:1`) (deadly d10, propulsive, reload 0, range 60 ft.), **Damage** 1d6+7 piercing"
spellcasting: []
abilities_bot:
  - name: "Imbue Righteousness"
    desc: "`pf2:1` The warrior imbues a weapon they wield with holy energy. Until the start of their next turn, their Strikes with that weapon gain the holy trait and deal an additional 1d6 spirit damage to unholy creatures."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Elves' long lives give them centuries to delve into studies, artistry, or exploration.

```statblock
creature: "Demonbane Warrior"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
