---
type: item
source-type: "Remaster"
level: "0"
price: "{'sp': 1}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

One of the more prolifically used devices developed in the infamous Alkenstar Gunworks, these small firearm components are capable of muffling most of the weapons' explosive sound when fired. Without a silencer, a firearm's shot makes a loud and distinctive bang, which can easily be heard through doors and thin walls, but firearms equipped with silencers only make a quiet noise when fired. Due to engineering constraints, a silencer can't be attached to any firearm with the scatter trait. Attaching a silencer to a firearm takes 1 minute, and the silencer is consumed the first time a shot is fired through it.

**Source:** `= this.source` (`= this.source-type`)
