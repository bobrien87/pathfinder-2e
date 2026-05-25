---
type: feat
source-type: "Remaster"
level: "4"
traits: ["[[Concentrate]]", "[[Prediction]]", "[[Witch]]"]
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** A creature within 30 feet is reduced to 0 Hit Points in a way that doesn't destroy their body.

Although the divinations of a haruspex traditionally require organs and lengthy interpretation, you've learned how to glimpse the future in a more simple fashion by reading creatures' wounds. The glimpse of the future gives guidance on what tools are best to use next. Roll `r 1d12` to determine the damage type favored by your prediction. The next time before the end of your next turn that you or your allies deals that damage type to an enemy, that enemy has weakness equal to your level against that damage.

> [!danger] Effect: Portents of the Haruspex

D12Damage Type1acid2-3bludgeoning4cold5electricity6fire7mental8-9piercing10poison11-12slashing

**Source:** `= this.source` (`= this.source-type`)
