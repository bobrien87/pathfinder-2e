---
type: feat
source-type: "Remaster"
level: "20"
traits: ["[[Alchemist]]"]
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

If you die while under the effect of at least one elixir, the alchemical compounds in your bloodstream bring you back to life at the start of your next turn. You're affected by an [[Elixir of Rejuvenation]], then a true elixir of life, then your choice of a major bestial mutagen, major juggernaut mutagen, or major quicksilver mutagen as though you just imbibed it. These automatic reactions don't get any special benefits you add when creating or using these items. Because you died, all other alchemical compounds in your bloodstream are inert. After being revived, you're temporarily immune to Alchemical Rejuvenation for 1d4 hours.

**Source:** `= this.source` (`= this.source-type`)
