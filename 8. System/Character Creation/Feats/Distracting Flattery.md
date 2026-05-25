---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Dandy|Dandy]]"
source-type: "Remaster"
level: "4"
traits: ["[[Archetype]]", "[[Skill]]"]
prerequisites: "Dandy Dedication, expert in Deception"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** You observe a target's attitude toward yourself or your allies decrease as a result of an ally's behavior.

You know how to maintain a good impression and manage your image, even while keeping uncouth company.

Make a [[Deception]] check against the target's Will DC. Regardless of your result, the target is temporarily immune to your Distracting Flattery for 10 minutes.
- **Success** The target's attitude doesn't decrease as a result of your ally's social blunder.
- **Failure** The target's attitude decreases, as normal.
- **Critical Failure** Your attempt makes matters worse, decreasing the target's attitude toward you by one step, in addition to any changes from the behavior that triggered this reaction.

**Source:** `= this.source` (`= this.source-type`)
