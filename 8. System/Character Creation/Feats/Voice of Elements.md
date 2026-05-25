---
type: feat
source-type: "Remaster"
level: "2"
traits: ["[[Kineticist]]"]
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You can speak with the secret tones of elements you channel, finding words in the crackle of flame, the grinding of stone. Your kinetic aura grants you these three benefits while active.

- You can speak all the languages of your kinetic elements (Sussuran for air, Petran for earth, Pyric for fire, Talican for metal, Thalassic for water, Muan for wood).

- You can communicate with mindless elementals on a basic level if they have a trait that matches one of your kinetic elements or are made of one of those elements. This allows you to use Diplomacy to [[Make an Impression]] on them and to make very simple [[Requests]].

- You gain a +2 circumstance bonus to Charisma-based skill checks you attempt against elementals of one of your kinetic elements.

**Source:** `= this.source` (`= this.source-type`)
