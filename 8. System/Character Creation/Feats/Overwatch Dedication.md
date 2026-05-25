---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Overwatch|Overwatch]]"
source-type: "Remaster"
level: "2"
traits: ["[[Archetype]]", "[[Dedication]]"]
prerequisites: "expert in Perception"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You have an innate knack for tactical observation, and you've innovated to apply that knack in a variety of ways that allow you to assist your allies. With the help of enhanced visual gear (such as a specially modified telescope, goggled visor, or binoculars) and a set of carefully curated signals to share the information you uncover with your allies, you and your team are always keenly aware of the movement of combatants on the battlefield. You quickly and efficiently disperse the information you discover to your nearby allies so they can use it to direct their own observations and reactions to danger.

You're surrounded by an overwatch field aura in a 30-foot emanation. Your overwatch field aura grants you increased perception and allows you to call out warnings to your allies within the aura to point out threats. This aura has the auditory and visual traits. When you roll Perception for initiative, you and allies within your overwatch field receive a +2 circumstance bonus on your initiative rolls.

> [!danger] Effect: Overwatch Field

Overwatch

**Source:** `= this.source` (`= this.source-type`)
