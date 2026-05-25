---
type: spell
sub-type: "Ritual"
source-type: "Remaster"
level: "3"
traits: ["[[Trial]]"]
cast: "1 day"
source: "Pathfinder Lost Omens Tian Xia World Guide"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

To many, the animals of Tian Xia are simply beasts to be conquered or harvested, but this isn't how all of the gods intended it. You approach, feed, and commune with the most notably hostile beasts in an effort to forge a true friendship and allegiance with the natural world.

Wantonly attacking or killing animals is anathema to this ritual and immediately ends its benefits. If the ritual is ended in this way, you must conduct an [[Atone]] ritual before attempting this ritual again.
- **Critical Success** As success, except you can instead resolve a conflict with one animal of level 15 or higher.
- **Success** You declare your allegiance to the wild and are bound by the ritual's anathema, but you still must prove yourself. Once you've nonviolently resolved conflicts with three different animals of a higher level than yours, you gain the [[Animal Empathy]] feat.
- **Failure** Your actions don't impress the gods of the wilds.
- **Critical Failure** You deeply offend the gods you were trying to impress, and they send a sign of displeasure, often an animal attack. You must conduct an *atone* ritual before attempting this ritual again.

**Source:** `= this.source` (`= this.source-type`)
