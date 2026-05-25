---
type: spell
sub-type: "Ritual"
source-type: "Remaster"
level: "4"
traits: ["[[Plant]]", "[[Vitality]]", "[[Wood]]"]
cast: "1 day"
duration: "1 year"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

**Area** 1/2-mile-radius circle centered on you

You cause the plants within the area to be healthier and more fruitful. In addition to other benefits of healthy plants, this increases the crop yield for farms, depending on your success. If you cast it in the area of a [[Blight]], *plant growth* attempts to counteract the *blight* instead of producing its usual effect.
- **Critical Success** Double the crop yield in the area, or increase the area to a 1-mile radius.
- **Success** Increase the crop yield in the area by one-third.
- **Failure** The ritual has no effect.
- **Critical Failure** The flora in the area changes in an unanticipated way, determined by the GM but generally as contradictory to your true desires as possible (for instance, blighting crops when you would prefer to enrich them).

**Source:** `= this.source` (`= this.source-type`)
