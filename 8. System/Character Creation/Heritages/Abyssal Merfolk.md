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

You live far, far below the surface of the ocean. Your fish tail might resemble a viperfish or anglerfish, and you might have luminous eyes or translucent skin. Abyssal merfolk have an uncanny reputation, but they can exist in even the most lightless realms. You gain darkvision and are immune to the crushing pressure of the oceanic depths.

**Source:** `= this.source` (`= this.source-type`)
