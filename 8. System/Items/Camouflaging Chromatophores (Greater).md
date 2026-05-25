---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Graft]]", "[[Invested]]", "[[Magical]]"]
price: "{'gp': 665}"
usage: "implanted"
bulk: "—"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Special cells in your skin can change color to help you blend in with your environment. You gain a +2 item bonus to Stealth checks to [[Sneak]] and [[Hide]].

**Activate—Background Adaptation** `pf2:2` (concentrate)

**Frequency** once per hour

**Effect** For 1 minute, you can Hide without needing cover or concealment to do so. This doesn't allow you to Sneak without ending your movement in cover or concealment, however, as your skin's attempts to match the background as you move produce noticeable rippling waves of color.

**Source:** `= this.source` (`= this.source-type`)
