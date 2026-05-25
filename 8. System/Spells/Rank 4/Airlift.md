---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "4"
traits: ["[[Air]]", "[[Concentrate]]", "[[Manipulate]]"]
cast: "`pf2:2`"
area: "10-foot emanation"
defense: "Reflex"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

A massive rush of wind lifts, briefly carrying you and everything around you to a nearby destination. You, each creature in the area, and each item of 10 Bulk or lighter are lifted by this powerful gale. You and all affected creatures and objects Fly up to 60 feet and land on a solid surface, arriving in the same relative position to each other. If there wouldn't be enough room at the destination for everything you're bringing, the spell fails, though the GM might allow you to rearrange the group slightly to accommodate the spell.

Any unwilling participant can attempt a Reflex save to avoid being carried along. The *airlift* doesn't carry items that are secured in place (such as a hinged door or a person manacled to a wall).

**Heightened (6th)** The distance you Fly increases to 120 feet, and the Bulk limit of an item you can airlift increases to 20.

**Source:** `= this.source` (`= this.source-type`)
