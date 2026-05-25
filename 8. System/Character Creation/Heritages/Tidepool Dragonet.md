---
type: heritage
source-type: "Remaster"
ancestry: "[[8. System/Character Creation/Ancestries/Dragonet|Dragonet]]"
traits: ["[[Amphibious]]"]
source: "Pathfinder Lost Omens Draconic Codex"
---
### `= this.file.name`
**Heritage**
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Ancestry** " + this.ancestry`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "")`

You have a slender, eel-like body with azure scales. Your wings sweep along your body like massive fins, making you well suited for watery terrain.

You gain the amphibious trait, and a swim Speed of 15 feet. You add Thalassic to your list of known languages.

**Source:** `= this.source` (`= this.source-type`)
