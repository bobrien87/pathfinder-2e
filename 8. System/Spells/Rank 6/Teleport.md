---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "6"
traits: ["[[Concentrate]]", "[[Manipulate]]", "[[Teleportation]]"]
cast: "10 minutes"
range: "100 miles"
targets: "you and up to 4 targets touched, either willing creatures or objects roughly the size of a creature."
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You and the targets are instantly transported to any location within range, as long as you can identify the location precisely both by its position relative to your starting position and by its appearance (or other identifying features). Incorrect knowledge of the location's appearance usually causes the spell to fail, but it could instead lead to teleporting to an unwanted location or some other unusual mishap determined by the GM. *Teleport* is not precise over great distances. The targets appear at a distance from the intended destination equal to roughly 1 percent of the total distance traveled, in a direction determined by the GM. For short journeys, this lack of precision is irrelevant, but for long distances this could be up to 1 mile.

**Heightened (7th)** You and the other targets can travel to any location within 1,000 miles.

**Heightened (8th)** You and the other targets can travel to any location on the same planet. If you travel more than 1,000 miles, you arrive only 10 miles off target.

**Heightened (9th)** You and the other targets can travel to any location on another planet within the same solar system. Assuming you have accurate knowledge of the location's position and appearance, you arrive on the new planet 100 miles off target.

**Heightened (10th)** As the 9th-rank version, but you and the other targets can travel to any planet within the same galaxy.

**Source:** `= this.source` (`= this.source-type`)
