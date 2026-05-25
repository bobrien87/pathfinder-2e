---
type: creature
group: ["Clockwork", "Construct"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Clockwork Mage"
level: "9"
rare_01: "Uncommon"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Clockwork"
trait_02: "Construct"
trait_03: "Mindless"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+17; [[Darkvision]]"
languages: ""
skills:
  - name: Skills
    desc: "Acrobatics +17"
abilityMods: ["+2", "+6", "+4", "-5", "+2", "-5"]
abilities_top:
  - name: "Wind-Up"
    desc: "24 hours, DC 26 Thievery, standby <br>  <br> For a clockwork to act, it must be wound with a unique key by another creature. This takes 1 minute. Once wound, it remains operational for the listed amount of time, usually 24 hours, after which time it becomes unaware of its surroundings and can't act until it's wound again. Some clockworks' abilities require them to spend some of their remaining operational time. They can't spend more than they have and shut down immediately once they have 0 time remaining. If it's unclear when a clockwork was last wound, most clockwork keepers wind all their clockworks at a set time, typically 8 a.m. <br>  <br> A clockwork that lists standby in its wind-up entry can enter standby mode as a 3-action activity. Its operational time doesn't decrease in standby, but it can sense its surroundings (with a -2 penalty to Perception). It can't act, with one exception: when it perceives a creature, it can exit standby as a reaction (rolling initiative if appropriate). <br>  <br> A creature can attempt to [[Disable a Device]] to wind a clockwork down (with a DC listed in the wind-up entry). For each success, the clockwork loses 1 hour of operational time. This can be done even if the clockwork is in standby mode."
armorclass:
  - name: AC
    desc: "27; **Fort** +17, **Ref** +19, **Will** +17"
health:
  - name: HP
    desc: "115; **Weaknesses** electricity 10, orichalcum 10; **Resistances** physical 5 except adamantine, orichalcum"
abilities_mid:
  - name: "Clockwork Wand"
    desc: "The clockwork mage uses a mechanical wand as a focus to channel magical energy. This wand is built into the clockwork mage's chest, with only the crystal at the end exposed. The mage can Interact to the remove the wand, or someone else can remove it with a DC 31 Thievery check to [[Disable a Device]]. The clockwork mage becomes unable to cast any spells except cantrips while the wand is removed. <br>  <br> When removed, the clockwork wand is a *[[Magic Wand]]* containing the last 2nd-rank innate spell the clockwork mage cast (the GM determines the spell randomly if it has not cast any eligible spells). The spells are placed within the wand while the mage is created, and the creator can substitute other arcane spells of the appropriate rank."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Fist +19 (`pf2:1`) (agile, finesse, unarmed), **Damage** 2d10+6 bludgeoning"
spellcasting:
  - name: "Arcane Innate Spells"
    desc: "DC 28, attack +20<br>**5th** [[Howling Blizzard]], [[Slither]]<br>**4th** [[Flicker]], [[Fly]], [[Wall of Fire]]<br>**3rd** [[Aqueous Orb]], [[Haste]]<br>**2nd** [[Invisibility]], [[Mist]], [[Revealing Light]], [[Web]]<br>**1st** [[Carryall]], [[Daze]], [[Detect Magic]], [[Frostbite]], [[Gentle Landing]], [[Grease]], [[Shield]], [[Tangle Vine]]"
abilities_bot:
  - name: "Energize Clockwork Wand"
    desc: "`pf2:1` **Frequency** once per 10 minutes. <br>  <br> **Effect** The clockwork mage regains a spell it has already cast that day. It must spend 1 hour of its operational time, or 2 hours if the spell is 3rd rank or higher."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

A clockwork mage is a lethal blend of magic and machinery. Each of these clockworks is imbued with an arcane stone at its core that powers spells through the wand embedded in its chest.

Intricate, complex machines, clockworks are built with care by highly skilled engineers. Though their creation involves some amount of magic, they're primarily mechanical, packed with precision-tuned gears and springs working in concert.

The sturdy mainspring within a clockwork must be wound to provide the energy needed to power the device. Some larger clockworks contain a series of springs for different limbs that each need to be wound. A clockwork's crafter creates a unique metal key while building the clockwork; winding the clockwork usually involves inserting the key into the machine's back and turning clockwise. Larger clockworks require greater strength to turn the key, and typically have larger keys to allow for more torque-some even accommodating a team of winders rather than an individual. Programming a clockwork requires both the key and the knowledge to set the program correctly, information usually reserved for the clockwork's creator or owner.

```statblock
creature: "Clockwork Mage"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
