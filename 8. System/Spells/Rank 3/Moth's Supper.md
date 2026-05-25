---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "3"
traits: ["[[Concentrate]]", "[[Manipulate]]"]
cast: "`pf2:2`"
duration: "1 hour"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You sigh, and your breath transforms into delicate, black-winged butterflies and huge death's-head hawkmoths. They flutter about you briefly, and then range forth in search of sustenance—fresh-spilled blood, by preference, but rotting corpses, flowering plants, or even left-behind food will do in a pinch. They then return, perching on your hair or shoulders and whispering their secrets into your ears. This has three effects.

- You heal 2d4 Hit Points every 10 minutes.
- The first time during the duration when someone successfully Treats your Wounds, you regain an additional 4d4 Hit Points.
- You gain an imprecise sense out to 30 feet that senses only freshly spilled blood and rotten flesh.

**Heightened (+1)** The amount of Hit Points healed every 10 minutes increases by 1d4 and the amount of Hit Points regained from the first [[Treat Wounds]] increases by 2d4.

**Source:** `= this.source` (`= this.source-type`)
