---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Rivethun Involutionist|Rivethun Involutionist]]"
source-type: "Remaster"
level: "14"
traits: ["[[Archetype]]"]
prerequisites: "Spirit Companion, Incredible Companion"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your animal companion gains a unique specialization, spirit-blessed. Thanks to the blessing bestowed upon it by the spirits of this world. If your animal companion already has the spirit-blessed specialization, it gains one additional specialization of your choice.

**Spirit-blessed:** Your companion is capable of harming wayward spirits, ghosts, and other incorporeal creatures as easy as if they were made of flesh and bone. Your companion's Strikes all gain the effects of the ghost touch property rune.

**Special** You can select this feat up to three times. Each time, add a different specialization to your companion. It's first specialization must be spirit-blessed.

**Source:** `= this.source` (`= this.source-type`)
