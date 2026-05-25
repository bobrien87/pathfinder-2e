---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Seneschal|Seneschal]]"
source-type: "Remaster"
level: "20"
traits: ["[[Archetype]]"]
prerequisites: "Seneschal Witch Dedication"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You have fully realized the ability to serve as a patron.

Your newfound abilities enhance your senses, rolling back the veil of a realm hidden to most mortals where great beings vie for unimaginable influence over vast worlds. You gain darkvision, constant [[Truesight]], and the ability to see into all other transitive planes that overlap the one you are in.

You can be a patron for other witches. Choose a single type of patron you represent, such as [[The Resentment]] or [[Starless Shadow]]. An allied witch you can observe who has that patron counts as and gains the benefits of your [[Witch's Charge]] feat, even if you did not select them as your charge during your daily preparations.

You learn the [[Wish]] ritual and can impart that knowledge to your charges. Once per month, when one of your charges performs the *wish* ritual, you can roll the skill check in their place.

**Source:** `= this.source` (`= this.source-type`)
