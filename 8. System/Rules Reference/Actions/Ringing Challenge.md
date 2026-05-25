---
type: action
source-type: "Remaster"
traits: ["[[Sonic]]", "[[Spirit]]", "[[Transcendence]]"]
cast: "`pf2:2`"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

You clang your ikon against a weapon, shield, or the ground, emitting a shock wave that deals @Damage[(max(1,(floor((@actor.level - 2)/2))))d4[spirit],(max(1,(floor((@actor.level - 2)/2))))d4[sonic]|options:area-damage] damage to all creatures in a @Template[type:cone|distance:30] or @Template[type:emanation|distance:15] ([[Fortitude]] save). A creature that critically fails its saving throw is [[Deafened]] for 1 minute.

At 6th level and every 2 levels thereafter, the damage increases by 1d4 spirit damage and 1d4 sonic damage.

**Source:** `= this.source` (`= this.source-type`)
