---
type: spell
sub-type: "Ritual"
source-type: "Remaster"
level: "10"
traits: ["[[Trial]]"]
cast: "1 day"
source: "Pathfinder Lost Omens Tian Xia World Guide"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Many have pursued alchemical means to immortality, and most haven't survived the attempt. The most common manner of purifying one's essence requires ingesting the following poison, and surviving the effects unassisted for at least a day.

**Saving Throw** DC 43 [[Fortitude]] save

**Onset** 1 hour

**Maximum Duration** 5 days

**Stage 1** 7d12 spirit damage plus [[Doomed]] 1 (1 hour)

**Stage 2** 9d12 spirit damage and [[Confused]] for 1 minute once every 1d4 minutes, plus [[Doomed]] 2 (1 hour)

**Stage 3** 9d12 spirit damage and [[Doomed]] 3 (1 day)

**Stage 4** death

Anathema for this ritual is determined at the time of the ritual. You choose 1 anathema, and the GM chooses 2 anathema. You're aware of all of your anathema. Appropriate anathema might include avoiding physical contact with a certain creature or substance (such as members of your bloodline or jade), eating certain foods (such as meat or grains), or wearing certain items or materials (such as silk or cotton). If the ritual is ended in this way, you must conduct an [[Atone]] ritual before attempting this ritual again.
- **Critical Success** As success, except you choose 1 anathema and your GM chooses 1 anathema.
- **Success** You've purified your body enough to attempt to attain immortality. You're bound by the ritual's anathema and must ingest the final potion to complete your apotheosis. Once you've withstood the effects of the poison for 1 day or completely recovered from the poison's effects without outside assistance, you gain immortality as follows: you don't age unless you wish to. You can't die except due to old age; if your dying or doomed condition would increase to a high enough value to kill you, it doesn't increase, and any effect that would instantly kill you instead just reduces you to 0 Hit Points. If you ever truly die and aren't returned to life within 1 year, you descend from the Heavens as an adult into a new mortal body somewhere in the world.
- **Failure** Your actions don't achieve immortality, and you automatically fail the first save against the poison.
- **Critical Failure** As failure, except the poison is also virulent.

**Source:** `= this.source` (`= this.source-type`)
