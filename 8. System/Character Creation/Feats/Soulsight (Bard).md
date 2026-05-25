---
type: feat
source-type: "Remaster"
level: "8"
traits: ["[[Bard]]"]
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your muse has opened your senses to the world beyond. You gain spiritsense as an imprecise sense with a range of 60 feet. Spiritsense enables you to sense the spirits of creatures, including living creatures, most non-mindless undead, and haunts within the listed range. As with your hearing and other imprecise senses, you still need to [[Seek]] to locate an undetected creature.

As spiritsense detects spiritual essence, not physical bodies, it can detect spirits projected by spells such as project image or possessing otherwise soulless objects. It can't detect soulless bodies, constructs, or objects, and like most senses, it doesn't penetrate through solid objects.

**Source:** `= this.source` (`= this.source-type`)
