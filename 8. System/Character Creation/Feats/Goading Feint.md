---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Swashbuckler]]"]
prerequisites: "trained in Deception"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your tricks make foes overextend their attacks. On a `act feint options=goading-feint`, you can use the following success and critical success effects instead of any other effects you would gain when you Feint; if you do, other abilities that adjust the normal effects of your Feint no longer apply. You can choose whether to use the Goading Feint benefits or the normal benefits each time you Feint a given foe.
- **Critical Success** The target takes a –2 circumstance penalty to all attack rolls against you before the end of its next turn.
- **Success** The target takes a –2 circumstance penalty to its next attack roll against you before the end of its next turn.

> [!danger] Effect: Goading Feint

**Source:** `= this.source` (`= this.source-type`)
