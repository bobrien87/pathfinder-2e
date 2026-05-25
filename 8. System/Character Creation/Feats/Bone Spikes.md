---
type: feat
source-type: "Remaster"
level: "2"
traits: ["[[Deviant]]", "[[Magical]]"]
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Sharp shards of bone tear forth from your elbows, wrists, or other parts of your body. For 1 minute, you can make bone spike unarmed Strikes, which deal 1d6 piercing damage and have the versatile S and sweep traits. When you take the Bone Spikes action, you can choose one weapon on your person and duplicate its weapon runes onto your bone spikes (with the exception of any runes that couldn't apply to the bone spears).

> [!danger] Effect: Bone Spikes

**Awakening** Your bones grow longer, lashing flexibly at range. While you have bone spikes, you can Interact to give your bone spikes reach 10 feet until the end of the current turn.

**Awakening** Grooves in your bone spikes form a channel for venom. Your bone spikes deal 1d4 persistent poison damage, which increases to 2d4 at 10th level and 3d4 at 18th level.

**Source:** `= this.source` (`= this.source-type`)
