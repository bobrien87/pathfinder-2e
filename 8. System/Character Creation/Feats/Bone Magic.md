---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Lizardfolk]]"]
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your connection to your iruxi ancestors manifests as a simple primal spell that you cast using a fragment of an ancestor's bones. Choose one cantrip from either the occult spell list or the primal spell list. You can cast this cantrip as an innate spell at will, and it's heightened to a spell rank equal to half your level rounded up.

**Special** Choose when you gain this feat whether your innate spells are primal or occult; this choice applies to all innate spells you gain from lizardfolk ancestry feats that have Bone Magic as a prerequisite.

**Source:** `= this.source` (`= this.source-type`)
