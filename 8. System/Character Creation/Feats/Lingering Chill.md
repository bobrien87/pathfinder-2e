---
type: feat
source-type: "Remaster"
level: "4"
traits: ["[[Aftermath]]", "[[Cold]]", "[[Primal]]"]
prerequisites: "You've been brought to 0 Hit Points by an enemy that has the cold trait or an enemy's ability that has the cold trait."
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

The chill of ice entered your veins and never left, adjusting the internal temperature of your body. Your breath comes out in puffs, and your skin is as cold and smooth as the ice in your veins. You can cast [[Frostbite]] as a primal innate cantrip. You gain resistance to cold damage equal to half your level, and you're protected from severe cold temperatures.

**Source:** `= this.source` (`= this.source-type`)
