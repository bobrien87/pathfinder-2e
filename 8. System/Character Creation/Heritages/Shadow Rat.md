---
type: heritage
source-type: "Remaster"
ancestry: "[[8. System/Character Creation/Ancestries/Ratfolk|Ratfolk]]"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Heritage**
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Ancestry** " + this.ancestry`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "")`

Your ancestors lived in dark spaces underground, granting you dark fur and a vaguely unnatural mien. You gain the trained proficiency rank in Intimidation and can use Intimidation to [[Coerce]] animals. When you [[Demoralize]] an animal, you don't take a penalty for not sharing a language with it. If you would automatically become trained in Intimidation (from your background or class, for example), you become trained in another skill of your choice.

Animals' attitudes toward you begin one degree worse than normal, usually starting at unfriendly instead of indifferent for domesticated animals, and hostile instead of unfriendly for wild animals.

**Source:** `= this.source` (`= this.source-type`)
