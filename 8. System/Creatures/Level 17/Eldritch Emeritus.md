---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Eldritch Emeritus"
level: "17"
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
    desc: "+32"
languages: "Common, Draconic (up to 6 additional languages)"
skills:
  - name: Skills
    desc: "Arcana +36, Intimidation +30, Nature +33, Occultism +33, Religion +33, Academia Lore +30"
abilityMods: ["+4", "+4", "+4", "+8", "+1", "-1"]
abilities_top:
  - name: "Constant Spells"
    desc: "A constant spell affects the monster without the monster needing to cast it, and its duration is unlimited. If a constant spell gets counteracted, the monster can reactivate it by spending the normal spellcasting actions the spell requires."
  - name: "Steady Spellcasting"
    desc: "If a reaction would disrupt the eldritch emeritus's spellcasting action, the eldritch emeritus attempts a DC 15 flat check. On a success, the action isn't disrupted"
armorclass:
  - name: AC
    desc: "39; **Fort** +27, **Ref** +27, **Will** +32"
health:
  - name: HP
    desc: "290"
abilities_mid:
  - name: "Counterspell"
    desc: "`pf2:r` **Trigger** A creature casts a spell the eldritch emeritus has prepared. <br>  <br> **Effect** The emeritus expends a prepared spell to counter the triggering creature's casting of that same spell. The emeritus loses their spell slot as if they had cast the triggering spell. The emeritus then attempts to counteract the triggering spell."
  - name: "Third Contingent Sequencer"
    desc: "`pf2:r` **Frequency** once per day <br>  <br> **Trigger** A creature attacks or uses a spell or ability that would affect the eldritch emeritus <br>  <br> **Effect** A masterpiece of complex spellwork instantly takes shape, casting [[Fire Shield]], [[Mislead]], and [[Mountain Resilience]] on the eldritch emeritus, each as an 8th-rank arcane spell."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Fist +30 (`pf2:1`) (agile, nonlethal, unarmed), **Damage** 1d4+14 bludgeoning"
  - name: "Melee strike"
    desc: "Staff +31 (`pf2:1`) (magical, two hand d8), **Damage** 3d4+14 bludgeoning"
  - name: "Ranged strike"
    desc: "Arcane Beam +31 (`pf2:1`) (arcane, fire, magical), **Damage** 6d6+10 fire"
spellcasting:
  - name: "Arcane Prepared Spells"
    desc: "DC 38, attack +30<br>**9th** (3 slots) [[Detonate Magic]], [[Falling Stars]], [[Energy Aegis]] (Constant)<br>**8th** (3 slots) [[Earthquake]], [[Quandary]], [[Quandary]]<br>**7th** (3 slots) [[Chain Lightning]], [[Chain Lightning]], [[Project Image]]<br>**6th** (3 slots) [[Disintegrate]], [[Teleport]], [[Wall of Force]]<br>**5th** (3 slots) [[Banishment]], [[Howling Blizzard]], [[Slither]]<br>**4th** (3 slots) [[Creation]], [[Dispel Magic]], [[Fly]]<br>**3rd** (3 slots) [[Earthbind]], [[Haste]], [[Locate]]<br>**2nd** (3 slots) [[Gecko Grip]], [[Translate]], [[Water Walk]]<br>**1st** (3 slots) [[Fleet Step]], [[Fleet Step]], [[Sure Strike]]<br>**Cantrips** [[Detect Magic]], [[Light]], [[Prestidigitation]], [[Sigil]], [[Telekinetic Hand]]"
abilities_bot:
  - name: "Didactic Arcanism"
    desc: "`pf2:1` `pf2:1` to `pf2:3` <br>  <br> **Requirements** The eldritch emeritus has seen a creature Cast a Spell of 7th rank or lower during the previous round, that spell takes between one and three actions to cast, and that spell is on the arcane spell list <br>  <br> **Effect** The eldritch emeritus mastered that spell 30 years ago, and is happy to show how a real master does it. The emeritus Casts the same Spell but heightened to 8th rank. Didactic Arcanism uses the same number of actions as the original spell took to cast."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

To outsiders, the eldritch emeritus looks something like a joke—a befuddled old scholar, their mind so stuffed with obscure theorems and abstract metaphysics that concerns about mere daily reality fade away. Those who know them, however, know that the eldritch emeritus wrote more treatises of spells than most wizards have had hot dinners, and if sufficiently annoyed, is entirely capable of providing a brief, thorough, and fatal demonstration.

True power comes from knowledge—the power to shape the growth of kingdoms by mere whispers, stay three steps ahead of adversaries, or even know which flora is best for creating untraceable poisons.

```statblock
creature: "Eldritch Emeritus"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
