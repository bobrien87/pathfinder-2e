---
type: action
source-type: "Remaster"
traits: ["[[Primal]]", "[[Void]]"]
cast: "`pf2:2`"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Frequency** once per day

**Effect** Void energy seeps out of you, decaying everything within a @Template[emanation|distance:5] and causing plants and foliage to age and decompose. Natural difficult terrain is destroyed, and creatures in the area with the plant or wood trait take @Damage[1d6[void]|options:area-damage] damage with a [[Fortitude]] save against your class DC or spell DC, whichever is higher.

**Source:** `= this.source` (`= this.source-type`)
