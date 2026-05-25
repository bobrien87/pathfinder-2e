---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Firework Technician|Firework Technician]]"
source-type: "Remaster"
level: "2"
traits: ["[[Archetype]]", "[[Dedication]]"]
prerequisites: "trained in Crafting"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You've learned the secrets of making fire and sound bloom using black powder, metals, and paper. You most likely came by this knowledge through formal training with a fireworks house in Tian Xia or a fireworks company from Vudra, though perhaps you mastered fireworks completely by yourself after finding a secret stash in an old shipwreck.

You become trained in Fireworks Lore or become an expert if you were already trained in it. You gain the quick alchemy benefits, creating up to 4 pyrotechnic versatile vials during your daily preparations. These vials have the fire trait and deal fire damage instead of acid. You can use pyrotechnic versatile vials only to throw as bombs, for the [[Launch Fireworks]] action or with [[Quick Alchemy]] to create fireworks consumables, including Doses or rounds of black powder, the [[Sparkler]] item, and other items determined by the GM. You can replenish your versatile vials during exploration the same way an alchemist can.

You can create fireworks displays to have distinctive effects you can use to make onlookers marvel and even to gain an advantage in combat. You gain the Launch Fireworks action and learn some basic effects. You can learn additional, more complex displays that use your versatile vials through other firework technician feats. These add a new fireworks display to your options for Launch Fireworks, each of which lists its number of actions and effects. The DC for Launch Fireworks is equal to your class DC or spell DC, whichever is higher.

**Special** If you have Quick Alchemy from another source (such as the alchemist class or multiclass archetype), you can use standard versatile vials to Launch Fireworks or create fireworks consumables. Each time you create a versatile vial, you choose whether it's a standard vial or pyrotechnic vial. Both types count toward your maximum number of versatile vials. You can replenish only pyrotechnic vials during exploration unless another ability lets you replenish standard versatile vials (such as the benefit of the alchemist class), in which case you can choose the type each time you replenish.

Firework Technician

**Source:** `= this.source` (`= this.source-type`)
