---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Druid]]", "[[Exploration]]"]
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You cultivate a seed that can sprout into a wooden staff, vine whip, or another weapon. You spend 10 minutes focusing primal energy into a seed, imprinting it with the potential of a single level 0 weapon you are trained with and that has no mechanical parts or metal components. When holding the imprinted seed, you can use an Interact action to cause it to immediately grow into that weapon; a second Interact action returns it to seed form. The verdant weapon can be etched with runes or affixed with talismans as normal, which are suppressed when the weapon is in seed form.

You can have only one verdant seed at a time. If you prepare a second, your first verdant seed immediately becomes a mundane seed; any runes on the previous seed transfer to the new seed at no cost, but inapplicable runes are suppressed.

**Source:** `= this.source` (`= this.source-type`)
