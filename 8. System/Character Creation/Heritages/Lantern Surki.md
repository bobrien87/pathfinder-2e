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

The nodes in your abdomen are particularly luminous. You can use an Interact action to shed light from your abdomen in a 20-foot radius (and dim light for the next 20 feet). This is a magical light effect with a counteract rank equal to half your level rounded up. You can change the color of the light or extinguish it with another Interact action.

- **Evolution** Your abdominal nodes have evolved into a pair of secondary limbs that project a magical focusing lens. You gain the [[Lantern Beam]] action.
- **Evolution** Secondary light emitters grow from your shoulder nodes that flash in time with your lantern. You gain the [[Lantern Strobe]] action.

**Source:** `= this.source` (`= this.source-type`)
