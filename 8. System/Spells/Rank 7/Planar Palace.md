---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "7"
traits: ["[[Concentrate]]", "[[Extradimensional]]", "[[Manipulate]]"]
cast: "1 minute"
range: "30 feet"
duration: "until the next time you make your daily preparations"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You grow an extradimensional demiplane consisting of a spacious dwelling with a single entrance. The entrance connects to the plane where you Cast the Spell, appearing anywhere within the spell's range as a faint, shimmering, vertical rectangle 5 feet wide and 10 feet high. You designate who can enter when you Cast the Spell. Once inside, you can shut the entrance, making it [[Invisible]]. You and the creatures you designated can reopen the door at will.

Inside, the demiplane appears to be a mansion featuring a magnificent foyer and numerous opulent chambers. The mansion can have any floor plan you imagine as you Cast the Spell, provided it fits within a space 40 feet wide, 40 feet deep, and 30 feet tall. While the entrance to the mansion is closed, effects from outside the mansion fail to penetrate it, and vice versa, except for [[Interplanar Teleport]], which can be used to enter the mansion. You can use scrying magic and similar effects to observe the outside only if they're capable of crossing planes.

A staff of up to 24 servants attends to anyone within the mansion. These are like the servant created by the [[Phantasmal Minion]] spell, though they're visible, with an appearance you determine during casting. The mansion is stocked with enough food to serve a nine-course banquet to 150 people.

**Source:** `= this.source` (`= this.source-type`)
