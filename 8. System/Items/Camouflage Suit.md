---
type: item
source-type: "Remaster"
level: "3"
price: "{'gp': 10}"
usage: "worn"
bulk: "L"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This lightweight mesh fits easily over light armor. The suit is designed to incorporate local flora and ground clutter into the mesh to help you blend in seamlessly with the environment. Due to the abrasive nature of the materials used, this item is unsuitable for use by unarmored characters. You can prepare the suit for use within your current environment by using an exploration activity that takes at least 10 minutes, but sometimes longer if the materials are hard to find or the environment is unusual enough to warrant additional difficulty in preparing camouflage that can blend with it consistently.

A suit prepared in this manner grants you a +1 item bonus to Stealth checks while you attempt to Hide or Sneak in the specific environment it has been prepared for. The suit remains usable in this manner until you rest for the night, though it doesn't grant the benefit whenever you aren't in the appropriate environment. The GM might rule that some environments are unusual enough that you can't create a camouflage suit appropriate for the environment.

> [!danger] Effect: Prepared Camouflage Suit

**Source:** `= this.source` (`= this.source-type`)
