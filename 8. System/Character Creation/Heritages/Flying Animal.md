---
type: heritage
source-type: "Remaster"
ancestry: "[[8. System/Character Creation/Ancestries/Awakened Animal|Awakened Animal]]"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Heritage**
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Ancestry** " + this.ancestry`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "")`

You are an animal that can take flight for long or sustained bursts, such as an eagle, bat, bee, or flying squirrel.

The awakening process has disrupted your ability to fly as freely as you once did. What used to be an automatic process is now one that you must apply some thought to until it becomes automatic once again. You can still slow your descent, so you take no damage from falling, regardless of the distance you fall. Most flying awakened animals choose the Take Flight ancestry feat at 1st level to regain a limited ability to fly. You have a land Speed of 20 feet and one animal attack of your choice (typically beak, claw, jaws, talon, or wing).

**Source:** `= this.source` (`= this.source-type`)
