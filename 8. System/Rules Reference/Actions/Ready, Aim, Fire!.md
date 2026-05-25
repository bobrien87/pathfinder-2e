---
type: action
source-type: "Remaster"
traits: ["[[Brandish]]", "[[Commander]]", "[[Tactic]]"]
cast: "`pf2:2`"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Frequency** once per 10 minutes

You signal a volley of ranged attacks from your allies. Choose an enemy and signal up to three squadmates within the aura of your commander's banner; your squadmates can Interact to reload as a free action and attempt a ranged Strike against the enemy as a reaction

**Special** If one of your squadmates knows or has prepared a cantrip with a range of 30 feet or more that deals damage and requires 2 or fewer actions to cast, they can cast it targeting the enemy instead of taking the other actions normally granted by this tactic.

**Source:** `= this.source` (`= this.source-type`)
