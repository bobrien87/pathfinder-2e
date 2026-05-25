---
type: action
source-type: "Remaster"
traits: ["[[Concentrate]]"]
cast: "`pf2:1`"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

You issue an order to your follower, granting them 2 actions. This action has the auditory or visual trait depending on the method of communication used, but it must have one or the other. You can Direct your Follower to perform any of the following basic actions: [[Crawl]], Drop Prone, [[Escape]], Interact, [[Leap]], Release, [[Seek]], [[Sense Motive]], Stand, Step, Stride, and Strike. They can only use the Strikes listed in their stat blocks. Followers that gain a burrow Speed or fly Speed can use Burrow or Fly, respectively. You can also direct your follower to use skill actions for which they meet the prerequisites. Finally, you can direct the follower to perform any actions listed in their stat block. Unlike an animal companion's support actions, these special actions don't impose restrictions on the other actions a follower can use on this turn.

**Source:** `= this.source` (`= this.source-type`)
