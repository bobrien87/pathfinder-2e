---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Monk]]", "[[Stance]]", "[[Water]]"]
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

The lessons of the flood teach a stance that distributes and circulates a single breath through the body and allows your punches to contain the focused power of a torrent of water. While in this stance, you hold your breath for up to 10 minutes and leave the stance if you stop holding your breath. You do not lose additional air if you attack, are critically hit, or critically fail a save. You still lose all remaining air if you speak, including to Cast a Spell. The only Strikes you can make are flooded river unarmed attacks. These deal 1d8 bludgeoning damage; are in the brawling group; have the nonlethal, trip, unarmed, and water traits; and don't take the normal penalty for being used underwater. They also gain the forceful trait while you're underwater.

**Source:** `= this.source` (`= this.source-type`)
