---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Esoterica]]", "[[Manipulate]]", "[[Primal]]", "[[Thaumaturge]]"]
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

`pf2:1` or `pf2:2`

Marigold, spider lily, pennyroyal-many primal traditions connect flowers and plants with the boundary between life and death, and you can leverage this association to keep an ally on this side of the line. You place a small plant or similar symbol on an adjacent [[Dying]] creature, immediately stabilizing them; the creature is no longer dying and is instead [[Unconscious]] at 0 Hit Points.

If you spend 2 actions instead of 1, you empower the act further by uttering a quick folk blessing to chase away ongoing pain, adding the auditory trait to the action. When you do so, attempt flat checks to remove each source of persistent damage affecting the target; due to the particularly effective assistance, the DC is 10 instead of the usual 15.

**Source:** `= this.source` (`= this.source-type`)
