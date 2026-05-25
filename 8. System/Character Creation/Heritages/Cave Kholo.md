---
type: heritage
source-type: "Remaster"
ancestry: "[[8. System/Character Creation/Ancestries/Kholo|Kholo]]"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Heritage**
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Ancestry** " + this.ancestry`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "")`

Storytellers spin ancient tales claiming that kholo lived in caves and underground before most of your kind ventured into the light. You're a throwback to these ancients, with a broad chest and markings that resemble short black slashes instead of spots. Your eyes are developed to see perfectly in the dark, a valuable advantage to your clan. You gain darkvision.

**Source:** `= this.source` (`= this.source-type`)
