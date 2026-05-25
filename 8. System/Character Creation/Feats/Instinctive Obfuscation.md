---
type: feat
source-type: "Remaster"
level: "13"
traits: ["[[Gnome]]", "[[Illusion]]", "[[Visual]]"]
prerequisites: "at least one arcane or occult innate spell gained from a gnome heritage or gnome ancestry feat"
frequency: "once per PT1H"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per hour

**Trigger** You are attacked by a foe, but they haven't rolled yet.

The magic within you manifests as a natural reaction to threats. An illusory double of you appears in your space for a brief moment. The triggering attacker must roll a DC 10 flat check; on a success, the attack targets you normally; if they fail, the attack targets the double and destroys it. The tradition of this action matches the tradition of your gnome ancestry options.

**Source:** `= this.source` (`= this.source-type`)
