---
type: feat
source-type: "Remaster"
level: "13"
traits: ["[[Lizardfolk]]"]
prerequisites: "Spirit Coffin"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your spirit coffin can temporarily detain the spirits of those you kill, allowing you to ask them one last question before they pass on. If you kill a creature with a slashing weapon, you can decapitate it and trap the spirit of its head in your spirit coffin. Once before your next daily preparations, you can cast [[Talking Corpse]] as a primal innate spell, which targets the spiritual head trapped in your coffin, not its physical corpse. A ghostly version of the head manifests from the coffin to answer the questions, taking a –2 status penalty to its Will save to resist the spell. After the spell resolves, or 1 day later, the head is released and rejoins its spiritual body. You can trap only one spirit in this way at a time.

**Source:** `= this.source` (`= this.source-type`)
