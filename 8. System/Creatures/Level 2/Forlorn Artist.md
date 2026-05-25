---
type: creature
group: ["Elf", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Forlorn Artist"
level: "2"
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
    desc: "+7; [[Low-Light Vision]]"
languages: "Common, Elven (one regional language)"
skills:
  - name: Skills
    desc: "Crafting +11, Diplomacy +9, Society +8, Art Lore (+13 for visual arts) +11"
abilityMods: ["+0", "+3", "-1", "+4", "+1", "+3"]
abilities_top:
  - name: "+2 Bonus on Perception to Notice Unusual Artwork"
    desc: ""
  - name: "Art Specialist"
    desc: "For encounters involving crafting or evaluating art, the forlorn artist is a 4th-level challenge."
armorclass:
  - name: AC
    desc: "18; **Fort** +3, **Ref** +9, **Will** +9"
health:
  - name: HP
    desc: "26"
abilities_mid:
  - name: "+1 Circumstance vs. emotion effects"
    desc: ""
  - name: "Flick Ink"
    desc: "`pf2:r` **Trigger** The artist is targeted with a melee or ranged Strike by a creature within 15 feet <br>  <br> **Effect** The artist flings ink in the attacker's eyes. The attacker must succeed at a DC 18 [[Reflex]] save or be [[Blinded]]. This takes effect before the attacker targets the artist. The blindness lasts until the end of the target's next turn, but the creature can Interact to rub its eyes to attempt a new save to end the condition."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Rapier +9 (`pf2:1`) (deadly d8, disarm, finesse), **Damage** 1d6+4 piercing"
  - name: "Melee strike"
    desc: "Fist +9 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4+4 bludgeoning"
spellcasting:
  - name: "Arcane Innate Spells"
    desc: "DC 18, attack +10<br>**1st** [[Figment]], [[Prestidigitation]], [[Sigil]]"
abilities_bot:
  - name: "Cry of Ages"
    desc: "`pf2:1` The artist channels their loneliness into a wordless wail that forces others to contemplate their mortality. Each enemy in a @Template[type:emanation|distance:30] must succeed at a DC 17 [[Will]] save or be [[Frightened]] 1. A creature that critically fails is also [[Stupefied 1]] for 1 minute. Each creature is then temporarily immune for 1 minute."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Forlorn elves, who spend their lives among shorter-lived peoples, often grow morose from constant loss. Some channel this melancholy into their art.

Elves' long lives give them centuries to delve into studies, artistry, or exploration.

```statblock
creature: "Forlorn Artist"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
