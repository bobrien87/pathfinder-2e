---
type: action
source-type: "Remaster"
cast: "`pf2:0`"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Trigger** Your turn begins.

You wait for the right moment to act. The rest of your turn doesn't happen yet. Instead, you're removed from the initiative order. You can return to the initiative order as a free action triggered by the end of any other creature's turn. This permanently changes your initiative to the new position. You can't use reactions until you return to the initiative order. If you Delay an entire round without returning to the initiative order, the actions from the Delayed turn are lost, your initiative doesn't change, and your next turn occurs at your original position in the initiative order.

When you Delay, any [[Persistent Damage]] or other negative effects that normally occur at the start or end of your turn occur immediately when you use the Delay action. Any beneficial effects that would end at any point during your turn also end. The GM might determine that other effects end when you Delay as well. Essentially, you can't Delay to avoid negative consequences that would happen on your turn or to extend beneficial effects that would end on your turn.

**Source:** `= this.source` (`= this.source-type`)
