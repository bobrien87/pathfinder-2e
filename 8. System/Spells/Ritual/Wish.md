---
type: spell
sub-type: "Ritual"
source-type: "Remaster"
level: "10"
cast: "1 day"
range: "10 feet"
targets: "1 creature"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You weave the fabric of reality itself to grant the target's greatest desire. The target declares their wish in a loud voice at the start of the ritual and again at the end. The target's wish can be anything, ranging from simpler wishes such as vast riches or the casting of a certain spell or ritual, to greater wishes like the destruction of an entire kingdom or ascension to divinity. The GM might decide a wish draws the attention of deities or other powerful creatures, leading to interference with the ritual or attempts to undo the wish. The power of the ritual alters reality to such a degree that even deities can't outright undo the wish, but they can react to the wish by sending servitors to take away the newly acquired riches, for example.
- **Critical Success** The wish is granted without complication or drawbacks.
- **Success** The wish is granted, but with unintended consequences or side effects, such as taking riches from a well-known criminal, stirring a damaged kingdom to war, or angering rival gods.
- **Failure** The wish fails and has no result. The GM can instead have the wish be partially granted, but to such a lesser degree that the target will be eternally unsatisfied.
- **Critical Failure** The wish is corrupted, resulting in a cruel fulfillment. The GM determines the full results, but the outcome is generally ironic in some nature, such as becoming trapped in an underground vault full of riches, being transported to the kingdom as it's destroyed, or achieving divinity within an inaccessible demiplane.

**Source:** `= this.source` (`= this.source-type`)
