---
type: spell
sub-type: "Ritual"
source-type: "Remaster"
level: "6"
traits: ["[[Air]]", "[[Illusion]]", "[[Visual]]"]
cast: "1 day"
duration: "8 hours"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You emblazon a message across the sky itself. Casting the ritual requires choosing a set of symbols for the message you want to send, which you can convey with an atmospheric phenomenon of your choice. Common choices include carefully shaped clouds during the day and auroras at night. Some cultures—such as the many denizens of the Plane of Air and star-gazing iruxis—develop complex symbology to communicate clearly using *sky signs*.

The message appears in the sky above you and can be seen to the horizon. To be conveyed in this way, the message must be very simple—typically something that can be expressed in 5 words or fewer. The symbols look the same to anyone who sees them. If you wish to conceal a message, you need to choose symbols that will make sense to your chosen audience but not to any other onlookers.
- **Critical Success** You display your chosen signs, and the message is clear to anyone who sees it.
- **Success** You display a somewhat muddled version of your message. The signs aren't entirely clear and require interpretation from those who view them—and many interpret them incorrectly.
- **Failure** You're unable to show your message.
- **Critical Failure** The spirits of air find your message audacious and offensive. As punishment, they emblazon the opposite of your intended message across the sky, and the message is clear to anyone who sees it.

**Heightened (10th)** The scope of your message is truly staggering and can be seen across the entire planet.

**Source:** `= this.source` (`= this.source-type`)
