---
type: heritage
source-type: "Remaster"
ancestry: "[[8. System/Character Creation/Ancestries/Lizardfolk|Lizardfolk]]"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Heritage**
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Ancestry** " + this.ancestry`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "")`

You can change your skin color to blend in with your surroundings, making minor shifts with a single action and dramatic changes over the course of an hour. When you're in an area where your coloration is roughly similar to the environment (for instance, forest green in a forest), you can use the minor, single-action application of this ability to make localized changes that help you blend into your surroundings, gaining a +2 circumstance bonus to Stealth checks until your surroundings change in coloration or pattern.

**Source:** `= this.source` (`= this.source-type`)
