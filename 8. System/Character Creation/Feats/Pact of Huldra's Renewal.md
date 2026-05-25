---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Pactbinder|Pactbinder]]"
source-type: "Remaster"
level: "4"
traits: ["[[Archetype]]", "[[Primal]]"]
prerequisites: "Pactbinder Dedication"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You've sworn a pact with Zemnaïdé, a huldra professor at Cobyslarni, to help renew his former homeland of the Sarkoris Scar. You can cast entangling flora as a primal innate spell once per day. After the spell ends, the flowers and vines become mundane plants that can continue surviving if the natural environment can support them. They're no longer difficult terrain, and don't have the other effects of the spell. Fiends that fail a save against this spell or another plant spell you cast become [[Sickened]] 1 in addition to the normal effects.

In exchange for her boon, Zemnaïdé requires that you never knowingly aid demons or their allies, nor despoil a natural environment. If you do either, you lose the benefits of this feat until you atone. If you comment on his bovine tail or imply the huldras are connected to trolls, Zemnaïdé revokes the benefits of this feat for 1 week or until you sincerely apologize.

**Source:** `= this.source` (`= this.source-type`)
