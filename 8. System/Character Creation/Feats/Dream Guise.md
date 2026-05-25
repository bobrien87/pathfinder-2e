---
type: feat
source-type: "Remaster"
level: "10"
traits: ["[[Illusion]]", "[[Occult]]", "[[Psyche]]", "[[Psychic]]"]
prerequisites: "wandering reverie subconscious mind"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You Stride into a willing ally's space, at which point both of your appearances shift into a shared third appearance, usually one that looks like a mix of the two of you. Then, either you or your ally [[Stride|Strides]]. You each maintain the merged appearance. Creatures who are observing this know what happened, but still must Seek or otherwise engage with the illusion to attempt to disbelieve it and determine which of you is which. Otherwise, they can't tell the difference and have an equal chance to target each of you (DC 11 flat check). This illusion ends as soon as either you or the ally you're merged with acts.

**Source:** `= this.source` (`= this.source-type`)
