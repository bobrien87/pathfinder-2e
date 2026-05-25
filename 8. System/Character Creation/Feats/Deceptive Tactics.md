---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Commander]]"]
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You can prepare at least three tactics.

Your training has taught you that the art of war is the art of deception. You can use your Warfare Lore modifier in place of your Deception modifier for Deception checks to `act create-a-diversion skill=warfare-lore` or `act feint skill=warfare-lore`, and can use your proficiency rank in Warfare Lore instead of your proficiency rank in Deception to meet the prerequisites of feats that modify the [[Create a Diversion]] or [[Feint]] actions (such as [[Lengthy Diversion]]). You gain the Lengthy Diversion feat.

**Source:** `= this.source` (`= this.source-type`)
