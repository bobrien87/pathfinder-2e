---
type: heritage
source-type: "Remaster"
ancestry: "[[8. System/Character Creation/Ancestries/Hobgoblin|Hobgoblin]]"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Heritage**
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Ancestry** " + this.ancestry`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "")`

You come from a line of wandering mercenaries constantly on the march and scavenging food on the trail. If you fail, but don't critically fail, to [[Subsist]] in the wilderness, you can still keep yourself fed with poor meals. When exploring, you can [[Hustle]] twice as long before you have to stop.

**Source:** `= this.source` (`= this.source-type`)
