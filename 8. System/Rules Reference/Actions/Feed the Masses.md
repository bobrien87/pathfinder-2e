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

The [[Horn of Plenty]] allows you to transfer the effects of potions and elixirs to your allies. You Interact to draw a consumable from the horn and then Interact to drink it. Rather than nourishing yourself, the item's effects are transferred to a willing ally within 60 feet, as if they had consumed it themself.

If the consumable restores Hit Points, you can choose to divide the amount it restores between you and the ally freely (after rolling dice to determine the amount).

**Source:** `= this.source` (`= this.source-type`)
