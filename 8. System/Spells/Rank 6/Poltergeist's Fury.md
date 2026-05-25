---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "6"
traits: ["[[Concentrate]]", "[[Manipulate]]"]
cast: "`pf2:3`"
area: "20-foot emanation"
defense: "basic Reflex"
duration: "1 minute (sustained)"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Your fury spills over in a telekinetic storm of terrifying proportions. Any loose, unattended objects of 1 Bulk or less within range are picked up and begin to orbit you at breathtaking speeds. All creatures in the area take 6d4 piercing damage with a basic Reflex save. Each time you Sustain the spell, you can increase the radius of the storm by 10 feet, to a maximum of 100 feet. The storm moves with you and provides you with lesser cover, though you can't use this cover to hide or sneak. Allies within the storm who roll a success on their Reflex save against your poltergeist's fury get a critical success instead, as you attempt to avoid hitting them.

**Heightened (+1)** The damage increases by 1d4.

**Source:** `= this.source` (`= this.source-type`)
