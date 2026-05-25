---
type: heritage
source-type: "Remaster"
ancestry: "[[8. System/Character Creation/Ancestries/Dragonet|Dragonet]]"
source: "Pathfinder Lost Omens Draconic Codex"
---
### `= this.file.name`
**Heritage**
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Ancestry** " + this.ancestry`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "")`

You have bright blue and purple scales, with silvery teeth and claws. Your jaws count as silver and you gain a +1 circumstance bonus to damage rolls against fiends. You add Diabolic to your list of known languages.

**Source:** `= this.source` (`= this.source-type`)
