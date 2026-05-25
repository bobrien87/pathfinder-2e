---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Mountaineer"
level: "5"
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
    desc: "+15"
languages: "Common, Petran, Pyric"
skills:
  - name: Skills
    desc: "Acrobatics +13, Athletics +13, Nature +12, Survival +12, Mountain Lore +15"
abilityMods: ["+4", "+3", "+2", "+0", "+3", "+0"]
abilities_top:
  - name: "Experienced Steps"
    desc: "A mountaineer isn't impeded by difficult terrain caused by snow or ice. They gain a +2 circumstance bonus to Acrobatics checks to [[Balance]] on slippery ice."
  - name: "Professional Climber"
    desc: "While climbing, the mountaineer can have up to five allies Following the Expert and grants a +3 circumstance bonus to Athletics checks to Climb."
  - name: "Arctic Passage"
    desc: "The mountaineer ignores difficult terrain caused by ice or snow."
armorclass:
  - name: AC
    desc: "21; **Fort** +14, **Ref** +12, **Will** +9"
health:
  - name: HP
    desc: "80"
abilities_mid:
  - name: "Lost My Footing"
    desc: "`pf2:r` **Frequency** once per day <br>  <br> **Trigger** The mountaineer critically fails a check to [[Balance]] or Climb <br>  <br> **Effect** Training kicks in, and the mountaineer catches themself, improving the check from a critical failure to a failure."
  - name: "Tuck and Roll"
    desc: "During an avalanche, the mountaineer gains a +2 circumstance bonus to their Reflex save against bludgeoning damage and natural disasters."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Pick +14 (`pf2:1`) (fatal d10), **Damage** 1d6+10 piercing"
  - name: "Melee strike"
    desc: "Hatchet +14 (`pf2:1`) (agile, sweep), **Damage** 1d6+10 slashing"
  - name: "Melee strike"
    desc: "Hatchet +13 (`pf2:1`) (agile, sweep, thrown 10), **Damage** 1d6+10 slashing"
  - name: "Melee strike"
    desc: "Fist +14 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4+10 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Chasm Crossing"
    desc: "`pf2:2` The mountaineer Strides twice and Leaps up to 20 feet horizontally."
  - name: "Team Awareness"
    desc: "`pf2:1` **Requirements** A creature is undetected by one or more of the mountaineer's allies but is observed by the mountaineer <br>  <br> **Effect** The mountaineer Points Out an enemy and makes a Strike against them."
  - name: "Quick Draw"
    desc: "`pf2:1` The mountaineer Interacts to draw their hatchet or pick, then Strikes with the weapon."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Mountaineers usually travel solo, but some guide expeditions into dangerous terrain.

Explorers are often well-equipped and well-trained for any type of hazard and are eager to lead others into the wild.

```statblock
creature: "Mountaineer"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
