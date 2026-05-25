---
type: heritage
source-type: "Remaster"
ancestry: "[[8. System/Character Creation/Ancestries/Yaksha|Yaksha]]"
traits: ["[[Plant]]", "[[Yaksha]]"]
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Heritage**
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Ancestry** " + this.ancestry`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "")`

You swore a vow to preserve the very foundation of sanctuary: the great earth and all that grows upon it. Your vow grants you the land's spiritual power; you gain one cantrip from the primal spell list. You can cast this spell as an innate primal spell at will. A cantrip is heightened to a spell rank equal to half your level rounded up. Your roots in the world grant you the plant trait.

**Additional Edict** cure or remove blight and pollution from the plants and soil you encounter

**Source:** `= this.source` (`= this.source-type`)
