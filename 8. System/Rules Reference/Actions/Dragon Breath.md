---
type: action
source-type: "Remaster"
cast: "`pf2:2`"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Frequency** once per hour

**Effect** You breathe deeply and exhale a line or cone of powerful breath, much like the dragon with which you made the pact. If the dragon had a cone-shaped breath, your breath is a @Template[type:cone|distance:30]. If they had a line-shaped breath, your breath is a @Template[type:line|distance:60]. If they had a burst-shaped breath, your breath is a @Template[type:burst|distance:10] within 60 feet. No matter the shape, it deals 1d6 damage per level (@Damage[(@actor.level)d6[untyped]|options:area-damage]), of the same damage type as the dragon's breath, with a [[Reflex]] save, using the higher of your class DC or spell DC. This action has the same traits as the breath of the dragon you made the pact with.

**Source:** `= this.source` (`= this.source-type`)
