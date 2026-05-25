---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Rivethun Invoker|Rivethun Invoker]]"
source-type: "Remaster"
level: "4"
traits: ["[[Archetype]]", "[[Morph]]", "[[Spirit]]"]
prerequisites: "Rivethun Invoker Dedication"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You're under the effects of [[Enter Spirit Trance]].

You manifest a physical attack of the spirits all around you, such as the claw of an animal spirit or the whipping vine of a nature spirit. You gain an unarmed attack that deals 1d8 spirit damage for the duration of your spirit trance. This unarmed attack is in the brawling weapon group and has the agile, finesse, and magical traits.

At 5th level, this unarmed attack gains the benefits of a striking rune. At 12th level, this unarmed attack gains the benefits of a greater striking rune. At 20th level, this unarmed attack gains the benefits of a major striking rune.

**Source:** `= this.source` (`= this.source-type`)
