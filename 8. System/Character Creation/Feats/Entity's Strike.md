---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Living Vessel|Living Vessel]]"
source-type: "Remaster"
level: "4"
traits: ["[[Archetype]]"]
prerequisites: "Living Vessel Dedication"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

The more you try to force your body to stay yours, the more it warps to channel the energy flowing through you. Whether you grow horns to match the wild hunt fey within you, develop a claw like that of the treachery demon sharing your soul, or feel a tentacle rip out of you from the outer being that imprinted itself on your psyche, the entity within you refuses to be contained. You gain an unarmed attack of your choice with its type determined by your entity. It deals 1d6 damage of a damage type appropriate for the unarmed attack (such as bludgeoning for the tentacle). This unarmed attack is in the brawling weapon group and has the agile, finesse, and magical traits.

**Source:** `= this.source` (`= this.source-type`)
