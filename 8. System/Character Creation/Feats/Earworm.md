---
type: feat
source-type: "Remaster"
level: "14"
traits: ["[[Bard]]", "[[Exploration]]"]
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

By endlessly repeating a motif, you implant a memorable song that repeats over and over again in your allies' heads, preparing them to respond to it later. Choose a composition cantrip and spend 10 minutes repeating a melody, chant, speech, series of motions, or a similar performance that embodies that cantrip. This activity gains the traits appropriate to the type of performance. You implant the earworm within all allies who can see or hear you (as appropriate for the type of performance) for the entire activity.

Once you've created the earworm, you can attempt a Performance check as a free action to activate it. This check uses the highest Will DC of the earworm's targets present at the time of activation. On a success, you cast the cantrip on all allies who learned the earworm and can perceive your performance; on a failure, the earworm is corrupted and lost. Because it is based on the earlier repetitions, you can't use further free actions like lingering composition or fortissimo composition to modify the activated earworm. Allies forget the earworm after it is activated, if you spend 10 minutes to implant another earworm, or during your next daily preparations, whichever comes first.

**Source:** `= this.source` (`= this.source-type`)
