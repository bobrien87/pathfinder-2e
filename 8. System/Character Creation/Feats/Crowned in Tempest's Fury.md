---
type: feat
source-type: "Remaster"
level: "18"
traits: ["[[Air]]", "[[Electricity]]", "[[Impulse]]", "[[Kineticist]]", "[[Primal]]", "[[Stance]]"]
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You become one with a devastating thunderstorm from the Plane of Air, placing a crown of lightning upon your brow. Sparks flash in your eyes, and lightning strikes constantly in the air around you as howling winds lift you from the ground.

- Any creature that enters your kinetic aura or ends its turn there takes 2d12 electricity damage.

- If you don't have a fly Speed, you gain a 20-foot fly Speed. If you have the Cyclonic Ascent impulse, you instead gain that fly Speed and the extra benefits.

- You gain a +10-foot status bonus to all your Speeds.

- Your air Elemental Blasts deal an additional 1d12 electricity damage.

**Source:** `= this.source` (`= this.source-type`)
