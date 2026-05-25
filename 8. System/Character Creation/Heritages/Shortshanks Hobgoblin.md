---
type: heritage
source-type: "Remaster"
ancestry: "[[8. System/Character Creation/Ancestries/Hobgoblin|Hobgoblin]]"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Heritage**
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Ancestry** " + this.ancestry`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "")`

You have a longer torso and broader shoulders than most hobgoblins, making your legs seem short by comparison. This gives you a strong, muscular core and lowers your center of gravity—features that assist you in riding and climbing—and you've trained at riding in a saddle from an extremely early age. You gain the [[Ride]] feat. Additionally, you are not [[Off Guard]] while you Climb.

**Source:** `= this.source` (`= this.source-type`)
