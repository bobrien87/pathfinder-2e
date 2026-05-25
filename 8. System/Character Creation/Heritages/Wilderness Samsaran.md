---
type: heritage
source-type: "Remaster"
ancestry: "[[8. System/Character Creation/Ancestries/Samsaran|Samsaran]]"
traits: ["[[Samsaran]]"]
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Heritage**
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Ancestry** " + this.ancestry`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "")`

Your preceding lives have been reborn in various remote environments away from major settlements in Tian Xia and beyond. Your past manifestations have had to learn how to survive on their own, and you recall this will to survive while possessing very little resources. You become trained in Survival. If you would automatically become trained in Survival (from your background or class, for example), you instead become trained in a skill of your choice. You can ignore difficult terrain from trees, foliage, and undergrowth.

**Source:** `= this.source` (`= this.source-type`)
