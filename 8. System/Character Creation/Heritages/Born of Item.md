---
type: heritage
source-type: "Remaster"
ancestry: "[[8. System/Character Creation/Ancestries/Yaoguai|Yaoguai]]"
traits: ["[[Yaoguai]]"]
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Heritage**
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Ancestry** " + this.ancestry`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "")`

You were an object until the moon breathed life into you. Choose one Lore skill related to what kind of tool you were; for instance, Cooking Lore for a cleaver or Farming Lore for a rake. You become trained in this skill.

- **Humanoid Form** You retain memories of the tasks you performed as an object. You gain a +1 circumstance bonus to the Lore skill you obtained through this heritage.
- **Yaoguai Form** Your time as a mindless object makes it harder to affect you mentally. If you roll a success on a mental effect, you gain a critical success instead.

**Source:** `= this.source` (`= this.source-type`)
