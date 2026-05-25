---
type: feat
source-type: "Remaster"
level: "8"
traits: ["[[Druid]]", "[[Healing]]", "[[Vitality]]"]
prerequisites: "leaf order"
frequency: "once per day"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per day

You request that nearby plants share their vitality with you to replenish your body and magic. You regain 1 Focus Point and @Damage[ceil(@item.level/2)d8[healing]] Hit Points.

You must be in a location of at least 15 feet by 15 feet of healthy plant life, though this can be grass, lichen, seaweed, or any other form of naturally occurring flora. Using Floral Restoration on a given section of nature does not harm it, but it prevents that section of nature from giving its vitality to another use of Floral Restoration for 24 hours.

At 9th level, and every 2 levels thereafter, increase the healing by 1d8.

**Source:** `= this.source` (`= this.source-type`)
