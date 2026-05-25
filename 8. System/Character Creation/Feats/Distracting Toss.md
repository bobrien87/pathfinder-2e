---
type: feat
source-type: "Remaster"
level: "8"
traits: ["[[Bravado]]", "[[Flourish]]", "[[Swashbuckler]]"]
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You toss one weapon into the air as a distraction as you throw another. Choose a creature within 30 feet and `act feint traits=bravado` against it; you can attempt this Feint even if the target is not within melee range, and if the target becomes [[Off Guard]] as a result of the Feint, this applies to your thrown weapon attacks for the duration.

Regardless of the result, you can then Interact to draw a thrown weapon and make a thrown weapon Strike against the target. If you have an open hand, you then catch the weapon you originally tossed into the air unless you critically failed at your attempt to Feint, in which case it lands on the ground at your feet.

**Source:** `= this.source` (`= this.source-type`)
