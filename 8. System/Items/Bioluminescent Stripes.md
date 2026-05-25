---
type: item
source-type: "Remaster"
level: "1"
traits: ["[[Graft]]", "[[Invested]]", "[[Light]]", "[[Magical]]"]
price: "{'gp': 10}"
usage: "implanted"
bulk: "—"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A line of glands embedded in your skin secretes a chemical that glows when it interacts with the air. As a single action, you can activate your bioluminescent stripes to glow with a bright light in a 20-foot radius and dim light for the next 20 feet. While you are glowing, you can't be [[Undetected]] and you take a –4 item penalty to Stealth checks to [[Hide]] and [[Sneak]]. You can Dismiss the glow as a free action.

**Source:** `= this.source` (`= this.source-type`)
