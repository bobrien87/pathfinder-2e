---
type: feat
source-type: "Remaster"
level: "1"
source: "Paizo Blog: Foolish Housekeeping and Other Articles"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Whenever you take a move action to Stride, you can attempt a DC 15 [[Acrobatics]] check to roll forward.
- **Critical Success** You gain 5 extra feet of movement to your Speeds and can move through solid obstacles such as walls until the end of your Stride action.
- **Success** You gain 5 extra feet of movement to your Speeds until the end of your Stride action.
- **Failure** You lose 5 feet of movement from your Speeds until the end of your Stride action.
- **Critical Failure** Your character softlocks and is [[Paralyzed]] permanently. Only a [[Wish]] ritual or similar magic can reverse this effect.

**Source:** `= this.source` (`= this.source-type`)
