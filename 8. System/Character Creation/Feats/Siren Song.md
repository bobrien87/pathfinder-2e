---
type: feat
source-type: "Remaster"
level: "9"
traits: ["[[Auditory]]", "[[Mental]]", "[[Merfolk]]", "[[Primal]]"]
prerequisites: "expert in Performance"
frequency: "once per day"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per day

You can beguile and bewitch with your song. All creatures in a @Template[emanation|distance:60] must attempt a [[Will]] save against your Performance DC. On subsequent rounds, you can Sustain the song, causing each creature in the area currently affected by your song to attempt another Will save. Typically, creatures that have traveled with you for a significant time, such as your fellow party members, are immune to your Siren Song.
- **Critical Success** The target is unaffected and becomes immune to your Siren Song for 24 hours.
- **Success** The target is [[Fascinated]] with you until the end of your next turn.
- **Failure** As success, and the target is [[Stupefied 1]] for as long as it's fascinated.
- **Critical Failure** As success, and the target is [[Stupefied 2]] for as long as it's fascinated.

**Source:** `= this.source` (`= this.source-type`)
