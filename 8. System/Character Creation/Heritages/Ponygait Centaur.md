---
type: heritage
source-type: "Remaster"
ancestry: "[[8. System/Character Creation/Ancestries/Centaur|Centaur]]"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Heritage**
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Ancestry** " + this.ancestry`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "")`

You are smaller than most other centaurs, though no less fleet of foot. Instead of Large, your size is Medium. You gain a +1 circumstance bonus to Reflex saving throws.

**Source:** `= this.source` (`= this.source-type`)
