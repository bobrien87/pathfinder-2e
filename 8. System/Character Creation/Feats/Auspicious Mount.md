---
type: feat
source-type: "Remaster"
level: "16"
traits: ["[[Champion]]"]
prerequisites: "Imposing Destrier"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Guided by your ongoing care, your steed has developed incredible intelligence and skill. The mount you gained with Faithful Steed is now a specialized animal companion. You can select one of the usual specializations or the auspice specialization. A faithful steed with the auspice specialization gains the following benefits.

- It gains the celestial, fiend, or monitor trait—whichever best matches your deity's servitors, and its appearance shifts to look more like those servitors. It also gains the holy trait if it's a celestial or the unholy trait if it's a fiend.
- Its Intelligence modifier increases by 2 and its Wisdom modifier by 1.
- Its proficiency rank in Religion increases to expert.
- It can speak the language associated with your deity's servitors (such as Empyrean for celestials, Chthonian for demons, or Requian for psychopomps).
- Its maximum Hit Points increase by 20, increasing to 25 at 18th level and 30 at 20th level. If the mount has the celestial trait, the extra HP increase by 5, and the mount gains weakness 5 to unholy. If it has the fiend trait, the extra HP increase by 5, and the mount gains weakness 5 to holy.
- It gains wings that grant it a fly Speed equal to its land Speed.

**Source:** `= this.source` (`= this.source-type`)
