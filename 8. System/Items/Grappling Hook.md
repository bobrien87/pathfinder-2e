---
type: item
source-type: "Remaster"
level: "0"
price: "{'sp': 1}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

You can throw a grappling hook with a rope tied to it to make a climb easier. To anchor a grappling hook, make a ranged attack roll using your simple weapon proficiency against a DC depending on the target, typically at least DC 20. This attack has the secret trait. On a success, your hook has a firm hold, but on a critical failure, the hook seems like it will hold but actually falls when you're partway up

**Source:** `= this.source` (`= this.source-type`)
