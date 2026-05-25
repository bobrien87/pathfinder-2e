---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Lineage]]", "[[Reflection]]"]
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You were once a shapeshifter or spellcaster using polymorph magic, but something went wrong, and you became trapped in the form of the creature you were imitating. This accident might have drained your power, or you might have retained some of your skills, but either way, your form resists further forced transformation. You gain a +1 circumstance bonus to saving throws against morph and polymorph effects, and if you roll a success on a saving throw against a hostile morph or polymorph effect, you get a critical success instead.

**Source:** `= this.source` (`= this.source-type`)
