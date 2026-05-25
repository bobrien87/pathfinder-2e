---
type: action
source-type: "Remaster"
traits: ["[[Concentrate]]", "[[Emotion]]", "[[Mental]]", "[[Transcendence]]", "[[Visual]]"]
cast: "`pf2:2`"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

You focus your attention on a creature within 30 feet, overwhelming its senses. The creature must succeed at a [[Will]] save against your class DC or be [[Fascinated]] by you until the start of your next turn. The condition ends if you use a hostile action against the target, but not if you use a hostile action against its allies.

**Source:** `= this.source` (`= this.source-type`)
