---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Broken Chain|Broken Chain]]"
source-type: "Remaster"
level: "20"
traits: ["[[Concentrate]]", "[[Mythic]]"]
prerequisites: "Broken Chain Dedication"
frequency: "once per P1M"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per month

Something terrible has happened. A beloved ally has fallen, a last stand has failed, or a tyrant has beaten you to a crucial goal. Whatever it is, your heart sinks. How can this be? No, this can't be. You spend a Mythic Point to alter reality as if you got a success (but not a critical success) with the [[Wish]] ritual. You must choose to completely undo the effects of a past action or set of actions that occurred within the past week to lead to the undesirable outcome. This will bring serious consequences back to haunt you some day. Altering the rhythm of causality is likely to draw the attention of certain aeons. Fey norns won't be too happy with you fraying their precious threads of fate either. Deities whose domains include change, fate, freedom, time, or tyranny are likely to start keeping tabs on you, if they haven't already, and send their agents to meddle in your affairs.

**Source:** `= this.source` (`= this.source-type`)
