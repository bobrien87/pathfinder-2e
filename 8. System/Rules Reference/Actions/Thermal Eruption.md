---
type: action
source-type: "Remaster"
traits: ["[[Fire]]", "[[Primal]]"]
cast: "`pf2:2`"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Frequency** once per day

**Effect** You concentrate your thermal energy and explode it outward. All creatures in a @Template[type:emanation|distance:20] take @Damage[14d6[fire]|options:area-damage] damage with a basic Reflex save. Afterward, you lose all effects of the Dormant Eruption feat until your next daily preparations.

**Source:** `= this.source` (`= this.source-type`)
