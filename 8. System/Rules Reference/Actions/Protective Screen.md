---
type: action
source-type: "Remaster"
traits: ["[[Brandish]]", "[[Commander]]", "[[Tactic]]"]
cast: "`pf2:1`"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

You've trained your allies in a technique designed to protect war mages. Signal one squadmate; as a reaction, that squadmate Strides directly toward any other squadmate who is within the aura of your banner. If the first squadmate ends their movement adjacent to another squadmate, the second squadmate does not trigger reactions when casting spells or making ranged attacks until the end of their next turn or until they are no longer adjacent to the first squadmate, whichever comes first. If the first squadmate ends their movement adjacent to more than one other squadmate, the first squadmate must choose which of the adjacent squadmates gains this benefit.

**Source:** `= this.source` (`= this.source-type`)
