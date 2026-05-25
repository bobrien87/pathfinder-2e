---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Sterling Dynamo|Sterling Dynamo]]"
source-type: "Remaster"
level: "10"
traits: ["[[Archetype]]"]
prerequisites: "Sterling Dynamo Dedication"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Access** You are from Arcadia.

You've incorporated beast tech from Arcadia into your dynamo, adding in components from various terrifying creatures to enhance your prosthesis's capabilities. The beast parts can unleash a disturbing howl as you make a powerful attack with your dynamo. Attempt Intimidation checks to [[Demoralize]] against each enemy within 30 feet; you don't take a penalty when you attempt to Demoralize a creature that doesn't understand your language. Then, make a dynamo Strike. Reduce the operational time of your sterling dynamo by 1 hour.

**Source:** `= this.source` (`= this.source-type`)
