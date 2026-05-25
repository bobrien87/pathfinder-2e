---
type: feat
source-type: "Remaster"
level: "17"
traits: ["[[Dragonblood]]"]
prerequisites: "draconic exemplar associated with a specific plane (such as a diabolic dragon or empyreal dragon)"
frequency: "once per P1W"
source: "Pathfinder Lost Omens Draconic Codex"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Twice per week, you can cast [[Interplanar Teleport]] as an innate spell of the tradition corresponding to your draconic exemplar. This can be used only to travel to the plane associated with your draconic exemplar (for instance, Heaven if your draconic nature is tied to an empyreal dragon) or from that plane to the Universe. Due to your draconic blood, your body serves as the locus, and you don't require a planar key. If there's any question about the plane to which your draconic exemplar is associated, the GM determines the answer.

**Source:** `= this.source` (`= this.source-type`)
