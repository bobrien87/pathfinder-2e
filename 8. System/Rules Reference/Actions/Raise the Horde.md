---
type: action
source-type: "Remaster"
traits: ["[[Concentrate]]", "[[Magical]]", "[[Manipulate]]"]
cast: "`pf2:2`"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Frequency** once per 10 minutes

**Effect** Your undead horde appears in an unoccupied space within 30 feet. Choose whether your horde consists of skeletons or zombies, which affects the type of damage it deals with Mobbing Assault. Your horde remains summoned until the end of your next turn, but you can Sustain the effect for up to 1 minute. The effect also ends if you end your turn more than 120 feet away from the horde. When you first use Raise the Horde and each time you Sustain the effect, you can have the horde Stride.

When Raise the Horde ends, the undead that comprise your horde collapse lifelessly to the ground and quickly rot away. They can no longer be targeted or used for actions.

**Source:** `= this.source` (`= this.source-type`)
