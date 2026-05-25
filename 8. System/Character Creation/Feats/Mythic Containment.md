---
type: feat
source-type: "Remaster"
level: "10"
traits: ["[[Mythic]]"]
prerequisites: "Artisan's Calling"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You infuse a receptacle, such as a normal bag, sack, or box, with mythic power, transforming it into a prison into which you can command a creature. Spend a Mythic Point, and attempt a [[Deception]] check, [[Diplomacy]] check, or [[Intimidation]] check at mythic proficiency against the Will DC of a creature within 30 feet to trick, convince, or command it into entering the receptacle. The receptacle can hold a creature of any size, and the creature enters the receptacle if your check is successful. The creature is [[Grabbed]], is [[Slowed]] 1, and has to hold its breath or start suffocating. A creature trapped in the receptacle can attempt to [[Escape]]; use the skill you used to lure the creature into the bag for the DC, and calculate the DC using mythic proficiency. The trapped creature is automatically freed after 1 minute, but you can spend an additional Mythic Point as a free action to prolong the duration of the containment for an additional minute when it would expire.

**Source:** `= this.source` (`= this.source-type`)
