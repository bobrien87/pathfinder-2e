---
type: spell
sub-type: "Ritual"
source-type: "Remaster"
level: "5"
traits: ["[[Concentrate]]", "[[Manipulate]]", "[[Sanctified]]", "[[Spirit]]"]
cast: "`pf2:2`"
range: "120 feet"
duration: "1 minute (sustained)"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

A Medium guardian made of magical force appears in an unoccupied space in range. The spiritual guardian is translucent and wields a ghostly echo of one weapon you're wielding or wearing. If you have a deity, the guardian takes the form of one of your deity's attendants or servitors. If you sanctify the spell, the guardian's attacks are sanctified as well.

Creatures can move through the guardian's space but can't end their movement in it. You and your allies can flank with the guardian. The guardian doesn't have any other attributes a creature would normally have, aside from 50 Hit Points that it can't recover by any means and that it can lose only when protecting a creature (see below).

When you Cast the Spell and each time you Sustain it, you can have the guardian move to any unoccupied space within 120 feet of you and either attack or protect.

- **Attack** The guardian makes a melee spell attack against an adjacent creature, dealing 3d8 damage on a hit (or double damage on a critical hit). The damage type is the same as the chosen weapon (or any of its types for a versatile weapon). The attack deals spirit damage instead if that would be more detrimental to the creature (as determined by the GM). This attack uses and contributes to your multiple attack penalty.

- **Protect** The guardian protects a creature of your choice. Each time the chosen creature would take damage and the guardian is adjacent to it, the guardian takes the first 10 damage instead of the ally. This protection lasts until you command the guardian to attack or to protect a different creature, or the guardian is destroyed.

**Heightened (+2)** The guardian's damage increases by 1d8, and its Hit Points increase by 20.

**Source:** `= this.source` (`= this.source-type`)
