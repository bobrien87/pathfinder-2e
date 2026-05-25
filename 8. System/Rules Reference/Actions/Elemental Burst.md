---
type: action
source-type: "Remaster"
traits: ["[[Concentrate]]", "[[Eidolon]]"]
cast: "`pf2:2`"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Frequency** once per 10 minutes

Your eidolon rips off a chunk of elemental matter from their own form and hurls it into a group of foes. Your eidolon loses a number of Hit Points equal to your level. All creatures in a @Template[type:burst|distance:20] within 60 feet take @Damage[(max(6,(@actor.level - 1)))d6|options:area-damage] damage with a [[Reflex]] save against your spell DC. The damage increases by 1d6 for each level you have beyond 7th. The damage's type is either fire damage if your eidolon is a fire elemental, or the same physical damage type as your eidolon's primary unarmed attack if your eidolon isn't a fire elemental. Elemental Burst gains any traits that your eidolon's unarmed attacks gain from elemental core.

**Source:** `= this.source` (`= this.source-type`)
