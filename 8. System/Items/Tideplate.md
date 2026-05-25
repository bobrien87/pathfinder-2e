---
type: item
source-type: "Remaster"
level: "10"
price: "{'gp': 1000}"
bulk: "4"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Rippling water motifs decorate this simple suit of +1 *resilient full plate*. The plate has been altered for underwater use, so it's check penalty doesn't apply to Acrobatics or Athletics checks in water or similar liquids. While wearing the armor, you gain a +2 item bonus to Athletics checks to Swim, and you can breathe underwater.

**Activate—Ride the Waves** `pf2:2` (concentrate, manipulate)

**Frequency** once per hour

**Effect** The ripples on the armor begin to undulate, matching the movement of any nearby water. The armor casts [[Water Walk]] on you.

**Activate—Submerge** `pf2:2` (concentrate, manipulate, polymorph)

**Frequency** once per day

**Requirements** You're in water that covers at least half of your body.

**Effect** You merge with the water for 10 minutes. While merged, you can't move, you can see through the water if it's clear enough, and you can hear what's going on outside of the water. Water typically can't take damage, but if the water you're merged in is subject to electricity damage or an ability or effect that destroys or dries water, you're expelled from the water and take 10d6 damage. *Control water* expels you without dealing damage.

**Source:** `= this.source` (`= this.source-type`)
