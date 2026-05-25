---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Concentrate]]", "[[Hungerseed]]", "[[Polymorph]]", "[[Primal]]"]
frequency: "once per PT10M"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your horns flash briefly as you grow in size and ferocity. Your size increases to Large, and you're [[Clumsy]] 1. This doesn't change your Speed, reach, or other statistics except as noted here. Your worn equipment automatically resizes to suit your new form, though it immediately returns to its original size if it leaves your possession.

This form is the same age and body type as your true form and has roughly analogous physical traits, such as hair color. Using Oni Form counts as creating a disguise for the [[Impersonate]] use of Deception.

You can Sustain your Oni Form for up to 10 minutes, though you must then spend at least 10 minutes in your natural form before using Oni Form again.

**Source:** `= this.source` (`= this.source-type`)
