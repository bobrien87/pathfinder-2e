---
type: creature
group: ["Animal"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Experienced Hound"
level: "7"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Animal"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+16; [[Low-Light Vision]], [[Scent]] (imprecise) 60 feet"
languages: ""
skills:
  - name: Skills
    desc: "Acrobatics +15, Athletics +17, Stealth +15, Survival +12"
abilityMods: ["+5", "+5", "+4", "-4", "+2", "+0"]
abilities_top:
  - name: "Humane Bite"
    desc: "The experienced hound doesn't take a penalty to make a nonlethal attack with its jaws."
  - name: "Pack Attack"
    desc: "The hound's Strikes deal 2d6 extra damage to creatures within the reach of at least two of the hound's allies."
armorclass:
  - name: AC
    desc: "24; **Fort** +15, **Ref** +14, **Will** +12"
health:
  - name: HP
    desc: "115"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +16 (`pf2:1`) (unarmed), **Damage** 2d6+9 piercing plus [[Knockdown]]"
spellcasting: []
abilities_bot:
  - name: "Drag"
    desc: "`pf2:1` **Requirements** The experienced hound is adjacent to a [[Prone]] creature <br>  <br> **Effect** The experienced hound attempts an Athletics check to `act grapple` the prone creature. The experienced hound can then Step away from the target; if the target is [[Grabbed]] by the hound, it is moved into the hound's previous square and remains grabbed."
  - name: "Knockdown"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Knockdown in its damage entry <br>  <br> **Effect** The monster attempts to `act trip` the creature. This attempt neither applies nor counts toward the monster's multiple attack penalty."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

An experienced hound has been on dozens of hunts. They are often raised from pups to catch the scents of certain animals and deliver their bodies unharmed when taken down by their owners. An experienced hound could accompany a hunter or other NPC who specializes in tracking down prey.

```statblock
creature: "Experienced Hound"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
