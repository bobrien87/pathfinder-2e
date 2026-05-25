---
type: action
source-type: "Remaster"
traits: ["[[Auditory]]", "[[Spellshape]]"]
cast: "`pf2:1`"
source: "Pathfinder #204: Stage Fright"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

By using your perfect pitch, you can amplify your voice to cause magical auditory effects to reach further. If your next action this round is to Cast a Spell or use an action that creates an auditory effect with a range, increase that range by 30 feet.

**Source:** `= this.source` (`= this.source-type`)
