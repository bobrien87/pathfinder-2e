---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Linguist|Linguist]]"
source-type: "Remaster"
level: "7"
traits: ["[[Archetype]]", "[[Linguistic]]", "[[Skill]]"]
prerequisites: "Linguist Dedication, master in Society"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

All communication is filled with slight tells and signals. If you interact with someone for at least 10 minutes, their regional words, pronunciation changes, and nonverbal cues provide you with a minor fact about their social environment, such as their hometown or certain groups they might belong to.

If a target of this ability is being deceptive about their social environment, such as a commoner pretending to be a noble, they must attempt a Deception, Society, or appropriate Lore check against your Society DC, providing you a false minor fact consistent with their assumed identity on a success.

Once you've gleaned one or more true minor facts about a person, you can then incorporate these mannerisms into your speech to present yourself in a way that they find familiar. This grants you a +1 circumstance bonus to your Diplomacy and Deception checks with them.

> [!danger] Effect: Read Shibboleths

**Source:** `= this.source` (`= this.source-type`)
