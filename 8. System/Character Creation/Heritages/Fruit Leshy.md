---
type: heritage
source-type: "Remaster"
ancestry: "[[8. System/Character Creation/Ancestries/Leshy|Leshy]]"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Heritage**
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Ancestry** " + this.ancestry`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "")`

Your body continually produces small fruits imbued with primal magic. At dawn each day, a new fruit ripens. You or an ally can remove this fruit as an Interact action. If a living creature that can derive sustenance from fruit consumes it as an Interact action within the next hour, they regain @Damage[(ceil(@actor.level/2))d8[vitality,healing]|shortLabel] Hit Points, plus an additional 1d8 Hit Points for every 2 of your levels beyond 1st. This effect has the healing and vitality traits.

**Source:** `= this.source` (`= this.source-type`)
