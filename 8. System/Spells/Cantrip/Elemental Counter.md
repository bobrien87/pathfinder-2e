---
type: spell
sub-type: "Cantrip"
source-type: "Remaster"
level: "1"
traits: ["[[Cantrip]]", "[[Concentrate]]"]
cast: "`pf2:r`"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

**Trigger** You or a creature within 60 feet rolls a saving throw against a spell with the earth, fire, metal, plant, water, or wood trait, or are targeted by a spell attack with such a trait.

**Requirements** You have a spell slot from which you could Cast a Spell of the triggering spell's countering element; see text.

Each element in the elemental cycle counters another, and you can use your elemental spells to protect against elements they counter. You lose your spell slot as if you had cast the triggering spell. You then attempt to counteract the triggering spell, using the rank of the spell you lost for the counteract rank. You can lose a plant or wood spell to counter earth, an earth spell to counter water, a water spell to counter fire, a fire spell to counter metal, or a metal spell to counter plant or wood.

**Source:** `= this.source` (`= this.source-type`)
