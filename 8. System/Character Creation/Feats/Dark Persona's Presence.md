---
type: feat
source-type: "Remaster"
level: "8"
traits: ["[[Aura]]", "[[Emotion]]", "[[Fear]]", "[[Mental]]", "[[Psychic]]"]
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** You [[Unleash your Psyche]].

When you Unleash your Psyche, all your rage and pain-the portion of your psyche dedicated to cruel retribution-come along with it.

The force of your dark persona's negativity batters constantly against all creatures in a @Template[emanation|distance:30] when you Unleash your Psyche and for as long as your Psyche is Unleashed. A creature must attempt a [[Will]] save against your spell DC the first time it enters the emanation, or if it's in the emanation when you take this action; it doesn't need to attempt a save again, even if it leaves the emanation and returns. A creature frightened by your Dark Persona's Presence can't decrease its frightened value below 1 while within the emanation.
- **Critical Success** The creature is unaffected.
- **Success** The target is [[Frightened]] 1.
- **Failure** The target is [[Frightened]] 2.
- **Critical Failure** The target is [[Frightened]] 3.

While your Psyche is Unleashed, your dark persona cares only for destruction. You can Cast a Spell only if it can directly damage an enemy or object or can impose a detrimental condition or penalty on one.

**Source:** `= this.source` (`= this.source-type`)
