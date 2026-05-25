---
type: creature
group: ["Halfling", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Halfling Street Watcher"
level: "-1"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Small"
trait_01: "Halfling"
trait_02: "Humanoid"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+8"
languages: "Common, Halfling"
skills:
  - name: Skills
    desc: "Acrobatics +5, Athletics +4, Diplomacy +3, Stealth +5, Thievery +5"
abilityMods: ["-1", "+3", "+1", "+0", "+3", "+1"]
abilities_top:
  - name: "Keen Eyes"
    desc: "The halfling gains a +2 circumstance bonus when using the [[Seek]] action to find [[Hidden]] or [[Undetected]] creatures within 30 feet of it. <br>  <br> Whenever the halfling targets a creature that is [[Concealed]] or hidden from them, reduce the DC of the flat check to DC 3 flat check for a concealed target or DC 9 flat check for a hidden one."
armorclass:
  - name: AC
    desc: "15; **Fort** +3, **Ref** +8, **Will** +5"
health:
  - name: HP
    desc: "8"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Frying Pan +9 (`pf2:1`) (fatal d8), **Damage** 1d4-1 bludgeoning"
  - name: "Ranged strike"
    desc: "Halfling Sling Staff +7 (`pf2:1`) (propulsive, reload 1, range 80 ft.), **Damage** 1d10-1 bludgeoning"
spellcasting: []
abilities_bot: []
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Halflings' keen sight makes them excellent street watchers. Though the job rarely calls for fighting, most street watchers cover themselves head to ankle in whatever armor and weapons they manage to get their hands on.

Despite their small stature, a halfling can prove to be a mighty foe if you find yourself on the wrong side of their frying pan.

```statblock
creature: "Halfling Street Watcher"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
