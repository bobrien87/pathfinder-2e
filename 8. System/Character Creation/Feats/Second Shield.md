---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Viking|Viking]]"
source-type: "Remaster"
level: "6"
traits: ["[[Archetype]]"]
prerequisites: "Viking Dedication"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** Your [[Shield Block]] causes your shield to break or be destroyed.

You're used to your shield breaking in the middle of battle, and you're prepared to use a backup or any convenient nearby object to defend yourself.

You can [[Interact]] to draw a shield on your person or an unattended shield within your reach. If there is an object within your reach that could serve as an improvised shield-for example, a table or chair-you can Interact to draw it with this feat. The GM determines if something can be used as an improvised shield.

Your new shield isn't raised until you use the [[Raise a Shield]] action, as normal.

**Source:** `= this.source` (`= this.source-type`)
