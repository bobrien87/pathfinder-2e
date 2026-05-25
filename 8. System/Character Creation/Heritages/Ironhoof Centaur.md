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

Your hooves are incredibly strong and serve as formidable weapons. You gain a hoof unarmed attack that deals 1d6 bludgeoning damage. Your hooves are in the brawling group and have the finesse and unarmed traits.

**Source:** `= this.source` (`= this.source-type`)
