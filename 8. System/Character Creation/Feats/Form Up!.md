---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Marshal|Marshal]]"
source-type: "Remaster"
level: "10"
traits: ["[[Archetype]]", "[[Auditory]]", "[[Flourish]]"]
prerequisites: "Marshal Dedication"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You've trained in battle formations for a plethora of situations. Choose a formation. Allies within your aura can use their reaction to Stride up to their Speed and take a place in the chosen formation. Allies can't benefit from this movement if there isn't room for them in the chosen formation. If there are more eligible allies than there are available spaces in the chosen formation, you choose which allies benefit.

- **Line** Your allies gather adjacent to you and each other to form a straight line in a direction of your choosing.
- **Wedge** Your allies gather into any space that would be covered by a @Template[type:cone|distance:15] originating from you in a direction of your choosing.
- **Cluster** Your allies gather into any space that would be covered by a @Template[type:emanation|distance:15] in an aura around you.

**Source:** `= this.source` (`= this.source-type`)
