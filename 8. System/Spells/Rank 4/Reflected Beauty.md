---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "4"
traits: ["[[Concentrate]]", "[[Illusion]]", "[[Manipulate]]", "[[Visual]]"]
cast: "`pf2:2`"
duration: "1 hour"
source: "Pathfinder #205: Singer, Stalker, Skinsaw Man"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

When you cast reflected beauty, choose a willing creature that's the same size as you and that you can see within 30 feet. The spell then disguises you with a realistic illusion, as if via [[Illusory Disguise]] heightened to 3rd rank, but includes tactile and olfactory sensation in addition to visual and voice. The appearance of the illusion that disguises you includes any changes to sex characteristics or other aspects needed to match the target creature's heart's desire, allowing you to interact with them as the person they could be. If you're ever more than 30 feet from the subject you're reflecting, *reflected beauty* immediately ends. You can Dismiss this spell.

**Source:** `= this.source` (`= this.source-type`)
