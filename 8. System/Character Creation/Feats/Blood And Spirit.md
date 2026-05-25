---
type: feat
source-type: "Remaster"
level: "5"
traits: ["[[Dragonblood]]"]
prerequisites: "Divine Dragonblood"
source: "Pathfinder Lost Omens Draconic Codex"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your connection to the divine has sanctified your blood, but the power only manifests when you are shedding it. Choose holy or unholy. While you are taking persistent bleed damage, you can Interact to coat a piercing or slashing weapon you're wielding with your blood. Until the end of your turn, your Strikes with that weapon deal an additional 1d6 spirit damage with the chosen trait to creatures with the opposing trait.

> [!danger] Effect: Blood and Spirit

Alternatively, you can deal 1d6 slashing damage to yourself (which can't be resisted in any way) as part of that Interact action if you aren't taking persistent bleed damage.

**Source:** `= this.source` (`= this.source-type`)
