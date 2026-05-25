---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Commander]]", "[[Manipulate]]"]
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You plant your banner to inspire your allies to hold the line. Plant your banner in a corner of your square. Each ally within a @Template[type:burst|distance:30] centered on your banner immediately gains 4 temporary Hit Points, plus an additional 4 temporary Hit Points at 4th level and every 4 levels thereafter. These temporary Hit Points last for 1 round; each time an ally starts their turn within the burst, their temporary Hit Points are renewed for another round.

> [!danger] Effect: Plant Banner

While your banner is planted, you must signal your tactics abilities using only auditory signals. If your banner is attached to a weapon, you cannot wield that weapon while your banner is planted. While your banner is planted, any effects that normally happen in an emanation around your banner instead happen in a burst that is 10 feet larger (so a @Template[type:emanation|distance:30] becomes a @Template[type:burst|distance:40]). The weapon or pole your banner is attached to gains an amount of additional Hardness equal to your level + your Intelligence modifier.

You can use this action again while adjacent to your banner to retrieve it. An enemy adjacent to the square you planted your banner in can remove your banner as an Interact action, ending this effect and preventing you and your allies from gaining any of your banner's other benefits until you have successfully retrieved it.

**Source:** `= this.source` (`= this.source-type`)
