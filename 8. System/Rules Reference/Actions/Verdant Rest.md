---
type: action
source-type: "Remaster"
traits: ["[[Concentrate]]"]
cast: "`pf2:1`"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

You turn into a tree or other non-creature plant. This has the effect of using [[One with Plants]] to turn into a plant, except that your AC is 30. You can Dismiss this effect to turn back. If you rest for 10 minutes in this form in natural sunlight, you recover half your maximum Hit Points. If you take your daily rest in this form, the rest restores you to maximum Hit Points and removes all non-permanent [[Drained]], [[Enfeebled]], [[Clumsy]], and [[Stupefied]] conditions, as well as all poisons and diseases of 19th level or lower.

**Source:** `= this.source` (`= this.source-type`)
