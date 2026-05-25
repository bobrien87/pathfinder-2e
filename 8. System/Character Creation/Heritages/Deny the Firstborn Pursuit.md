---
type: heritage
source-type: "Remaster"
ancestry: "[[8. System/Character Creation/Ancestries/Yaksha|Yaksha]]"
traits: ["[[Yaksha]]"]
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Heritage**
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Ancestry** " + this.ancestry`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "")`

You swore a vow to shelter others from the First World's cruelties. Wise to fey's mind-affecting abilities, your vow grants mental resistance equal to half your level (minimum 1), and a +2 circumstance bonus to Nature checks to Recall Knowledge about fey.

**Additional Edict** confront cruel fey you encounter (as long as you have a reasonable chance of success)

**Source:** `= this.source` (`= this.source-type`)
