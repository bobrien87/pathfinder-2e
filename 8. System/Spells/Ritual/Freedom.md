---
type: spell
sub-type: "Ritual"
source-type: "Remaster"
level: "8"
traits: ["[[Mythic]]"]
cast: "1 day"
targets: "1 creature"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You perform a ritual to free a creature imprisoned, petrified, or otherwise put into stasis by any magical effects. You free them from all such effects, even effects like [[Imprisonment]] that don't have a duration, as long as *freedom*'s spell rank is equal to or higher than the effect's spell rank. To perform the ritual, you must be within 10 feet of the target, or within 10 feet of the place where the target was imprisoned (in the case of effects that trap the creature in an unreachable prison, like the oubliette form of *imprisonment*). You must know the name of the creature and details of its background; if the creature isn't a close associate, a failure or critical failure on a secondary [[Society]] check reduces even a critical success on the primary check to a failure.
- **Critical Success** You free the target from all magical effects imprisoning it, petrifying it, or putting it into stasis. It gains a +1 status bonus to saving throws to resist those same magical effects for 1 week.
- **Success** You free the target from all magical effects imprisoning it, petrifying it, or putting it into stasis.
- **Failure** You fail to free the target.
- **Critical Failure** The magical effects imprisoning the target, petrifying the target, or putting it into stasis affect you and all secondary casters.

**Source:** `= this.source` (`= this.source-type`)
