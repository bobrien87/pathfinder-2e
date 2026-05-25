---
type: item
source-type: "Remaster"
level: "6"
traits: ["[[Consumable]]", "[[Magical]]", "[[Missive]]"]
price: "{'gp': 50}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:2` (concentrate, manipulate)

You compose a heartening missive by creating a short message or image intended to grant the recipient moral support. You must dedicate the missive to an individual creature you know and address it to their location (typically the settlement where you think they are). Once you finish composing the missive, it folds itself into the shape of an animal and Flies at a speed of 45 feet (about 15 miles per hour) toward the location for up to 24 hours. It alights near the recipient or in their hand. After Activating the missive, the recipient gets its benefit and becomes temporarily immune to all heartening missives for 24 hours

If the missive fails to reach its recipient in 24 hours, it returns to its sender at the same pace, becoming non-magical when it arrives. After imparting or losing its magic, the missive remains as a normal document.

Folded into a square-shelled turtle, this missive grants the recipient a firm sense of self and serenity. The recipient gains a +1 item bonus to Will saves for the next 24 hours.

**Source:** `= this.source` (`= this.source-type`)
