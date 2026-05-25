---
type: action
source-type: "Remaster"
traits: ["[[Spirit]]", "[[Transcendence]]"]
cast: "`pf2:1`"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Requirements** Your previous action was an unsuccessful Strike with the weapon from the [[Shadow Sheath]]

**Effect** The shadow weapon you threw fades, the distraction covering your true intention all along—a second strike in hidden in the blind spot of the first! Interact to draw another weapon from the shadow sheath, then Strike with it at the same multiple attack penalty as the unsuccessful attack. The opponent is [[Off Guard]] to this attack.

This Strike counts toward your multiple attack penalty as normal. After the Strike resolves, you can Interact to draw another weapon from the shadow sheath.

**Source:** `= this.source` (`= this.source-type`)
