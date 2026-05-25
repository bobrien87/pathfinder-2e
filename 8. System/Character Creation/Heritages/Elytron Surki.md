---
type: heritage
source-type: "Remaster"
ancestry: "[[8. System/Character Creation/Ancestries/Surki|Surki]]"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Heritage**
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Ancestry** " + this.ancestry`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "")`

The top layer of your carapace is especially mobile, and you can unfurl it to catch the air gracefully as you fall. You take no damage from falling, regardless of the distance you fall.

- **Evolution** Your shoulder nodes have evolved into a pair of spines that you can energize to project a pair of glowing wings. You can cast [[Fly]] as an innate spell once per day, targeting yourself; while your wings are energized, you shed bright light in a 20-foot radius and dim light for the next 20 feet.

- **Evolution** Your shoulder nodes have evolved into a fan of thin membranes that resonate when magic is coursed through them. You gain the [[Stridulating Song]] action.

**Source:** `= this.source` (`= this.source-type`)
