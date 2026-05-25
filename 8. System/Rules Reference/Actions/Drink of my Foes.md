---
type: action
source-type: "Remaster"
traits: ["[[Healing]]", "[[Transcendence]]", "[[Vitality]]"]
cast: "`pf2:1`"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Requirements** Your last action was a successful Strike with the [[Barrow's Edge]]

**Effect** Your blade glows as it absorbs your foe's vitality. You regain Hit Points equal to half the damage dealt.

**Source:** `= this.source` (`= this.source-type`)
