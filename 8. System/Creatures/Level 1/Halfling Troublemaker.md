---
type: creature
group: ["Halfling", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Halfling Troublemaker"
level: "1"
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
    desc: "+10"
languages: "Common, Halfling"
skills:
  - name: Skills
    desc: "Acrobatics +7, Athletics +3, Deception +5, Stealth +7, Thievery +7"
abilityMods: ["+1", "+4", "+1", "+0", "+3", "+3"]
abilities_top:
  - name: "Keen Eyes"
    desc: "The halfling gains a +2 circumstance bonus when using the [[Seek]] action to find [[Hidden]] or [[Undetected]] creatures within 30 feet of it. <br>  <br> Whenever the halfling targets a creature that is [[Concealed]] or hidden from them, reduce the DC of the flat check to DC 3 flat check for a concealed target or DC 9 flat check for a hidden one."
  - name: "Sneak Attack"
    desc: "The troublemaker deals an extra 1d6 precision damage to [[Off Guard]] creatures."
armorclass:
  - name: AC
    desc: "16; **Fort** +4, **Ref** +10, **Will** +7"
health:
  - name: HP
    desc: "18"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Filcher's Fork +9 (`pf2:1`) (agile, backstabber, deadly d6, finesse), **Damage** 1d4+1 piercing"
  - name: "Melee strike"
    desc: "Filcher's Fork +9 (`pf2:1`) (agile, backstabber, deadly d6, thrown 20), **Damage** 1d4+1 piercing"
spellcasting: []
abilities_bot:
  - name: "Graffiti Egg"
    desc: "`pf2:1` The halfling troublemaker throws an egg filled with paint, glitter, and confetti at a creature within 30 feet. The target must succeed a DC 17 [[Reflex]] save saving throw or become [[Dazzled]] for 1 round (or 1 minute on a critical failure)."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

A halfling's bravado can sometimes lead them into trouble. These tricksters often roam in groups trying to one-up each other's last prank. While troublemakers rarely intend to kill, occasionally their pranks get out of hand.

Despite their small stature, a halfling can prove to be a mighty foe if you find yourself on the wrong side of their frying pan.

```statblock
creature: "Halfling Troublemaker"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
