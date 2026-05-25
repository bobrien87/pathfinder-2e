---
type: feat
source-type: "Remaster"
level: "6"
traits: ["[[Air]]", "[[Composite]]", "[[Impulse]]", "[[Kineticist]]", "[[Primal]]", "[[Wood]]"]
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

An ephemeral tree bursts forth, floating on air in an unoccupied square of your choice within 60 feet. Blooming flowers and fungal growths shed pollen and spores, which a swirling gust of air spreads in a @Template[emanation|distance:10] around it. The tree lasts until the end of your next turn, and you can Sustain it up to 1 minute. This has both of the following effects.

- **Cleansing Pollen** (healing, vitality) Each living ally that's in the area or enters it regains @Damage[(floor((max(6,@actor.level)-6)/2)+3)d4[healing]] HP and is then temporarily immune to regaining HP from Tree of Duality for 10 minutes.
- **Hallucinogenic Spores** (mental) Enemies in the area are [[Dazzled]]. An enemy that leaves the area remains dazzled until the start of its next turn.

**Level (+2)** The healing increases by 1d4.

**Source:** `= this.source` (`= this.source-type`)
