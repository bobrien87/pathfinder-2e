---
type: heritage
source-type: "Remaster"
ancestry: "[[8. System/Character Creation/Ancestries/Merfolk|Merfolk]]"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Heritage**
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Ancestry** " + this.ancestry`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "")`

You're a merfolk of the open seas. Your tail is patterned after the silvery tuna and herring that school by the million in your hunting grounds. Water obeys your will, and with a quick word, you can draw a sheathe of it around you. You gain the [[Shielding Wave]] action.

**Source:** `= this.source` (`= this.source-type`)
