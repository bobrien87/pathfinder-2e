---
type: action
source-type: "Remaster"
traits: ["[[Concentrate]]", "[[Mental]]", "[[Spirit]]", "[[Transcendence]]"]
cast: "`pf2:2`"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

The weight of authority falls heavily upon you, as well as nearby creatures. All enemies in a @Template[type:burst|distance:15] within 60 feet take @Damage[(@actor.level)[spirit]|options:area-damage]{spirit damage damage equal to your level} with a [[Will]] save against your class DC. Any enemy that fails its save must immediately kneel, dropping [[Prone]] as a free action.

**Source:** `= this.source` (`= this.source-type`)
