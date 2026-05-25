---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Rose Warden|Rose Warden]]"
source-type: "Remaster"
level: "2"
traits: ["[[Archetype]]", "[[Dedication]]"]
prerequisites: "trained in Stealth, you worship Milani"
source: "Pathfinder Lost Omens Hellfire Dispatches"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

As a follower of the Everbloom, you stand up against tyranny and oppression, understanding that revolution against an unjust ruler must sometimes be enacted in secret. You become trained in Deception. If you're already trained in Deception, you become an expert in your choice of Deception or Stealth. When you get a critical success to Lie to a figure of authority, you gain a +1 circumstance bonus to your Fortitude DC and saving throws against being [[Confused]], [[Controlled]], [[Grabbed]], [[Immobilized]], or [[Restrained]] by that figure of authority for 24 hours.

You add the edicts and anathema of [[Milani]] to your own. Failing to uphold edicts or committing acts that violate the anathema result in you losing access to any abilities granted by this archetype, as determined by your GM. You can regain these lost abilities through the atone ritual as normal.

> [!danger] Effect: Rose Warden Dedication

Rose Warden

**Source:** `= this.source` (`= this.source-type`)
