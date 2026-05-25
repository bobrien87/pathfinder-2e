---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Snarecrafter|Snarecrafter]]"
source-type: "Remaster"
level: "6"
traits: ["[[Archetype]]"]
prerequisites: "Snarecrafter Dedication"
source: "Pathfinder Lost Omens Hellfire Dispatches"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Using clever gnomish engineering, you can quickly erect small barriers in which your snares are hidden. When you prepare snares for quick deployment, you can prepare some of them as barricade snares. A barricade snare consists of a small barricade in which the snare is hidden, but it costs two of your quick deployment snares. Though creatures can automatically see the barricade, the snare hidden inside the barricade must be detected like a standard snare, but with a +2 circumstance bonus to the DC. The barricade occupies the same space as the snare and is 5 feet high; it provides standard cover, can be Climbed with a successful DC 12 [[Athletics]] check, has an AC of 10, Hardness 5, and 20 healing Hit Points, and is immune to critical hits and precision damage. The barricade lasts as long as the snare does. A creature triggers and is affected by the hidden snare when it attempts to Climb the barricade or successfully attacks the barricade while adjacent to it. The snare and barricade are destroyed when the snare is triggered or if the barricade is destroyed, whichever comes first.

**Special** Even if you have the Surprise Snare feat, you must craft a barricade snare in an empty square.

**Source:** `= this.source` (`= this.source-type`)
