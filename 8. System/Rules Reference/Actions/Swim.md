---
type: action
source-type: "Remaster"
traits: ["[[Move]]"]
cast: "`pf2:1`"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

You attempt an Athletics check to move a maximum distance of 10 feet through water. The GM determines the DC based on the turbulence or danger of the water; in most instances of calm water, you get an automatic critical success. If your land Speed is 40 feet or higher, increase the maximum possible distance by 5 feet for every 20 feet of Speed above 20 feet.

If you end your turn in water and haven't succeeded at a Swim action that turn, you sink 10 feet or get moved by the current, as determined by the GM. This doesn't apply if your last action on your turn was to enter the water.
- **Critical Success** You move through the water, increasing the maximum distance by 5 feet.
- **Success** You move through the water.
- **Critical Failure** You make no progress. If you're holding your breath, you lose 1 round of air.

Sample Swim Tasks**Untrained** lake or other still water

**Trained** flowing water, like a river

**Expert** swiftly flowing river

**Master** stormy sea

**Legendary** maelstrom, waterfall

**Source:** `= this.source` (`= this.source-type`)
