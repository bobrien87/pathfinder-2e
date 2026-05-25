---
type: spell
sub-type: "Ritual"
source-type: "Remaster"
level: "4"
traits: ["[[Plant]]", "[[Void]]"]
cast: "1 day"
duration: "1 year"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

**Area** 1/2-mile-radius circle centered on you

You twist and stunt plants in the area, causing them to wither. In addition to other dangers from failing plant life, this decreases the crop yield for farms. If you cast this ritual in an area affected by *plant growth*, *blight* attempts to counteract *plant growth* instead of producing its usual effect.
- **Critical Success** Completely spoil the crop yield in the area, or decrease the yield by half in an area with up to a 1-mile radius.
- **Success** Decease the crop yield in the area by half.
- **Failure** The ritual has no effect.
- **Critical Failure** The flora in the area changes in an unexpected way, determined by the GM but generally as contradictory to your true desires as possible (for instance, enriching crops when you would prefer to blight them).

**Source:** `= this.source` (`= this.source-type`)
