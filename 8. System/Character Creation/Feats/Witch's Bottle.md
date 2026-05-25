---
type: feat
source-type: "Remaster"
level: "8"
traits: ["[[Witch]]"]
prerequisites: "Cauldron"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You spend 10 minutes and 1 Focus Point brewing a special potion containing the power of one of your hexes that targets a creature. A creature that consumes this potion is targeted by the hex. If the hex has a sustained duration and you have [[Cackle]], you can cast *cackle* into the bottle just before you seal it. If you do, the hex's duration is extended as if you had cast cackle the round after the hex was cast (typically this extends the duration by 1 round). Your cackling laugh sounds out when the potion is unsealed.

Any potion you create this way loses its power the next time you make your daily preparations. While the potion is in your possession, you can render it inert using a single action that has the concentrate trait. You can't regain the Focus Point you spent to create the potion (or the Focus Point you spent to cast cackle) until the potion is consumed or loses its magic.

**Source:** `= this.source` (`= this.source-type`)
