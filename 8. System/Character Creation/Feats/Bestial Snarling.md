---
type: feat
source-type: "Remaster"
level: "2"
traits: ["[[Auditory]]", "[[Bard]]", "[[Emotion]]", "[[Fear]]", "[[Mental]]"]
prerequisites: "zoophonia muse"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You can convey the subtle menace of a low growl or predatory rumble. Attempt a [[Nature]] check or Performance check, and compare it to the Will DC of each enemy adjacent to you. If you have an animal minion, such as an animal companion or summoned animal, you can also compare it to each enemy adjacent to them. For each creature that you succeed at, it's [[Frightened]] 1 (or [[Frightened]] 2 if it's an animal). Regardless of the result, each target is temporarily immune to your Bestial Snarling for 10 minutes.

**Source:** `= this.source` (`= this.source-type`)
