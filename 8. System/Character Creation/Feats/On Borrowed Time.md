---
type: feat
source-type: "Remaster"
level: "10"
traits: ["[[Cursebound]]", "[[Divine]]", "[[Oracle]]"]
prerequisites: "time mystery"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You accelerate a foe's personal timestream, which causes them to experience time at a faster rate, putting a terrible strain on their mind and body. A creature you target within 30 feet takes 3d6 persistent,mental damage with a [[Will]] save. At the end of the subject's turn, they take this persistent damage after all other persistent damage. Before they roll their flat check to end the persistent damage, an additional round passes for them; this affects the duration of all beneficial effects, negative effects, afflictions, conditions, and other persistent damage. The subject attempts saving throws, flat checks, and any other rolls and takes damage as if the time had passed. They don't take the persistent mental damage from On Borrowed Time more than once per round.

If you are [[Cursebound 2]] when you use On Borrowed Time, the persistent damage increases to 4d6. If you are [[Cursebound 3]] when you use On Borrowed Time, the persistent damage increases to 5d6.

**Source:** `= this.source` (`= this.source-type`)
