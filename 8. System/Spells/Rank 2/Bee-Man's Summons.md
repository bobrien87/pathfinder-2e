---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "2"
traits: ["[[Auditory]]", "[[Concentrate]]", "[[Linguistic]]", "[[Mental]]"]
cast: "`pf2:2`"
area: "500-foot emanation"
duration: "until the next time you make your daily preparations or until discharged"
source: "Pathfinder #201: Pactbreaker"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You recreate the Bee-Man's infamous ability to sense when someone utters their name. During the spell's duration, you mentally sense whenever someone (referred to as a speaker) speaks your full name while within the spell's area. You gain a vague sense of the speaker's identity, such as "a local farmer" or "a halfling in distress," unless the speaker is someone you have met and interacted with before, in which case you recognize the speaker specifically. As a reaction within 1 minute of the speaker's utterance, you can send the speaker a telepathic prompt, asking if they intend to summon you. If they respond affirmatively, the spell's remaining duration decreases to sustained (up to 10 minutes), during which time you know the direction to where the speaker named you and how far away they are.

**Heightened (4th)** The emanation's radius increases to 1,000 feet.

**Heightened (7th)** The emanation's radius increases to 1 mile, and instead of locating the speaker, you can instead converse with the speaker for 5 minutes. This otherwise works as sending.

**Heightened (9th)** As 7th, except the emanation's radius increases to 5 miles, and the duration of the conversation is 10 minutes.

**Source:** `= this.source` (`= this.source-type`)
