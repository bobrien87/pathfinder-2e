---
type: feat
source-type: "Remaster"
level: "12"
traits: ["[[Wizard]]"]
prerequisites: "Counterspell, Quick Recognition"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You creatively apply your prepared spells to [[Counterspell]] a much wider variety of your opponents' magic. Instead of being able to counter a foe's spell with Counterspell only if you have that same spell prepared, you can use Counterspell as long as you have the spell the foe is casting in your spellbook. When you use Counterspell in this way, you must still expend a prepared spell; the prepared spell you expend must share a trait with the triggering spell other than concentrate, manipulate, or its tradition trait. The GM might allow you to instead use a spell that has an opposing trait or that otherwise logically would counter the triggering spell (such as using a cold or water spell to counter [[Fireball]] or using [[Clear Mind]] to counter a fear spell).

**Source:** `= this.source` (`= this.source-type`)
