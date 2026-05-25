---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Athamaru]]"]
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You've tended to your coral jewelry so well that you have formed a symbiotic relationship with it. The powerful filtration properties of this coral protect you from impurities. You gain a +1 status bonus to saving throws against poisons, and your flat check to remove persistent poison damage is DC 10 instead of DC 15, which is reduced to DC 5 if another creature uses a particularly appropriate action to help. You must submerge yourself in water once every 24 hours to hydrate your coral or you lose the bonuses granted by the symbiotes.

**Source:** `= this.source` (`= this.source-type`)
