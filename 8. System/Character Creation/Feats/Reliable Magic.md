---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Avenging Runelord|Avenging Runelord]]"
source-type: "Remaster"
level: "14"
traits: ["[[Mythic]]"]
prerequisites: "Avenging Runelord Dedication"
source: "Pathfinder #219: Lord of the Trinity Star"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Magic stored in written form or within wands is more reliable in your capable hands. Whenever you overcharge a wand, reduce the DC of the flat check to avoid destroying the wand by 4. It still gains the broken condition on a success.

When you Cast a Spell from a scroll you can spend a Mythic Point as a free action. The spell is cast at mythic proficiency. Once you cast the spell using this ability, attempt a DC 11 flat check. If this check is successful, the scroll is not destroyed, and instead glows with light equivalent to that of a candle for 10 minutes. You can Cast a Spell from this scroll again, but if you do so you cannot enhance it in any way (such as by using this feat), and the scroll is destroyed. If not used before the end of the 10 minutes, the scroll is destroyed.

**Source:** `= this.source` (`= this.source-type`)
