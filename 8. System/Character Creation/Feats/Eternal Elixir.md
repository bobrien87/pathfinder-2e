---
type: feat
source-type: "Remaster"
level: "16"
traits: ["[[Alchemist]]"]
prerequisites: "Extend Elixir"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your body readily accepts and retains minor changes. When you drink one of your alchemical items that has the elixir and infused traits and a duration of 1 minute or more, you can make the elixir's duration indefinite. This can exceed the 10-minute limit of an item made with [[Quick Alchemy]]. You can do so only if the elixir's level is half your level or lower. If you later consume a different elixir and make it indefinite, the effect of the previous indefinite elixir ends.

**Source:** `= this.source` (`= this.source-type`)
