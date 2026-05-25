---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Verduran Shadow|Verduran Shadow]]"
source-type: "Remaster"
level: "4"
traits: ["[[Archetype]]"]
prerequisites: "Verduran Shadow Dedication"
source: "Pathfinder #201: Pactbreaker"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You gain the [[Terrain Stalker]] feat, selecting the underbrush terrain; if you already have Terrain Stalker for underbrush, you can select a different type of difficult terrain. If you [[Avoid Notice]] while exploring, and if any allies use [[Follow the Expert]] to follow you as you do so, you can extend your Terrain Stalker feat's benefits to one ally so long as they remain within 10 feet of you. If you have master proficiency in Stealth, you can extend the effect to two allies. If you have legendary proficiency in Stealth, you can extend it to four allies.

**Source:** `= this.source` (`= this.source-type`)
