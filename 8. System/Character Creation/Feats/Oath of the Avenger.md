---
type: feat
source-type: "Remaster"
level: "2"
traits: ["[[Champion]]", "[[Oath]]"]
prerequisites: "lay on hands"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You've sworn an oath to punish wicked acts you witness. You gain the edict "hunt down those who have harmed innocents or committed heinous atrocities." When you see a creature harm an ally, an innocent, or a noncombatant, you can invoke your oath against that creature. Like speaking, this doesn't require an action. Most champions choose to invoke these oaths out loud if they're able. The invocation lasts indefinitely, though you can choose to end if you are satisfied that the target has reformed, atoned, or been forgiven.

You can use [[Lay on Hands]] to damage a creature you have invoked your oath against as if it were undead; in this case, *lay on hands* deals spirit damage instead of vitality damage, gains the spirit trait, and loses the vitality trait. This doesn't prevent you from healing such a creature with *lay on hands* if you so choose.

**Source:** `= this.source` (`= this.source-type`)
