---
type: heritage
source-type: "Remaster"
ancestry: "[[8. System/Character Creation/Ancestries/Dragonet|Dragonet]]"
traits: ["[[Fey]]"]
source: "Pathfinder Lost Omens Draconic Codex"
---
### `= this.file.name`
**Heritage**
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Ancestry** " + this.ancestry`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "")`

You have a brightly colored body with gleaming scales that become more lustrous as you age, and iridescent butterfly wings. You can change the coloration and pattern of your wings with a single action to let you blend into an area.

When your wings match your environment, you gain a +2 circumstance bonus to Stealth checks until your surroundings shift in coloration or pattern. You gain the fey trait and add Fey to your list of known languages.

**Source:** `= this.source` (`= this.source-type`)
