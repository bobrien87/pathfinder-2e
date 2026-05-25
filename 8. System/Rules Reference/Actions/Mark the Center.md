---
type: action
source-type: "Remaster"
traits: ["[[Transcendence]]"]
cast: "`pf2:1`"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

You hold a hand to your lips and exhale, releasing enchanted red ash in a @Template[type:cone|distance:15]. The ash clings to the vital areas of each enemy in the area for 1 minute. When a creature marked by the ash is hit and dealt damage by a Strike, it takes an additional 4d6 precision or vitality damage, then its mark ends. The damage type is whichever is worse for the creature, as determined by the GM. At 13th level and every 3 levels thereafter, the damage increases by 1d6.

**Source:** `= this.source` (`= this.source-type`)
