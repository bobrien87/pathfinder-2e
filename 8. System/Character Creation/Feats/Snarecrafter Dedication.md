---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Snarecrafter|Snarecrafter]]"
source-type: "Remaster"
level: "2"
traits: ["[[Archetype]]", "[[Dedication]]"]
prerequisites: "trained in Crafting, Snare Crafting"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You have studied the art of crafting snares and laying traps, and few have shown more talent in these arts than you. You gain the [[Snare Crafting]] feat. When you set a snare, the DC of any saving throw it requires uses the higher of your class DC or the snare's DC. If a snare normally takes 1 minute to Craft, you can Craft it with 3 Interact actions instead.

Each day during your daily preparations, you can prepare four snares from your formula book for quick deployment (increasing to six snares if you're a master in Crafting and eight if you're legendary). Snares prepared in this way don't cost you any resources to Craft.

When you increase your proficiency rank in Crafting to expert, master, or legendary, add three additional snare formulas to your formula book. The snares must be of your level or lower.

**Special** Rangers can adapt snare crafting techniques to create snares from natural materials. If you are a ranger, you can use Survival instead of Crafting for all prerequisites and functions of feats from this archetype. (This includes using Survival to Craft a snare.)

Snarecrafter

**Source:** `= this.source` (`= this.source-type`)
