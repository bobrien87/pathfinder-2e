---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Celebrity|Celebrity]]"
source-type: "Remaster"
level: "10"
traits: ["[[Archetype]]", "[[Auditory]]", "[[Aura]]", "[[Concentrate]]", "[[Emotion]]", "[[Mental]]", "[[Visual]]"]
prerequisites: "Celebrity Dedication"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You command the attention of all around you with style, ensuring their gaze falls only upon you until the end of your next turn. Whenever a creature in a @Template[emanation|distance:30] around you attempts a saving throw against a different visual effect, it gets a result one degree of success better than it rolled. This is a fortune effect.

When an enemy within the aura attempts to use a visual effect that involves focusing its attention on a particular creature (such as a medusa's Focus Gaze), it must succeed at a [[Will]] save against your class DC or spell DC, whichever is higher, in order to target any creature except you.

Allies in the aura can attempt to [[Hide]] even if they don't have cover, as you are continually providing a distraction.

**Source:** `= this.source` (`= this.source-type`)
