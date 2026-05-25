---
type: action
source-type: "Remaster"
cast: "`pf2:2`"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

Choose either auditory or visual effects. The display gains that trait, and you attempt to counteract one or more effects in a @Template[emanation|distance:60] that have this trait. On a success, the effect is suppressed until the start of your next turn, rather than ending entirely. Use your Fireworks lore check modifier as your counteract modifier, and your counteract rank is equal to half your level (rounded up). You can spend 2 versatile vials and 3 actions (instead of the usual Cost and actions) to create an even bigger coughing dragon display that attempts to counteract both auditory and visual effects at the same time.

**Source:** `= this.source` (`= this.source-type`)
