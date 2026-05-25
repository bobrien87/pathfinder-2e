---
type: feat
source-type: "Remaster"
level: "6"
traits: ["[[Bard]]", "[[Concentrate]]"]
prerequisites: "Well-Versed"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** An ally benefiting from one of your composition spells is subject to an effect with the auditory, illusion, linguistic, sonic, or visual trait.

You tweak the properties of your composition spell to convey a bit of your defensive knowledge. All allies affected by your composition spell gain your +1 circumstance bonus from [[Well Versed]] until the start of your next turn. Teaching your allies also bolsters your own skills; your personal circumstance bonus from Well-Versed also increases to +2 until the start of your next turn.

> [!danger] Effect: Educate Allies

**Source:** `= this.source` (`= this.source-type`)
