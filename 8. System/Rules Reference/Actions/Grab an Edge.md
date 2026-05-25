---
type: action
source-type: "Remaster"
traits: ["[[Manipulate]]"]
cast: "`pf2:r`"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Trigger** You fall from or past an edge or handhold.

**Requirements** Your hands are not tied behind your back or otherwise restrained.

When you fall off or past an edge or other handhold, you can try to grab it, potentially stopping your fall. You must succeed at your choice of an Acrobatics check or a Reflex save, usually at the Climb DC. If you grab the edge or handhold, you can then [[Climb]] up using Athletics.
- **Critical Success** You grab the edge or handhold, whether or not you have a hand free, typically by using a suitable held item to catch yourself (catching a battle axe on a ledge, for example). You still take damage from the distance fallen so far, but you treat the fall as though it were 30 feet shorter.
- **Success** If you have at least one hand free, you grab the edge or handhold, stopping your fall. You still take damage from the distance fallen so far, but you treat the fall as though it were 20 feet shorter. If you have no hands free, you continue to fall as if you had failed the check.
- **Critical Failure** You continue to fall, and if you've fallen 20 feet or more before you use this reaction, you take 10 bludgeoning damage from the impact for every 20 feet fallen.

**Source:** `= this.source` (`= this.source-type`)
