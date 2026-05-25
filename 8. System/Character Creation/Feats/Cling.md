---
type: feat
source-type: "Remaster"
level: "9"
traits: ["[[Goblin]]"]
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** Your last action was a successful Strike and you have a free hand.

You hang onto a foe to harry them into submission. If your target moves while you're hanging onto it, you can choose to move with the target. The target is released if you choose not to move with it, at the start of your next turn, or if the target Escapes. Attempts to [[Escape]] from a Cling are made against your Acrobatics DC, but they end the Cling instead of the conditions normally ended by the Escape action.

**Special** You can use this action without a free hand if your preceding Strike was made with your jaws or a similar unarmed attack you could use to hang on. The GM determines which unarmed attacks apply. Hanging on in this way prevents you from using that unarmed attack.

**Source:** `= this.source` (`= this.source-type`)
