---
type: feat
source-type: "Remaster"
level: "4"
traits: ["[[Ranger]]"]
prerequisites: "Trained in Deception"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

With a bit of hide, some antlers, and some cast-off fur, you can create a disguise that will fool even an experienced hunter. You can [[Impersonate]] creatures with the animal, beast, or plant traits, so long as they are either the same size or one size larger than you and have a body shape that conforms at least vaguely to your own (in other words, a typical humanoid could Impersonate a bear or an arboreal, but not a horse, giant scorpion, or assassin vine). Impersonating a larger creature doesn't change your actual size.

**Source:** `= this.source` (`= this.source-type`)
