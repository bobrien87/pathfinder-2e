---
type: action
source-type: "Remaster"
traits: ["[[Transcendence]]"]
cast: "`pf2:3`"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

Make a Strike that deals slashing damage with your weapon ikon. If that Strike is successful, you can immediately make an additional Strike against a different target within your reach. You can continue making Strikes in this manner, each against a different target, until you have made a total of four Strikes or you miss with a Strike, whichever comes first. Each attack counts toward your multiple attack penalty, but you do not increase your penalty until you have made all your attacks.

**Source:** `= this.source` (`= this.source-type`)
