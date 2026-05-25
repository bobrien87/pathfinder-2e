---
type: heritage
source-type: "Remaster"
ancestry: "[[8. System/Character Creation/Ancestries/Poppet|Poppet]]"
traits: ["[[Poppet]]"]
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Heritage**
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Ancestry** " + this.ancestry`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "")`

You have the form and memories of a common tool. Choose one Lore skill related to what kind of tool you were; for instance, Cooking Lore for a kitchen knife or spoon. You're trained in this skill, and you gain a +2 circumstance bonus to checks to Aid with this skill. If you take the [[Helpful Poppet]] feat, the bonus increases to +3.

While most poppets are made of stuffing, cloth, or soft metals, some tsukumogami are made of other materials, changing the poppet weakness to fire. If your body is primarily wood or cloth, you have the normal poppet weakness to fire. If your body is primarily metal, you're instead weak to electricity; if its primarily ceramic, you're instead weak to cold.

**Source:** `= this.source` (`= this.source-type`)
