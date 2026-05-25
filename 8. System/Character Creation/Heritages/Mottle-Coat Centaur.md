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

Your coat is mottled or striped, granting you natural camouflage in your home environment. Select a terrain from the following: arctic, desert, forest, mountain, plains, or swamp. In your selected terrain, you gain a +1 circumstance bonus to Stealth checks to [[Hide]] or [[Sneak]] and to Deception checks to [[Feint]].

**Source:** `= this.source` (`= this.source-type`)
