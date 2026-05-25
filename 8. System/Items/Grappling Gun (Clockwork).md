---
type: item
source-type: "Remaster"
level: "1"
price: "{'gp': 15}"
usage: "held-in-two-hands"
bulk: "1"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This wooden, pistol-like device features a large reel coiled with 100 feet of thin metal cord and can fire a grappling hook up to 100 feet. To reload the grappling gun, you must manually recoil the cord by turning the reel's crank, and then lock in the grappling hook. Reloading a grappling gun takes 1 minute.

Clockwork controls the reel on this grappling gun, reeling the grappling hook back in when you pull a lever. Reloading a clockwork grappling gun takes three Interact actions.

**Source:** `= this.source` (`= this.source-type`)
