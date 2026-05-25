---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Mage Killer"
level: "8"
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
    desc: "+16"
languages: "Common"
skills:
  - name: Skills
    desc: "Acrobatics +17, Arcana +13, Athletics +16, Stealth +18"
abilityMods: ["+4", "+5", "+2", "+1", "+2", "+0"]
abilities_top:
  - name: "Magical Static"
    desc: "The mage killer's Strikes deal an additional 1d8 mental damage to a creature that has Cast (or attempted to Cast) a Spell within the last round, and on a critical hit, the creature is [[Stupefied 1]] for 1 minute."
armorclass:
  - name: AC
    desc: "25; **Fort** +16, **Ref** +17, **Will** +16"
health:
  - name: HP
    desc: "145"
abilities_mid:
  - name: "Spell Dodge"
    desc: "`pf2:r` **Trigger** The mage killer is targeted by a spell <br>  <br> **Effect** The mage killer gains a +2 circumstance bonus to AC and saving throws against the triggering spell."
  - name: "Spell Interception"
    desc: "`pf2:r` **Trigger** A creature within 10 feet of the mage killer Casts a Spell <br>  <br> **Effect** The mage killer makes a melee Strike or thrown dagger Strike against the triggering creature. If it hits, the spell is disrupted."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Dagger +19 (`pf2:1`) (agile, finesse, versatile s), **Damage** 1d4+10 piercing plus [[Magical Static]]"
  - name: "Melee strike"
    desc: "Dagger +19 (`pf2:1`) (agile, finesse, thrown 10, versatile s), **Damage** 1d4+10 piercing plus [[Magical Static]]"
  - name: "Melee strike"
    desc: "Rapier +20 (`pf2:1`) (deadly d8, disarm, finesse, magical), **Damage** 2d6+10 piercing plus [[Magical Static]]"
  - name: "Melee strike"
    desc: "Fist +19 (`pf2:1`) (agile, finesse, nonlethal, unarmed), **Damage** 1d4+10 bludgeoning plus [[Magical Static]]"
spellcasting: []
abilities_bot:
  - name: "Shift Energy Runes"
    desc: "`pf2:1` **Frequency** once per hour <br>  <br> **Effect** The mage killer alters the magical countermeasures in the runes on their armor. They change their resistance to the energy type of their choice (acid, cold, electricity, fire, force, sonic, vitality, or void)."
  - name: "Sudden Charge"
    desc: "`pf2:2` The mage killer Strides twice. If they end their movement within melee reach of at least one enemy, they can make a melee Strike against it."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Whenever high command needs an enemy spellcaster taken off the board in the midst of battle, they send in a mage killer.

Whether they're hired to wage war, protect a caravan, or infiltrate an impenetrable fortress, there's ample work for mercenaries all over Golarion.

```statblock
creature: "Mage Killer"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
