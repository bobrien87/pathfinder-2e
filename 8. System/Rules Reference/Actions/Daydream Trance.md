---
type: action
source-type: "Remaster"
traits: ["[[Mental]]", "[[Occult]]"]
cast: "`pf2:1`"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

You fall into a half-sleeping trance. This lasts for 1 minute or until you fall [[Unconscious]], whichever comes first. You can attempt to Dismiss your trance, but your attempt fails unless you succeed at a [[Will]] save saving throw against your own class DC or spell DC, whichever is higher. Once your trance ends, you can't enter a Daydream Trance again for 1 minute. While you're in your trance, you gain the following effects:

- You gain a +1 status bonus to Will saves. This bonus increases to +2 against mental effects. If you're legendary in Occultism, the bonus against mental effects increases to +3.
- You take a –1 penalty to Perception checks and initiative rolls.

**Source:** `= this.source` (`= this.source-type`)
