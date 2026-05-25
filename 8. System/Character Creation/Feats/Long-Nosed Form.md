---
type: feat
source-type: "Remaster"
level: "5"
traits: ["[[Concentrate]]", "[[Polymorph]]", "[[Primal]]", "[[Tengu]]"]
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You transform into a specific, curious-looking human form. This human form is the same age and body type as your tengu form and has roughly analogous physical traits, such as height, though your nose remains as long as your beak and your complexion has red undertones, no matter the skin color of your human form. Using Long-Nosed Form counts as creating a disguise for the Impersonate use of Deception. Due to your imperfect transformation, your transformation doesn't automatically defeat Perception DCs to determine whether you are human, though you may be able to explain away or hide your tengu traits.

You lose your beak unarmed Strike in your human form, as well as any other unarmed Strikes you gained from a tengu heritage or ancestry feat. You remain in your human form indefinitely, until you Dismiss this effect.

**Source:** `= this.source` (`= this.source-type`)
