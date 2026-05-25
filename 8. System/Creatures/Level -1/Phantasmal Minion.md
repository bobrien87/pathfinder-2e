---
type: creature
group: ["Force", "Mindless"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Phantasmal Minion"
level: "-1"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Force"
trait_02: "Mindless"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+0; [[Darkvision]]"
languages: "understands its creator"
skills:
  - name: Skills
    desc: "Stealth +8"
abilityMods: ["-4", "+2", "+0", "-5", "+0", "+0"]
abilities_top:
  - name: "Force Body"
    desc: "A phantasmal minion's body is made of magical force. It can't use attack actions. Though it has no physical weight, it can move and use Interact actions to do things such as fetch objects, open unstuck or unlocked doors, hold chairs, and clean. It can't pass through solid objects."
  - name: "Invisible"
    desc: "An phantasmal minion can be summoned [[Invisible]], though it normally doesn't [[Sneak]], so it is usually only [[Hidden]]."
armorclass:
  - name: AC
    desc: "13; **Fort** +0, **Ref** +4, **Will** +0"
health:
  - name: HP
    desc: "4; **Immunities** disease, paralyzed, poison, precision, unconscious, spirit; **Resistances** all damage 5 except force, ghost touch"
abilities_mid: []
speed: "0 feet"
attacks: []
spellcasting: []
abilities_bot: []
sourcebook: "Player Core"
source-type: "Remaster"
---
### `= this.file.name`

This creature can be summoned with the spell [[Phantasmal Minion]].

```statblock
creature: "Phantasmal Minion"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
