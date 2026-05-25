---
type: action
source-type: "Remaster"
traits: ["[[Concentrate]]"]
cast: "`pf2:2`"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Requirements** Your swarm is within your body

**Effect** Your swarm boils forth from your body into a space adjacent to yours. (Its space can overlap yours.) It remains separate from you until the end of your next turn, but you can Sustain the effect up to 1 minute. The effect also ends if you end your turn more than 60 feet away from the swarm. When you use Swarm Forth and each time you Sustain the effect, you can have the swarm Stride.

**Source:** `= this.source` (`= this.source-type`)
