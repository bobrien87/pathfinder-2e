---
type: feat
source-type: "Remaster"
level: "5"
traits: ["[[Merfolk]]"]
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Some legends claim that the flesh of a merfolk, if consumed, can grant health, longevity, and even immortality. For obvious reasons, merfolk prefer to discourage these rumors (with violence, if necessary), but you're living proof that there's at least a fraction of truth to such claims. When [[Administering First Aid]], [[Treating Disease]], or [[Treating Wounds]], you can take 1 damage to give someone a drop of your blood. When you do so, you don't need healer's tools, and you gain a +1 item bonus to your Medicine check.

If someone were to eat your heart and liver within an hour of your death, they would be healed of all physical injuries (regaining Hit Points up to their maximum) and would cease to age for 8 years.

**Source:** `= this.source` (`= this.source-type`)
