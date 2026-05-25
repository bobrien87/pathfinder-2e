---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "3"
traits: ["[[Concentrate]]", "[[Darkness]]", "[[Manipulate]]"]
cast: "`pf2:3`"
range: "30 feet"
duration: "1 minute"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You form a wall of pure darkness in a straight line up to 60 feet long and 10 feet high. You must create the wall in an unbroken open space so its edges don't pass through any creatures or objects, or the spell is lost. The wall stands vertically and, if you wish, can be of a shorter length or height. The wall prevents light from passing through and appears as a sheet of pure darkness to creatures observing it.

Creatures without darkvision or those unable to see through darkness can't see creatures on the other side of the wall. The wall is too thin for creatures to [[Hide]] in the darkness itself, but creatures can Hide from creatures on the other side of the wall as normal.

**Heightened (5th)** Creatures with darkvision (but not greater darkvision) can barely see through the wall. They treat targets seen through the wall as [[Concealed]].

**Heightened (7th)** Creatures with greater darkvision can barely see through the darkness. They treat targets seen through the wall as concealed. All other creatures are unable to see through the darkness at all.

**Source:** `= this.source` (`= this.source-type`)
