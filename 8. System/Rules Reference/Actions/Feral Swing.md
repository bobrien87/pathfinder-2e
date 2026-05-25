---
type: action
source-type: "Remaster"
traits: ["[[Spirit]]", "[[Transcendence]]"]
cast: "`pf2:2`"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

You lash out with both arms, rending all before you. Each creature in a @Template[type:cone|distance:15] must succeed at a [[Reflex]] save against your class DC or take spirit damage equal to your normal Strike damage with your [[Hands of the Wildling]].

You can choose to swing with abandon, which imposes a –2 circumstance bonus to enemies' saving throws, but causes you to become [[Off Guard]] until the start of your next turn.

> [!danger] Effect: Feral Swing

**Source:** `= this.source` (`= this.source-type`)
