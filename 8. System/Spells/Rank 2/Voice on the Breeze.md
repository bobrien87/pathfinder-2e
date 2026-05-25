---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "2"
traits: ["[[Air]]", "[[Concentrate]]", "[[Manipulate]]"]
cast: "`pf2:2`"
range: "10 miles"
area: "10-foot burst"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You whisper a secret message or sound into the wind, which carries it to a designated spot. The message travels to a specific @Template[burst|distance:10] within range that's familiar to you, provided there's a path for the wind to follow between you and the area. The gentle breeze goes all but unnoticed until it reaches its destination, where it delivers its whisper-quiet message. The message is delivered regardless of who or what is present to hear it, even if no one receives it at all. Once the message is delivered, the spell ends.

Your message can contain no more than 25 words, 1 round's worth of other sounds, or a simple rustling in the air at the target location. It moves at a speed of your choosing between 1 mile per hour and 1 mile per 10 minutes; when it arrives, the wind swirls around the area and whispers the full message. A voice on the breeze can't activate magical effects triggered by voices.

**Heightened (4th)** The range increases to 1,000 miles, and the message can contain up to 100 words.

**Source:** `= this.source` (`= this.source-type`)
