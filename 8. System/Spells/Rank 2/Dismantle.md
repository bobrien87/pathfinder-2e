---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "2"
traits: ["[[Concentrate]]", "[[Manipulate]]"]
cast: "`pf2:2`"
range: "touch"
targets: "1 non-magical object in your possession of 1 Bulk or less"
duration: "1 minute"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You touch an object, and it immediately disassembles itself into its component pieces. The spell fails if the target lacks component pieces (such as a statue carved from one block of stone), and using it on a dangerous object like a snare or trap typically triggers it. The object gains the [[Broken]] condition, and the component pieces become small enough to be [[Hidden]] under normal clothing and armor. You can [[Dismiss]] the spell.

When the spell ends, the object reassembles itself into its original form, appearing in your hand or hands if you have them free, or on the ground in front of you otherwise. Once reassembled, the object loses the Broken condition and its Hit Points return to the value the object had when you [[Cast the Spell]].

**Heightened (4th)** The spell lasts for 10 minutes.

**Heightened (6th)** The spell lasts until your next daily preparations.

**Source:** `= this.source` (`= this.source-type`)
