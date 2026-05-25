---
type: feat
source-type: "Remaster"
level: "17"
traits: ["[[Tanuki]]"]
frequency: "once per day"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

No distance can stop tanuki from making their way to a good party. You whistle and point, and 808 tanuki, in their raccoon dog forms, somehow appear from the surrounding terrain and fill a @Template[type:burst|distance:30] within 120 feet. The tanuki scurry over the ground, leap through the air, and climb up walls and surfaces, dealing @Damage[6d8[bludgeoning]|options:area-damage] damage to all enemies in the area as they're trampled and danced upon. The tanuki continue to party in the area for the next minute, dealing @Damage[3d8[bludgeoning]|options:area-damage] damage to any enemy that ends its turn in the area and transforming the area into difficult terrain (though the tanuki allow you and your allies to pass normally). Creatures in raccoon dog form can attempt to [[Hide]] within the mass of tanuki. After 1 minute, the tanuki clap 30 times and run off to the next party. You can Dismiss the effect, though if you do, the tanuki grumble as the party ends early.

**Source:** `= this.source` (`= this.source-type`)
