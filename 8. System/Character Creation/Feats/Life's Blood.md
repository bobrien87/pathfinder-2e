---
type: feat
source-type: "Remaster"
level: "9"
traits: ["[[Healing]]", "[[Samsaran]]", "[[Vitality]]"]
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your journey to enlightenment has made your blood possess nigh-immortal properties, allowing you to heal others. You sacrifice some of your vitality to heal another willing living creature that's adjacent to you, coating its wounds with your blood. You lose @Damage[(max(3,floor((@actor.level -4)/2))d6)[untyped]] Hit Points, plus an additional 1d6 Hit Points for every 2 levels you have beyond 10th. This damage can't be resisted, prevented, or negated in any way. The target creature regains a number of Hit Points equal to the damage you took. Creatures you heal in this manner are then temporarily immune to your Life's Blood for 24 hours.

**Source:** `= this.source` (`= this.source-type`)
