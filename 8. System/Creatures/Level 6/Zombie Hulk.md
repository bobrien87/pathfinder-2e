---
type: creature
group: ["Mindless", "Undead"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Zombie Hulk"
level: "6"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Huge"
trait_01: "Mindless"
trait_02: "Undead"
trait_03: "Unholy"
trait_04: "Zombie"
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+8; [[Darkvision]]"
languages: ""
skills:
  - name: Skills
    desc: "Athletics +18"
abilityMods: ["+7", "-1", "+4", "-5", "+0", "-2"]
abilities_top:
  - name: "Slow"
    desc: "A zombie is permanently slowed 1 and can't use reactions."
  - name: "Corpse Throwing"
    desc: "A zombie hulk can throw Medium or smaller corpses at foes. They can also throw Medium or smaller zombies for this purpose, who take just as much damage as the target they hit. A zombie that survives being thrown falls [[Prone]]."
armorclass:
  - name: AC
    desc: "21; **Fort** +16, **Ref** +9, **Will** +12"
health:
  - name: HP
    desc: "160; void healing; **Immunities** death effects, disease, paralyzed, poison, unconscious, bleed; **Weaknesses** vitality 10, slashing 10"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Hunk Of Meat +17 (`pf2:1`) (reach 15 ft.), **Damage** 2d10+9 bludgeoning"
  - name: "Ranged strike"
    desc: "Corpse +17 (`pf2:1`) (brutal, range 30 ft.), **Damage** 2d6+9 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Wide Swing"
    desc: "`pf2:1` The zombie hulk makes two hunk of meat Strikes against different targets within its reach."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

These towering horrors rise from monstrous, gigantic corpses.

A zombie's only desire is to consume the living. Unthinking and ever-shambling harbingers of death, zombies stop only when they're destroyed.

```statblock
creature: "Zombie Hulk"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
