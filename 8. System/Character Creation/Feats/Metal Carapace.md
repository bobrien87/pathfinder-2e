---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Impulse]]", "[[Kineticist]]", "[[Metal]]", "[[Primal]]"]
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Sheets of bent and rusted metal cover you in an armored shell. The carapace is medium armor but uses your highest armor proficiency. The carapace's statistics are: AC Bonus +3; Dex Cap +2; Check Penalty –2; Speed Penalty –5 feet; Strength +2; Bulk 2; Group plate; Armor Traits noisy. Any bonuses, runes, and magical abilities of your actual armor are suppressed, but any that could apply to the metal carapace are replicated onto it.

When you use this impulse, you can also create a rusty steel shield in a free hand, which uses the statistics of a regular steel shield. You can Shield Block with this shield even if you don't have that feat. The hand wielding this shield counts as a free hand for using impulses. The shield crumbles to flakes of rust if it becomes broken or leaves your grasp. The impulse lasts for 10 minutes, and you can Dismiss this impulse. If you use this impulse again, any existing one ends. The metal is rusted and fragile. If you take damage from a critical hit, the metal shatters and the impulse ends.

**Level (+3)** The shield's Hardness increases by 1, its HP by 4, and its BT by 2.

**Source:** `= this.source` (`= this.source-type`)
