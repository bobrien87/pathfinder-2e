---
type: feat
source-type: "Remaster"
level: "9"
traits: ["[[Poppet]]"]
prerequisites: "tsukumogami poppet heritage"
frequency: "once per PT10M"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per 10 minutes

You bestow some of your own life energies to mend damage. You touch a non-magical object of 2 Bulk or less, or a magical object of 1 Bulk or less, and you @Damage[(2*@actor.level)[healing]]{restore Hit Points} to the target equal to twice your level. You lose as many Hit Points as the target regained. This direct transfer of vitality means that no effects apply that would increase the Hit Points the target regains or decrease the Hit Points you lose. This transfer also ignores any temporary Hit Points you or the target have. You can't reduce your Hit Points below 1 using Solidarity. You can't replace lost pieces or repair an object that has been completely destroyed.

**Special** If you have the [[Minuscule Mentee]] feat, you can use Solidarity to heal your familiar.

**Source:** `= this.source` (`= this.source-type`)
