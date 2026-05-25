---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Gnome]]"]
prerequisites: "kijimuna gnome heritage"
frequency: "once per day"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per day

You can gain the magic of the seas by eating your favorite seafood. This gives you an advantage when diving, escaping notice after pilfering a valuable artifact from a local warlord, moving through poisonous fumes, or sleeping next to a particularly gassy adventuring partner. If you eat the left eye of a fish, you gain the [[Breath Control]] feat for the next hour, and that feat's benefits apply against effects that have the olfactory trait in addition to those that have the inhaled trait. As this feat is temporary, you can't use it as a prerequisite for a permanent character option like a feat or access to a spell.

**Source:** `= this.source` (`= this.source-type`)
