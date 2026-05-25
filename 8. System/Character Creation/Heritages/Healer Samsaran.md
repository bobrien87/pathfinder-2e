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

In seeking enlightenment, your past incarnations have wandered away from the ancestral homelands of Zi Ha, exploring the different nations of Tian Xia and elsewhere in Golarion. Your past incarnations had dangerous encounters while traveling, and you frequently have flashbacks to healing wounds. You become trained in Medicine. If you would automatically become trained in Medicine (from your background or class, for example), you instead become trained in a skill of your choice.

When you use Medicine to [[Treat Wounds]] on yourself, you can use your special techniques to add your level to the Hit Points you regain from the treatment.

**Source:** `= this.source` (`= this.source-type`)
