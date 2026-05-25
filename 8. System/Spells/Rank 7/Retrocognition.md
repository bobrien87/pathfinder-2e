---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "7"
traits: ["[[Concentrate]]", "[[Manipulate]]"]
cast: "1 minute"
duration: "sustained"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Opening your mind to mental echoes, you gain impressions from past events that occurred in your current location. *Retrocognition* reveals psychic impressions from events that occurred over the course of the last day throughout the first minute of the duration, followed by impressions from the next day back the next minute, and so on. These echoes don't play out like a vision but instead reveal impressions of emotions and metaphors that provide cryptic clues and details of the past. If you witness a traumatic or turbulent event through an impression, the spell ends unless you succeed at a Will save with a DC of at least 30 and possibly as much as 50, depending on the severity of the event. The GM determines whether an event is traumatic and chooses the DC.

**Heightened (8th)** You gain impressions of events that occurred over the previous year for each minute you concentrate, instead of the previous day, though the details diminish, making it harder to distinguish impressions from all but the most major events.

**Heightened (9th)** You gain impressions of events that occurred over the previous century for each minute you concentrate, instead of the previous day, though the details diminish, making it almost impossible to distinguish impressions from all but the most major events.

**Source:** `= this.source` (`= this.source-type`)
