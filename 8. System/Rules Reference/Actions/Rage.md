---
type: action
source-type: "Remaster"
traits: ["[[Barbarian]]", "[[Concentrate]]", "[[Emotion]]", "[[Mental]]"]
cast: "`pf2:1`"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Requirements** You aren't [[Fatigued]] or raging.

You tap into your inner fury and begin raging. You gain a number of temporary Hit Points equal to your level plus your Constitution modifier. While you are raging:

- You deal 2 additional damage on melee Strikes. This additional damage is halved if your weapon or unarmed attack is agile.
- You can't use actions with the concentrate trait unless they also have the rage trait. You can [[Seek]] while raging.

Rage lasts for 1 minute, until you fall [[Unconscious]], or until the encounter ends, whichever comes first. You can't voluntarily stop raging. When you stop raging, you lose any remaining temporary Hit Points from Rage, and can't gain temporary Hit Points from using the Rage action again for 1 minute.

> [!danger] Effect: Rage Temporary Hit Points Immunity

**Source:** `= this.source` (`= this.source-type`)
