---
type: action
source-type: "Remaster"
traits: ["[[Occult]]", "[[Shadow]]"]
cast: "`pf2:1`"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Frequency** once per minute

**Effect** You plunge your fist or weapon into your shadow, enveloping it in a rippling, damask-like pattern of darkness. If your next action is to Strike, the shadows cling to your foe with your attack, obscuring its vision. On a hit, the target of your Strike becomes [[Dazzled]] until the start of your next turn. The target can use an Interact action to tear away the clinging shadows and remove the dazzled condition. On a critical hit, the shadows are particularly stubborn and can't be torn away.

**Source:** `= this.source` (`= this.source-type`)
