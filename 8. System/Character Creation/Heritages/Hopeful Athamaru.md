---
type: heritage
source-type: "Remaster"
ancestry: "[[8. System/Character Creation/Ancestries/Athamaru|Athamaru]]"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Heritage**
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Ancestry** " + this.ancestry`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "")`

You have begun to prepare yourself to become an athamaru matriarch, and are likely stepping outside of your community to better prepare yourself as a leader. As part of the physical change, you are substantially taller than you once were. Instead of Medium, your size is Large. In addition, you instill your allies with a feeling of hopefulness. You have a 10-foot aura that grants any ally in it a +1 circumstance bonus to saving throws against fear; this is an emotion and mental effect.

**Source:** `= this.source` (`= this.source-type`)
