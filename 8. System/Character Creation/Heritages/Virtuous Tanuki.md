---
type: heritage
source-type: "Remaster"
ancestry: "[[8. System/Character Creation/Ancestries/Tanuki|Tanuki]]"
traits: ["[[Tanuki]]"]
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Heritage**
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Ancestry** " + this.ancestry`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "")`

Many tanuki carry a gourd of alcohol to remind themselves to act with virtue, and by these standards, you're quite virtuous indeed. You gain poison resistance equal to half your level (minimum 1). You can eat and drink things when you're [[Sickened]]. You can't become incapacitated by conventional alcohol if you don't wish to be.

**Source:** `= this.source` (`= this.source-type`)
