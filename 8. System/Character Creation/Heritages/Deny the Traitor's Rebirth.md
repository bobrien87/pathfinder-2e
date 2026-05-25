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

You swore a vow to deliver others from rakshasas and asuras, whom yaksha legends have condemned as corrupted kin. To counter their shadowy schemes, your vow grants you darkvision and a +1 circumstance bonus to Perception checks to [[Seek]] or [[Sense the Motives]] of rakshasas and asuras.

**Additional Edict** confront rakshasas and asuras you come across (as long as you have a reasonable chance of success); in the unlikely event you find a benevolent rakshasa or asura, you don't have to confront them

**Source:** `= this.source` (`= this.source-type`)
