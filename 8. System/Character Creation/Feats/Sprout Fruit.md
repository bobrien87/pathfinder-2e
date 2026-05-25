---
type: feat
source-type: "Remaster"
level: "2"
traits: ["[[Deviant]]", "[[Healing]]", "[[Magical]]", "[[Plant]]"]
source: "Pathfinder #202: Severed at the Root"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

The plants covering your body sprout a single, ripe fruit. A creature other than you who eats this fruit as a three-action activity (1 Interact action to pluck the fruit and 2 Interact actions to eat it) is healed @Damage[(floor(@actor.level/2)d4)[healing]] Hit Points for every 2 levels you have.

**Awakening** The fruit is more potent. Increase the healing from d4s to d6s (@Damage[(floor(@actor.level/2)d6)[healing]]).

**Awakening** The fruit is plentiful. You sprout one additional fruit for every 5 levels you have beyond 2. Also, those who eat a fruit may reduce a condition affecting them by 1.

**Source:** `= this.source` (`= this.source-type`)
