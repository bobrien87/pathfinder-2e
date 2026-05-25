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

Your body warps beyond recognition into a powerful, one-eyed form. You're affected by a 4th-rank [[Enlarge]] spell and a 6th-rank [[Moon Frenzy]] spell, which both last until the end of your next turn. You can't attempt to end the moon frenzy early.

If this ikon becomes empowered again, you can extend Spasm of the Berserker's duration until the end of your next turn. While you're already affected by Spasm of the Berserker, the transcend action becomes a free action to extend its duration until the end of your next turn.

**Source:** `= this.source` (`= this.source-type`)
