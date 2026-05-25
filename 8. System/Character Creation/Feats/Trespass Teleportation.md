---
type: feat
source-type: "Remaster"
level: "14"
traits: ["[[Occult]]", "[[Teleportation]]", "[[Thaumaturge]]"]
prerequisites: "Exploit Vulnerability"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You are benefiting from Exploit Vulnerability.

**Trigger** The target of your Exploit Vulnerability is within 120 feet and uses a teleportation effect.

You can hunt your foe to the ends of creation. You teleport along with the enemy, appearing the same direction and distance from it as you were before it teleported (or the nearest unoccupied space if your destination is occupied). Any allies affected by Share Weakness or Ubiquitous Weakness, if you have those abilities, can spend their reaction to teleport along with the enemy if they're within 120 of the enemy and choose to do so.

**Source:** `= this.source` (`= this.source-type`)
