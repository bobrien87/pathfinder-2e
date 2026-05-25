---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "2"
traits: ["[[Manipulate]]", "[[Subtle]]", "[[Teleportation]]"]
cast: "`pf2:2`"
range: "60 feet"
targets: "1 unattended object of light Bulk or less"
source: "Pathfinder NPC Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You can pilfer an object even if it's outside the reach of your fingers. You teleport the target into one of your open hands. If you don't have a hand free, it falls to the ground at your feet.

**Heightened (3rd)** The range increases to 120 feet.

**Heightened (5th)** The range increases to 120 feet, and you can target an unattended object with a Bulk of 1 or less.

**Heightened (7th)** As 5th rank, and when you Cast the Spell you can spend 3 actions instead of 1 to increase the range to planetary. If you do, you don't need line of sight to the target, but you must be extremely familiar with the target.

**Source:** `= this.source` (`= this.source-type`)
