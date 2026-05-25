---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Agile]]", "[[Finesse]]", "[[Thrown 10]]", "[[Versatile s]]"]
price: "{'gp': 150}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The blade of this *+1 striking dagger* is made from the thigh bone of a canine that died in the act of protecting its master. A werecreature or other creature willingly under the effects of a non-permanent polymorph effect damaged by a *dog-bone knife* must succeed at a DC 19 [[Will]] save or immediately revert to its natural form-this has no effect on a creature unwillingly polymorphed. On a successful save, the creature is temporarily immune to this effect for 1 minute. Kushtakas and other creatures vulnerable to canines take a -2 circumstance penalty to saves against this effect, and this weapon overcomes any resistance such creatures have to physical attacks.

**Source:** `= this.source` (`= this.source-type`)
