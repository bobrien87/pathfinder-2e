---
type: heritage
source-type: "Remaster"
ancestry: "[[8. System/Character Creation/Ancestries/Kobold|Kobold]]"
traits: ["[[Kobold]]"]
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Heritage**
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Ancestry** " + this.ancestry`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "")`

Your connection to wise and celestial imperial dragons has led others to seek your advice. You can speak Draconic. Whenever you critically fail a Diplomacy check to [[Make an Impression]] or [[Request]], you get a failure instead.

**Source:** `= this.source` (`= this.source-type`)
