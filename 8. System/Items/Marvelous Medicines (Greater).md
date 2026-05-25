---
type: item
source-type: "Remaster"
level: "18"
traits: ["[[Magical]]"]
price: "{'gp': 19000}"
usage: "held-in-two-hands"
bulk: "1"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This healer's toolkit contains a seemingly endless supply of bandages, herbs, and healing items of impeccable quality, granting you a +3 item bonus to Medicine checks.

If you use the *marvelous medicines* when you [[Treat Poison]] or [[Treat Disease]], before you roll your check, the medicines attempt to counteract the poison or disease you're treating, with a counteract rank of 8 and a counteract modifier of +30. This is a healing effect.

The medicines can't be used to treat the same affliction for that patient again

**Source:** `= this.source` (`= this.source-type`)
