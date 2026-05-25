---
type: feat
source-type: "Remaster"
level: "20"
traits: ["[[Sorcerer]]"]
prerequisites: "a bloodline based on a specific type of creature"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You permanently mutate to become more like the creatures of your bloodline. You gain the appropriate trait or traits for those types of creatures (aberration for aberrant, angel and celestial for angelic, demon and fiend for demonic, and so on). You gain low-light vision or darkvision, if one is appropriate for creatures with those traits. Choose one of the following.

- If the creatures associated with your bloodline have the ability to fly, you gain a fly Speed equal to your land Speed.
- If the creatures associated with your bloodline are aquatic or amphibious, you become amphibious, able to breathe water and air equally well, and you gain a swim Speed equal to your land Speed.
- If creatures associated with your bloodline have a resistance or immunity to acid, cold, electricity, fire, void, or sonic, choose an energy type your bloodline is immune or resistant to and gain resistance 20 against that energy type.

**Source:** `= this.source` (`= this.source-type`)
