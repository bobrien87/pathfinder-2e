---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Globetrotting Scholar"
level: "13"
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
    desc: "+26"
languages: "Common (up to 5 additional languages)"
skills:
  - name: Skills
    desc: "Acrobatics +24, Athletics +27, Crafting +22, Nature +27, Stealth +24, Survival +27"
abilityMods: ["+3", "+4", "+3", "+3", "+1", "+3"]
abilities_top: []
armorclass:
  - name: AC
    desc: "33; **Fort** +23, **Ref** +26, **Will** +20"
health:
  - name: HP
    desc: "235"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Frost Dagger +25 (`pf2:1`) (agile, finesse, magical, versatile s), **Damage** 2d4+11 piercing plus 1d6 cold"
  - name: "Melee strike"
    desc: "Fist +24 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4+11 bludgeoning"
  - name: "Ranged strike"
    desc: "Flintlock Pistol +27 (`pf2:1`) (concussive, fatal d8, magical, reload 1, range 40 ft.), **Damage** 2d4+8 piercing plus 1d6 electricity"
spellcasting:
  - name: "Arcane Prepared Spells"
    desc: "DC 30, attack +22<br>**7th** (2 slots) [[Disintegrate]], [[Project Image]]<br>**6th** (2 slots) [[Mislead]], [[Thunderstrike]]<br>**5th** (1 slots) [[Sure Strike]]<br>**Cantrips** [[Detect Magic]], [[Figment]], [[Gouging Claw]], [[Ignition]], [[Tangle Vine]]"
abilities_bot:
  - name: "Following Spell"
    desc: "`pf2:1` **Frequency** once per round <br>  <br> **Requirements** The globetrotting scholar's last action was a successful Strike <br>  <br> **Effect** The globetrotting scholar immediately casts [[Gouging Claw]], [[Ignition]], or [[Tangle Vine]] at the target of the Strike."
  - name: "Magnificent…!"
    desc: "`pf2:1` The globetrotting scholar enthusiastically describes certain features of whatever dread horror they are currently facing, pointing out the weaknesses of a creature within 30 feet. The globetrotting scholar and all allies that can hear or see them gain a +1 status bonus to attack and damage rolls against that creature until the beginning of the globetrotting scholar's next turn. The scholar deals an extra 3d6 precision damage with their weapon and unarmed Strikes that hit that creature during the same duration. <br>  <br> > [!danger] Effect: Magnificent…!"
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

It takes a particular kind of personality to leave the creature comforts of academia in order to explore trap-ridden ancient tombs or observe man-eating monstrosities in their native habitats. The sort of personality that finds joy in the life cycle of parasitic wasps or recounts grisly Ghol-Gani sacrificial rites with a decidedly gruesome relish. Academia would not survive without such globetrotting scholars, but to their more sedate colleagues, they do tend to come off as an odd bunch.

True power comes from knowledge—the power to shape the growth of kingdoms by mere whispers, stay three steps ahead of adversaries, or even know which flora is best for creating untraceable poisons.

```statblock
creature: "Globetrotting Scholar"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
