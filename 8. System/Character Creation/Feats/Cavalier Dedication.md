---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Cavalier|Cavalier]]"
source-type: "Remaster"
level: "2"
traits: ["[[Archetype]]", "[[Dedication]]"]
prerequisites: "trained in Nature or Society"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You gain a young animal companion that serves as your mount. You can choose from animal companions with the mount special ability, as well as any additional options from your pledge (see Cavalier Pledges journal), as determined by your GM. You must choose an animal companion that's at least one size larger than you, but if the animal usually starts as Small, you can begin with a Medium version of that animal (changing no statistics other than its size).

**Special** If you have pledged yourself to a cause, you can take a second dedication feat closely tied to that cause even if you haven't taken two additional Cavalier feats. For instance, if you pledged yourself to fight crime with a group of vigilantes, you could take the vigilante dedication without first completing the cavalier archetype. The GM determines what archetypes, if any, are valid choices.

**Source:** `= this.source` (`= this.source-type`)
