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

As a fearsome shark merfolk, your lower body is similar to that of one of the apex predators of the ocean. Like a shark, you can smell blood from quite a distance. You gain scent as an imprecise sense with a range of 30 feet. However, you can smell spilled blood at a range of 120 feet in the air and 500 feet in the water.

**Source:** `= this.source` (`= this.source-type`)
