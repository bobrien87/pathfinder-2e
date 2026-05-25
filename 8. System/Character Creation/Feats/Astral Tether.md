---
type: feat
source-type: "Remaster"
level: "4"
traits: ["[[Occult]]", "[[Psychic]]"]
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You spin out a thread of psychic energy that connects you to an ally, using it as a conduit for your abilities. Choose a willing creature within 60 feet and connect to it. Whenever you would gain a benefit from a psychic amp, you can have the amp affect the tethered creature instead. You can do so only if the amp grants a distinct benefit, not if it alters the amped spell.

The tether can't be severed physically but breaks if the distance between you and the tethered ally ever exceeds 60 feet, if you become [[Unconscious]], or if you use Astral Tether again.

**Source:** `= this.source` (`= this.source-type`)
