---
type: feat
source-type: "Remaster"
level: "6"
traits: ["[[Air]]", "[[Illusion]]", "[[Impulse]]", "[[Kineticist]]", "[[Overflow]]", "[[Primal]]"]
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Compact layers of air diffract and bend light around your body, making you appear as clear as the sky on a perfect day. You become [[Invisible]] until the end of your next turn. You can Sustain the impulse. If you use a hostile action, the impulse ends after that action is completed. If you activate your kinetic aura, the impulse conceals its elements, though any special effects of your aura might give away your location.

This impulse weakens if you use it too frequently. Using it again within 10 minutes makes you [[Concealed]] instead of invisible.

**Level (10th)** The impulse doesn't end if you take a hostile action, but if you're invisible, you become concealed instead of invisible until the start of your next turn.

**Level (16th)** Taking a hostile action has no effect on the impulse.

**Source:** `= this.source` (`= this.source-type`)
