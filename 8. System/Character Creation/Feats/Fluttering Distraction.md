---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Fan Dancer|Fan Dancer]]"
source-type: "Remaster"
level: "10"
traits: ["[[Archetype]]", "[[Manipulate]]", "[[Misfortune]]"]
prerequisites: "Fan Dancer Dedication"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** An enemy attempts a ranged or melee Strike against an ally within 30 feet.

**Requirements** You're wielding two fans, one in each hand.

You're trained in snapping and fluttering your fans to draw the eyes of observers around you. You manipulate your fans to create a distraction. The enemy must roll its attack twice and take the lower result.

> [!danger] Effect: Fluttering Distraction

**Source:** `= this.source` (`= this.source-type`)
