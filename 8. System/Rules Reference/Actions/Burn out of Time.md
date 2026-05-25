---
type: action
source-type: "Remaster"
traits: ["[[Spirit]]", "[[Transcendence]]", "[[Void]]"]
cast: "`pf2:2`"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

An impossible amount of energy blazes in a sphere above you before compressing itself into your weapon. Strike one creature. The Strike deals an additional 3d8 spirit damage and 3d8 void damage. If the creature is reduced to 0 Hit Points, it's immediately killed and reduced to ash, not in the present, but in the recent past, erasing the consequences of their recent actions.

If a creature died within the last round as a result of the incinerated target's actions, that creature is returned to life with 5d8 healing Hit Points at the location that it died as its death is retroactively undone.

**Source:** `= this.source` (`= this.source-type`)
