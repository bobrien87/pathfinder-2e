---
type: creature
group: ["Air", "Elemental"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Phade"
level: "7"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Air"
trait_02: "Elemental"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+16; [[Darkvision]]"
languages: "Sussuran"
skills:
  - name: Skills
    desc: "Acrobatics +16, Nature +15, Stealth +18, Survival +15"
abilityMods: ["+3", "+6", "+3", "+2", "+2", "+0"]
abilities_top:
  - name: "Sneak Attack"
    desc: "The phade deals 2d6 extra precision damage to [[Off Guard]] creatures."
armorclass:
  - name: AC
    desc: "26; **Fort** +14, **Ref** +18, **Will** +11"
health:
  - name: HP
    desc: "70; **Immunities** bleed, paralyzed, poison, sleep"
abilities_mid:
  - name: "Naturally Invisible"
    desc: "The phade is [[Invisible]] at all times, though when it takes a hostile action of any kind, it is [[Hidden]] instead of undetected until the start of its next turn, as the vague outline of its humanoid form is faintly visible for a short period of time."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Fist +18 (`pf2:1`) (agile, finesse, unarmed), **Damage** 1d10+5 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Hush"
    desc: "`pf2:1` The phade calms the air in a @Template[emanation|distance:30] until the beginning of its next turn, reducing sounds in it to a whisper that can't be heard outside the emanation. <br>  <br> This doesn't prevent casting spells, but a phade attempts to counteract any auditory or sonic effect originating in the area with a +17 counteract modifier. If the counteract attempt fails, Hush ends early."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

On the Plane of Air, and throughout the Inner Sphere, phades serve as spies and assassins for their creators. Even when summoned into the mortal Universe, phades are generally called for unsavory and violent purposes, giving the phades that have turned their back on their creator a poor opinion of mortals as well.

Hailing from the Plane of Air, these beings appear in a variety of sizes and shapes. They're noted for being elusive, swift, and often difficult to detect due to being composed primarily of air.

```statblock
creature: "Phade"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
