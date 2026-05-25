---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Apocalypse Rider|Apocalypse Rider]]"
source-type: "Remaster"
level: "20"
traits: ["[[Mythic]]"]
prerequisites: "Apocalypse Rider Dedication"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your commitment to ending all life earns you a measure of immortality, setting the stage for you to become a true Rider of the Apocalypse, possibly supplanting one of the Four. You gain the daemon, fiend, and unholy traits, and so does your apocalypse mount, but your fates are ever more entwined. As long as your apocalypse mount lives, you don't age and whenever your [[Doomed]] or [[Dying]] condition would increase to 4 or more, it doesn't increase. If you would be killed in any other way, you are instead reduced to 0 Hit Points, become [[Unconscious]], and if your apocalypse mount is conscious, it instantly teleports to your side, picks you up, and attempts to flee the scene of danger.

While you are conscious and within 30 feet of your apocalypse mount, it can't be killed. If your apocalypse mount is reduced to 0 Hit Points, it immediately stabilizes and its dying condition can't increase. If its doomed condition would increase to 4 or more, it doesn't increase. However, if you move more than 30 feet away from your apocalypse mount or go [[Unconscious]] during this time, your apocalypse mount loses these benefits and might die.

Finally, when a living creature within 60 feet of you dies, it must attempt a [[Will]] save saving throw against your class DC or spell DC, whichever is higher. This is an incapacitation effect. On a failure, that creature can't be brought back to life for 24 hours. On a critical failure, you can chose to have that creature's soul coalesce into a fist-sized soul gem (Hardness 2, HP 8) that appears in that creature's space. That creature's soul is trapped within the gem for 1 week, though you can make the gem permanent with a 10-minute ritual. Destroying the gem frees the soul within but doesn't return the deceased creature to life. If a caster attempts to return to life a creature whose soul is trapped within a soul gem, they fail unless they succeed at a [[Religion]] check against your class DC or spell DC, whichever is higher. A success causes the soul gem to shatter, allowing the creature to be returned to life as normal for the spell. Daemons and other fiends prize these soul gems, and they're generally worth an amount relative to the level of a gem's captive soul.

**Source:** `= this.source` (`= this.source-type`)
