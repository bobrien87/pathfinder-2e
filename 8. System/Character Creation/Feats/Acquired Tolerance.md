---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Poisoner|Poisoner]]"
source-type: "Remaster"
level: "8"
traits: ["[[Archetype]]", "[[Fortune]]"]
prerequisites: "Poisoner Dedication"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** You fail a save against a poison.

A small amount of poison, taken at nonlethal doses, can help the body build up resistance against a more deadly dosage. Reroll the triggering check and use the second result. Once you use Acquired Tolerance, you can continue to use it against the same type of poison that day, but you can't use it against a different type of poison until after you make your next daily preparations. For instance, if you used the reaction on a save against [[Giant Scorpion Venom]], you could use it again against giant scorpion venom even if it came from a different source, but you couldn't use it against [[Wyvern Poison]].

**Source:** `= this.source` (`= this.source-type`)
