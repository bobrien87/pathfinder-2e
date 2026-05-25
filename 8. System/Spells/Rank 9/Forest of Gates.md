---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "9"
traits: ["[[Concentrate]]", "[[Manipulate]]", "[[Teleportation]]"]
cast: "10 minutes"
range: "1000 miles"
targets: "you and up to 6 willing creatures"
duration: "1 hour"
source: "Pathfinder Lost Omens Shining Kingdoms"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You transport yourself and your allies to a peaceful extraplanar realm of towering trees, each of which holds a misty gateway to another location. When you Cast this Spell, you choose a specific destination within 1,000 miles that you can identify by its position relative to your starting position and by its appearance (or other identifying features). Incorrect knowledge of the location causes the spell to fail. You and your allies walk for 1 hour through the forest, and each of you regains Hit Points and reduces the value of any doomed or drained condition as if you'd taken a full night's rest. At the end of the journey, you attempt a DC 40 [[Arcana]] check or DC 40 [[Nature]] check to find the correct gate to your desired location.
- **Critical Success** You and your allies arrive within 1,000 feet of your desired location.
- **Success** You and your allies arrive within 1 mile of your desired location.
- **Failure** You and your allies arrive within 10 miles of your desired location.
- **Critical Failure** You and your allies exit the forest within 1 mile of your original location.

**Source:** `= this.source` (`= this.source-type`)
