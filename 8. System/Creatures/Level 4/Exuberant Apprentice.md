---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Exuberant Apprentice"
level: "4"
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
    desc: "+11"
languages: "Common"
skills:
  - name: Skills
    desc: "Arcana +12, Academia Lore +10, Library Lore +12"
abilityMods: ["+1", "+2", "+2", "+4", "-2", "+4"]
abilities_top: []
armorclass:
  - name: AC
    desc: "20; **Fort** +10, **Ref** +10, **Will** +8"
health:
  - name: HP
    desc: "65"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Textbook +12 (`pf2:1`), **Damage** 1d6+5 bludgeoning"
  - name: "Melee strike"
    desc: "Fist +13 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4+5 bludgeoning"
spellcasting:
  - name: "Arcane Prepared Spells"
    desc: "DC 21, attack +13<br>**2nd** (3 slots) [[Acid Grip]], [[Darkvision]], [[Revealing Light]]<br>**1st** (4 slots) [[Force Barrage]], [[Grease]], [[Gust of Wind]], [[Phantasmal Minion]]<br>**Cantrips** [[Detect Magic]], [[Frostbite]], [[Prestidigitation]], [[Read Aura]], [[Telekinetic Hand]]"
abilities_bot:
  - name: "Overambitious Spell"
    desc: "`pf2:2` **Frequency** once per day <br>  <br> **Effect** The exuberant apprentice's teacher has told them they're not ready for this spell, but desperate times call for desperate measures. The exuberant apprentice attempts to cast [[Fireball]] as a 3rd-rank arcane spell but must first attempt a DC 11 flat check. <br> - **Critical Success** The spell is cast flawlessly and heightened to 4th rank. The apprentice is [[Stunned]] 2 from sheer shock. <br> - **Success** Nothing goes wrong, and the spell is cast normally. <br> - **Failure** The spell fizzles and creates only a harmless puff of smoke. <br> - **Critical Failure** Academic ablaze! The apprentice takes 6d6 fire damage as the magic backfires"
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Bright-eyed and bushy-tailed, these young mages seamlessly combine boundless curiosity, vigorous enthusiasm, and a complete lack of survival instincts.

True power comes from knowledge—the power to shape the growth of kingdoms by mere whispers, stay three steps ahead of adversaries, or even know which flora is best for creating untraceable poisons.

```statblock
creature: "Exuberant Apprentice"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
