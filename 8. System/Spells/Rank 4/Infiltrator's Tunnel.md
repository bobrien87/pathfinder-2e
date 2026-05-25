---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "4"
traits: ["[[Concentrate]]", "[[Manipulate]]", "[[Teleportation]]"]
cast: "`pf2:2`"
range: "60 feet (see text)"
defense: "Will"
duration: "1 minute"
source: "Pathfinder NPC Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

It's best to know the ingress and egress points for any location you plan to rob. But it's even better to make your own! You create two portals. One appears on a flat surface you can touch, and the other appears on a different flat surface in range that you can see.

You can move through the portals as though they were adjacent to each other. Any other creature attempting to move through the portals must succeed at a Will saving throw or be teleported up to 30 feet away from their starting point to a random safe space determined by the GM.

**Heightened (6th)** When you Cast the Spell, you can designate up to 5 other creatures to freely move between the portals.

**Source:** `= this.source` (`= this.source-type`)
