---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Thlipit Contestant|Thlipit Contestant]]"
source-type: "Remaster"
level: "4"
traits: ["[[Archetype]]", "[[Attack]]"]
prerequisites: "Thlipit Contestant Dedication, trained in Athletics"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** The target can't be more than one size larger than you.

You quickly wrap your lash around an opponent and pull them toward you. Attempt an `act grapple` check against the Fortitude DC of a target within your lash's reach.
- **Critical Success** You pull the target to any open space adjacent to you.
- **Success** You pull the target to the nearest open space adjacent to you.
- **Critical Failure** You misjudge your leverage and fall [[Prone]].

**Special** If you have the Titan Wrestler feat, you can target a creature up to two sizes larger than you, or up to three sizes larger than you if you're legendary in Athletics.

**Source:** `= this.source` (`= this.source-type`)
