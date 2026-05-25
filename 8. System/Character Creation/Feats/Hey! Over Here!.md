---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Venture Gossip|Venture Gossip]]"
source-type: "Remaster"
level: "6"
traits: ["[[Archetype]]", "[[Auditory]]"]
prerequisites: "Venture-Gossip Dedication"
source: "Paizo Blog: Foolish Housekeeping and Other Articles"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** An ally within 30 feet rolls a saving throw against an auditory effect.

Hey! Don't listen to that! That's bad sounds! Listen to me! Would you like to hear about how the high priest of the Abadaran church in Absalom's Petals District is having an affair with an Urgathoan cleric? Yeah, I'm thinking about calling the article "Boney Money!"

Your targeted ally treats the result of their saving throw as one degree of success better. Once an ally has been targeted by this effect, they're immune for 24 hours.

**Source:** `= this.source` (`= this.source-type`)
