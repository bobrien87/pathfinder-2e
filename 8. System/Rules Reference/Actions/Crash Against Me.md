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

Your skin becomes virtually unbreakable. Until the start of your next turn, you have resistance equal to your level to the chosen damage type.

During this time, if a creature attacking you using a weapon dealing the same damage type as your resistance misses you or hits you but deals no damage due to your resistance, the weapon clangs wildly off your skin. This painful reverberation makes the attacking enemy [[Off Guard]] and gives it a –2 circumstance penalty to attacks with that weapon until the start of the enemy's next turn.

**Source:** `= this.source` (`= this.source-type`)
