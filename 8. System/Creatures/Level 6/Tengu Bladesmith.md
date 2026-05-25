---
type: creature
group: ["Humanoid", "Tengu"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Tengu Bladesmith"
level: "6"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Humanoid"
trait_02: "Tengu"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+14; [[Low-Light Vision]]"
languages: "Common, Tengu (plus two others)"
skills:
  - name: Skills
    desc: "Acrobatics +14, Athletics +16, Crafting +16, Deception +14, Intimidation +16, Tengu Lore +14"
abilityMods: ["+4", "+3", "+2", "+1", "+1", "+1"]
abilities_top: []
armorclass:
  - name: AC
    desc: "24; **Fort** +15, **Ref** +16, **Will** +11"
health:
  - name: HP
    desc: "100"
abilities_mid:
  - name: "Reactive Strike"
    desc: "`pf2:r` **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Cold Iron Wakizashi +15 (`pf2:1`) (agile, cold iron, deadly d8, versatile p), **Damage** 1d4+7 slashing"
  - name: "Melee strike"
    desc: "Katana +17 (`pf2:1`) (deadly d8, magical, two hand d10, versatile p), **Damage** 1d6+7 slashing plus 1d4 bleed"
  - name: "Melee strike"
    desc: "Beak +15 (`pf2:1`) (unarmed), **Damage** 1d6+7 piercing"
spellcasting: []
abilities_bot:
  - name: "Feinting Failure"
    desc: "`pf2:1` **Frequency** once per round <br>  <br> **Requirements** The tengu bladesmith's previous action this turn was a Strike that failed or critically failed <br>  <br> **Effect** The tengu bladesmith Strikes the same target, who is [[Off Guard]] against this attack. On a hit, the bladesmith deals 1d6 additional precision damage."
  - name: "Swirling Blade"
    desc: "`pf2:1` The tengu bladesmith Interacts to draw a weapon in the sword group, then attempts to `act disarm` a weapon held by a foe within reach. The weapon the tengu bladesmith draws gains the disarm trait for this attempt."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

With the tengu diaspora spreading across much of Golarion, their knowledge and tradition of blade crafting has been passed through the generations to those who show interest and aptitude. Many tengu bladesmiths have experience as warriors; others learn their sword craft to improve their knowledge and understanding of the weapons they produce.

Originally hailing from the continent of Tian Xia, tengu have spread across the globe. Though some staunchly uphold traditions, gazing at the sky from the tallest mountaintops, other tengu remain on the ground, adapting and blending into the societies in which they settle.

```statblock
creature: "Tengu Bladesmith"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
